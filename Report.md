# Sensor Mini Project Report
## Task 0: 
The greeting string is: ECE Senior Capstone IoT simulator
## Task 1: 
Code was added to client.py to save data to a file when a .txt file name is provided when it is run.
## Task 2: 
We ran the server and collected the data in the file 'data.txt', which has 3130 data values. We have already calculated the median and variance for all sensors in three rooms, and they are listed below.
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
 
* We plotted probability density function for each sensor type from the **office** room which are as follow: 

*PDF are plotted in two formats, the left one is line graph and the right one is histogram.*

**Temperature sensor**

<img src="./img/pdf_temp.png" width="45%" /><img src="./img/hist_temp.png" width="45%" />

**Occupancy sensor**

<img src="./img/pdf_occ.png" width="45%" /><img src="./img/hist_occ.png" width="45%" />

**CO2 sensor**

<img src="./img/pdf_co2.png" width="45%" /><img src="./img/hist_co2.png" width="45%" />

* We ran the server for a period of time. The mean and variance of **Time interval** between sensor readings are:

 Mean | Variance 
 ----------- | ----------- 
1.0186770140620007 | 1.062734582236113


**Probability density function and histogram of the time interval**

<img src="./img/pdf_time.png" width="50%" /><img src="./img/hist_time.png" width="45%" />

* The PDF above shows a plot with 0.5 and 0.95 quantile removed to emphasize where most of the density are. The histogram above are plotted without any quantile removed. As seen from the histogram of time intervals above, most of the time intervals are between 0.1 to 0.8 seconds and there are some outliers up to 7 seconds. Connection intervals in large systems are usually in unit of millisecond (e.g. 0.007 seconds) so this hisogram does not qutie mimic distribution for connection intervals in large system in terms of numbers, but it does reflect distribution for connection intervals in terms of density. In large system, the connection intervals (time in seconds) is usually less than or similar to what is on the histogram above. A big factor that contributes to number discrepancy might be that the simulation wait to sends readings from three sensors out at the same time. In terms of density represented on the histogram, a well-known distribution for connection intervals in large system could have similar behavior which is that most of the sensor will transmit information in millisecond, but there could be some outliers in sensor readings due to external errors. Most the readings tend to fall in millisecond, however, there is also a chance that sometimes, sensors can transmit information faster or slower than the average millisecond due to error factors.


## Task 3:
* For our anomaly detection algorithm, we defined an anomaly to be outside of two standard deviations of the mean, and used these values to find anomalies and add them to a list, which is then returned. This was done in the analyze.py file, in the function detectAnomalies. The output of the function is displayed below, and shows a list of all the anomalies from each room, as well as the percentage of anomalies out of the total values collected.
 <img src="./img/anomalyPercent.PNG" width="100%" />
 * After filtering out the anomalies, we got the following new median and variance for the temperature data in Lab1:
 
 Room | Median | Variance 
 ----------- | ----------- |----------- 
 lab1 | 20.99933606970943 | 0.2191340158120675
 
 
* A persistent change in temperature may indicate a failed sensor, but it could also mean there is something wrong with the temperature of the room itself (e.g. a persistent higher temperature could indicate a fire). This is dependent on whether the sensor would continue to perform and send data under these conditions, but if so, this could be a reason for a persistent change in temperature, so this would not always indicate a failed sensor. However, since this project was using simulated sensors, I would assume that if there is a persistent change, it would indicate a malfunction with the simulated sensor since there isn't a physical room which may be having an external issue causing a change in temperature. 
* Since for our algorithm, we defined an upper and lower bound for detecting an anomaly, we can use those as our possible bounds for room temperature: 

 Room | Lower Bound | Upper Bound 
 ----------- | ----------- |----------- 
 class1 | 17.756367534250455 | 35.889437592286356
 lab1 | 17.54055048399767 | 24.620248204447925
 office | -4.757673873048333 | 49.644748112366656
 
 * The bounds for both class1 and lab1 seem reasonable, whereas for the office, the bounds are outside of what would be considered a normal temperature for a building. This likely means that the standard deviation was greater for the office, so the finding bounds from the mean lead to a greater range of 'valid' temperatures than would actually be reasonable. Since our algorithm was relatively basic, it did not account for this issue. 
 
## Task 4:
* In this simulation, there are several sensors in different rooms which reflect a real world scenario where there are usually more than one sensor to detect changes in several environmental conditions. Sensor readings are also done in time interval of millisecond or less to ensure accuracy in readings because in the real world, there is no places that always have a stable conditions and changes in these conditions can be within millisecond or less. Sensors can also be damaged by unprecedented incident/ uncontrollable enviromental factors which can result in sensor failures and erratic readings. In this simulation, we see anomalies in different sensor readings, this could be comparable to a real world scenario where for example, geotechnical sensors are damaged by natural lighting.

* This simulation fails to account for: first, the transmit time of each sensor in different rooms. Currently the simulation wait for readings from all three sensors to be collected before the readings are sent to the clients. In a real world scenario, each sensors might have different transmit time (e.g. temperature sensors might have readings out in 0.4 seconds but co2 has transmit time of 0.6 seconds). All readings should be sent to clients accordingly, there should be no wait time; data from different sensors do not need to be sent to clients at the same time. Second, this simulation fails to account for the fluctuations in data readings from all three sensors. As seen from data readings collected from three sensors, some of the variance values are quite high. If you use {dataframe name}.describe() to view the min and max data, you can see that some of the max and min values quite differ from the mean value. Sensor readings should be able to detect irregular fluctuations in readings and inform clients of the error.

* The difficulty of initially using this Python websockets library seemed to be less compared to a compiled language like C++. For context, in our team, we were both unfamiliar with Python as well as working with websockets. From looking at the examples of C++ websockets libraries, as well as an [online example of a C++ websocket](https://www.netburner.com/learn/websockets-for-real-time-web-and-iot-applications/), we found the Python syntax, which is much closer to pseudo-code/english, made it much easier to understand this Python websockets library, and what particular parts of the code were doing. Furthermore, there was relatively thorough documentation of the Python library that made working with it easier. If there were performance benefits to using one of the C++ libraries, this was not an issue that we encountered, and we found that the increased readability of the code compared to C++ implementations was more useful than having slightly optimised performance would be. 

* If the server polled the sensors, there would inevitably be connections where the sensors don't yet have data. On the other hand, if the sensors reach out to the server, that wouldn't be an issue as it would be guaranteed that there was data to be passed along. Additionally, having the sensors send the data when they get it means that they wouldn't need to use their storage to keep data if the server hasn't polled it yet, which may be good if they have limited storage. It would also mean that the server wouldn't have to store the results of the polls when no data was collected and they essentially got nothing. Furthermore, if the sensors had an unstable connection as some do, it may be more beneficial to have the sensors be able to send an asynchronous message rather than depending on them having a stable connection at the time the server polls it and the sensor needing to provide an immediate response. 
