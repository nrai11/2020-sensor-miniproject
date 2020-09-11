#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.kde import gaussian_kde
from numpy import linspace


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index()
    }

    return data

def detectAnomalies(data):
    #list to add anomalies to, to be returned
    anomalies = []

    # calculate standard deviation
    standardDev = np.std(data)
    detect_anomaly = standardDev * 2

    meanVal = np.mean(data)
    # define outliers as outside 2 standard deviations from mean
    lowerBound = meanVal - detect_anomaly
    upperBound = meanVal + detect_anomaly

    # loop through data to identify anomalies
    for val in data:
        if val > upperBound or val < lowerBound:
            anomalies.append(val)
    return anomalies

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    data = load_data(file)

    df1 = data['temperature']
    df2 = data['occupancy']
    df3 = data['co2']

    #Print temperature and ccupancy median and variance
    print('Temperature Median:\n{}\nTemperature Variance:\n{}'.format(df1.median(),
                                                df1.var()))
    print('-------------------------------')
    print('Occupancy Median:\n{}\nOccupancy Variance:\n{}'.format(df2.median(),
                                                df2.var()))
    print('-------------------------------')

    #plot PDF of temperature sensor in office room
    plt.figure(0)
    plt.title("PDF of temperature sensor in office")
    pdf_temp = df1[['office']].min(axis = 1).plot.kde()

    #plot PDF of occupancy sensor in office room
    plt.figure(1)
    plt.title("PDF of occupancy sensor in office")
    pdf_occ = df2[['office']].min(axis = 1).plot.kde()

    #plot PDF of co2 sensor in office room
    plt.figure(2)
    plt.title("PDF of co2 sensor in office")
    pdf_co2 = df3[['office']].min(axis = 1).plot.kde()

    #plot PDF of 3 sensors in 3 rooms in histogram format
    for k in data:
        # data[k].plot()
        time = data[k].index
        data[k].hist()
        plt.figure(3)
        plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        plt.xlabel("Time (seconds)")

    #find time interval median and variance
    CO2 = data['co2']
    diff = np.diff(CO2.index).astype(np.int64) * 1e-9
    print('Time interval median:\n{}\nTime interval variance:\n{}'.format(np.median(diff), np.var(diff)))


    #find actual lowest and highest time interval
    [low, high] = np.quantile(diff, [0.5, 0.95])

    #Remove 0.5 and 0.95 quantile from data and plot PDF
    diff1 = [d for d in diff if d > low and d < high]
    kde = gaussian_kde(diff1)
    dist_space = linspace( min(diff1), max(diff1), 100 )


    plt.figure(6)
    plt.title("PDF of time interval (removed 0.05 and 0.95 quantile)")
    plt.plot( dist_space, kde(dist_space) )
    plt.show()
    
    findAnomalies = detectAnomalies(df1['combine'])
    print(findAnomalies)
