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



## Set Up
1. Check Python requirements
2. Download: https://drive.google.com/file/d/18bWyl_SieLtARy1tdjTIX25OAMIAVXHK/view?usp=sharing and place in `ProcessingServer/datasets` subfolder
3. On command prompt/terminal, cd into `ProcessingServer/src` subfolder for `ProcessingServer.py`
4. On second command prompt/terminal, cd into `CameraServer` subfolder for  `WebSocketServer.py`
5. Download `Brackets` application and open `Web` subfolder in application


## Ignore below this

#### Align Training Set (Isolate Face)
`python3 -W ignore src/align/align_dataset_mtcnn.py datasets/train datasets/train_clean`

#### Train Classifier
`python3 -W ignore src/classifier.py TRAIN datasets/train_clean /models/20180408-102900.pb models/classifier.pkl --batch_size 25`

#### Align Test
`python3 -W ignore src/align/align_dataset_mtcnn.py datasets/test datasets/test_clean`

#### Classification of Test Set
`python3 -W ignore src/classifier.py CLASSIFY datasets/test_clean models/20180408-102900.pb models/classifier.pkl`

#### To Classify Camera Inputs (separate from full networking application - only run to see classifier by itself)
Images must be saved in `datasets/test_pi` in `Unknown` subfolder

Align input: `python3 -W ignore src/align/align_dataset_mtcnn.py datasets/test_pi datasets/test_pi_clean`

`python -W ignore src/classifier.py CLASSIFY datasets/test_pi_clean models/20180408-102900.pb models/classifier.pkl > output.txt`

