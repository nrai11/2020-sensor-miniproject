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
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    #data['temperature'].median()

    file = Path(P.file).expanduser()
    data = load_data(file)

    df1 = data['temperature']
    df2 = data['occupancy']

    df1['combine'] = df1[['class1', 'lab1', 'office']].min(axis = 1)

    #print(df1['combine'].describe())
    #print(df1['combine'].quantile([0.2,0.4,0.6,0.8]))

    print('Temperature:\nmedian is {}\nvariance is {}'.format(df1['combine'].median(),
                                                df1['combine'].var()))


    df2['combine2'] = df2[['class1', 'lab1', 'office']].min(axis = 1)

    #print(df2['combine2'].describe())
    #print(df2['combine2'].quantile([0.2,0.4,0.6,0.8]))

    print('Occupancy:\nmedian is {}\nvariance is {}'.format(df2['combine2'].median(),
                                                df2['combine2'].var()))


    for k in data:
        # data[k].plot()
        time = data[k].index
        data[k].hist()
        plt.figure()
        plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        plt.xlabel("Time (seconds)")

    # plt.show()
