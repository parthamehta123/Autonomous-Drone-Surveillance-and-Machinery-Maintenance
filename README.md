# Autonomous-Drone-Surveillance-and-Machinery-Maintenance

Navigating over rough terrain is really difficult for humans & we often deploy autonomous vehicles for monitoring, yet we have vehicle maintenance & security issues which we need to address. This project focus on addressing this issue using an autonomous drone for machinery maintenance & surveillance. The drone primarily collects machine critical sensor information from the vehicle via a bi-directional communication channel using Zigbee. These data are further analyzed for an early warning anomaly detection system using LSTM to predict machine sensor failures. Secondly, while the drone is navigating over the terrain, we do real-time surveillance using an optimized YoloV3 model.  

Detailed description of the project is given in the report [Report](https://github.com/sand47/Autonomous-Drone-Surveillance-and-Machinery-Maintenance/blob/master/project_report.pdf)

# Object Detection 

**Note:** This is not the optimized Yolov3 code used in project but instead a generic code. Its not published due to IP concerns.  <br><br>
Download the yolov3 weights from https://pjreddie.com/darknet/yolo/ and place it inside the folder yolo-deep_learning
<br><br>
Upload images to be tested in yolo-deep_learning/output_aerial folder and run 
<br><br>
python yolo_drone.py 
<br><br>
Ouput images are stored in output folder 

 
