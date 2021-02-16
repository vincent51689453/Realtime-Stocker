# Realtime-Stocker

**1. Install libraries**
---------------------------
After you have successfully install GPU version of Tensorflow & Keras,

1) pip install yahoo-fin          [or pip3]
2) pip install requests_html      [or pip3]
3) pip install python3-tk         [or pip3]
3) apt-get install python3-matplotlib 

**2. Startup**
---------------------------
1) Get realtime stock price
```
$ python3 save_data.py
```

2) Start auto AI analyze
```
$ python3 scheduler.py
```

**3. Sample Layout**
---------------------------
![image](https://github.com/vincent51689453/Realtime-Stocker/blob/main/git_image/layout_graph.PNG)


**4. Docker Image**
---------------------------
The complete installed libraries were embedded inside this docker image which tested by RTX2060 Super. 8GB RAM is required.

Link to docke image:
https://hub.docker.com/r/vincent51689453/stocker