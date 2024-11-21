### VR Viam Solutions Engineer Project

### Setup and run
* Activate the virtual environment with```source viam/bin/activate```
* Install needed Python packages with ```pip install requirements.txt```
* Make sure launch script is executable with ```chmod u+x launch_webcam_server```, launch server with  ```./launch_webcam_server```
* Run the person detector with ```python vision_detect.py```

### ASSIGNMENT
## Task 1: Vision
Using a camera, this could be the one on your laptop, or any USB camera. We would like to see
you implement a basic camera component in Viam and expand on it to make use of our vision
service to implement a simple object detector.<br>

## Task 2: Cloud Integration
Now that we have implemented our vision service, we would like you to implement our data
capture service to store camera frames into the cloud. How could we use this data to possibly
create a custom model? </br>
* https://docs.viam.com/fleet/data-management/

## Task 3: Modular Registry
When working with customers, we often come across a wide variety of hardware components
and systems that we have to integrate the Viam platform with. The Viam Registry allows
managing these custom integrations as so-called modules. The Registry is comparable to
Node.js npm or Python pip, just for what we call smart machines.

Now that we have our object detection working, we would like you to create a custom sensor
which will call the previously created vision service and return true if an object is detected or
false if no object is detected.

This will depend on the service created above with a single field called “person_detected” and it

is set to 1 if our detection has a person and 0 if no person is detected.
The goal of this exercise is to later show and explain how simple and fast you / our customers
can do this with the Viam platform.</br>

* https://docs.viam.com/how-tos/train-deploy-ml/

## Task 4: Describe Your Work
We would like you to give a short presentation (10-15 minutes) on your progress and results.
Please include:
* Screenshots
* Code samples
* Any notes on various approaches attempted


### Sources
* Installation guide - https://docs.viam.com/installation/viam-server-setup/#install-viam-server
* Person detection example - https://docs.viam.com/tutorials/projects/send-security-photo/
* https://docs.viam.com/how-tos/detect-people/