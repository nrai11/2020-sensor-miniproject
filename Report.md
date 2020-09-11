# Sensor Mini Project Report
## Task 0: 
The greeting string is: ECE Senior Capstone IoT Simulator
## Task 1: 
Code was added to client.py to save data to a file when a file name is provided when ws_client.py is run
## Task 2: 
We ran the server and collected the data in the file 'data.txt', which has 3130 data values.
* For the **temperature data**, the median and variance of each room are: 

 Room | Median | Variance 
 ----------- | ----------- | ----------- 
 class1 | 26.980973 | 20.570161 
 lab1 | 21.000710 | 3.135624 
 office | 23.008981 | 185.155364 
* For the **occupancy data**, the median and variance of each room are:

 Room | Median | Variance 
 ----------- | ----------- | ----------- 
 class1 | 19.0 | 19.203707 
 lab1 | 5.0 | 5.099918 
 office | 2.0 | 1.808376 
 
* We plotted probability density function for each sensor type from the office room which are as follow: 

*PDF are plotted in two formats, the left one is line graph and the righ one is histogram.*

**Temperature sensor**

<img src="./img/pdf_temp.png" width="45%" /><img src="./img/hist_temp.png" width="45%" />

**Occupancy sensor**

<img src="./img/pdf_occ.png" width="45%" /><img src="./img/hist_occ.png" width="45%" />

**CO2 sensor**

<img src="./img/pdf_co2.png" width="45%" /><img src="./img/hist_co2.png" width="45%" />

* We ran the server for a period of time. The median and variance of **Time interval** between sensor readings are:

 Median | Variance 
 ----------- | ----------- 
0.6966920000000001 | 1.062734582236113

> Consider the value of median, there might be errors in readings

**Probability density function of the time interval**
<img src="./img/pdf_time.png" width="45%" />


What is the mean and variance of the time interval of the sensor readings? Please plot its probability density function. Does it mimic a well-known distribution for connection intervals in large systems? [8 points]

## Task 3:
* For our anomaly detection algorithm, we defined an anomaly to be outside of two standard deviations of the mean, and used these values to find anomalies and add them to a list, which is then returned. This was done in the analyze.py file, in the function detectAnomalies.
## Task 4:
