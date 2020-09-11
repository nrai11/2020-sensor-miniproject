# Sensor Mini Project Report
## Task 0: 
The greeting string is: ECE Senior Capstone IoT Simulator
## Task 1: 
Code was added to client.py to save data to a file when a file name is provided when ws_client.py is run
## Task 2: 
We ran the server and collected the data in the file 'data.txt', which has ~3000 data values
* For the temperature data, the median is: 23.002888022722825 and the variance is: 75.13395189988015
* For the occupancy data, the median is: 5.0 and the variance is: 62.43182798860909
## Task 3:
* For our anomaly detection algorithm, we defined an anomaly to be outside of two standard deviations of the mean, and used these values to find anomalies and add them to a list, which is then returned. This was done in the analyze.py file, in the function detectAnomalies.
## Task 4:
