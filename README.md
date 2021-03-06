# IoT Computer Vision Networking App
---

## What
- A webcam that streams a live feed and can send the user a notification if it detects motion or people.

## Why
- Home security remains an important issue. Recently, for example, there have been several cases of thieves stealing packages from people’s porches and front doors. A security camera can help to keep a log of who enters or approaches a home.

## How
- A development board such as a Raspberry Pi/Pi Zero W can be used as a server which streams a live feed and sends notifications to a client.

## Deliverables
1. Network App (IoT Computer Vision)
2. Documentation


## Plan
| **Week** | **Tasks** |
| ----------- | ----------- |
| Week 1 | First progress report, research/literature review, get hardware/prototype, begin networking components |
| Week 2 | Networking components, begin application side, research web deployment |
| Week 3 | Work on application (Machine learning/computer vision), work on network components |
| Week 4 | Complete application, complete network, test, fix bugs |
| Week 5 | Fix bugs, Presentation, Code on GitHub/Documentation, Demo |

## Team Members
- Arianna Burch

- Tarek Elkheir

- Chris Villamarin

## Features/Project Flow

1. Captures video and retrieves individual image frames
2. Sends images to server for processing. 
3. Performances face detection, draws bounding boxes, aligns/crops image
4. Sends aligned images to display on webpage
5. Recognizes and classifies faces from trained model
6. Sends classification and confidence to display on webpage
7. Checks user access and sends alert to Raspberry Pi
8. Flash green or red LED light to simulate security system
9. Retrain or update model to include new users or other datasets
10. Dynamically updates website as new images/classifications are made


## Getting Started

### Install
1. Check Python requirements (see requirements.txt)
2. Install `brackets` application

### Run
1. On command prompt/terminal, cd into `ProcessingServer/src` subfolder for `ProcessingServer.py`
2. On second command prompt/terminal, cd into `CameraServer` subfolder for  `WebSocketServer.py`
3. On third prompt/terminal, again cd into `ProcessingServer/src` subfolder for `objectDetectionTest.py`
4. Download `Brackets` application and open `Web` subfolder in application
5. Run `ProcessingServer.py` (for Mac/Linux use sudo python3, for Windows, py)
6. Run `WebSocketServer.py`
7. Run `objectDetectionTest.py` to jumpstart python3 app (you won't need it after that)
8. Go to brackets open index.html from left sidebar. Click lightening icon on right side.

## Notes

If you are on a Mac or Linux and running the program multiple times, run `sudo lsof -i :21`, and `sudo lsof -i :5678`, collect the PIDs, and run `sudo kill -9 _PID_`

### Demo Videos

Demo to display CameraServer (laptop) interacting with WebServer to display PreprocessingServer results

https://youtu.be/4yIFA8Dnd2I

Demo to display CameraServer (laptop) interacting with ProcessingServer (also laptop) - which does image segmentation, then interacting with server on raspberry pi:

https://www.youtube.com/watch?v=tCcnDnl-gE0

Note: Demos were created with multiple faces to show robustness of our project (with help from friends who allowed us to train on them). 

