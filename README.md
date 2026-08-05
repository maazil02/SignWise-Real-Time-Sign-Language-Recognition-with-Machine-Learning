
# SignWise: Real-Time Sign Language Recognition with Machine Learning

## Overview

SignWise is a real-time sign language detection system that uses **Computer Vision** and **Machine Learning** to recognize hand gestures from a webcam. The project aims to bridge the communication gap between sign language users and non-signers by providing accurate gesture recognition in real time.

---

# Features

* Real-time hand gesture detection
* Sign language recognition using a CNN model
* Automatic hand tracking and landmark detection
* Custom dataset collection using a webcam
* Live prediction with gesture labels
* Easy-to-use and scalable architecture

---

# Technology Stack

* **Programming Language:** Python
* **Computer Vision:** OpenCV
* **Hand Tracking:** cvzone
* **Machine Learning:** TensorFlow / Keras
* **Model:** Convolutional Neural Network (CNN)
* **IDE:** Visual Studio 2022

---

# System Requirements

## Hardware

* Intel Core i5/i7 or higher
* 4 GB RAM (minimum)
* 8 GB free disk space
* Webcam

## Software

* Windows 10 or later
* Python 3.x
* Visual Studio 2022 (or any Python IDE)

---

# Project Workflow

The project follows the following workflow:

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Model Training (CNN)
        │
        ▼
Model Testing
        │
        ▼
Real-Time Gesture Recognition
```

---

# Implementation

### 1. Data Collection

The dataset is created by capturing hand gesture images through a webcam. Each gesture is stored with its corresponding label to prepare the data for supervised learning.

### 2. Data Preprocessing

The collected images are:

* Resized to a fixed resolution (300 × 300)
* Normalized
* Cropped around the detected hand
* Cleaned to reduce noise and improve consistency

### 3. Model Training

A Convolutional Neural Network (CNN) is trained on the prepared dataset. The dataset is divided into training and validation sets, allowing the model to learn gesture patterns and improve prediction accuracy.

### 4. Real-Time Prediction

The trained model processes live webcam frames, detects the hand, classifies the gesture, and displays the predicted sign instantly.

---

# Project Modules

## 1. Data Collection Module

Responsible for generating the training dataset.

**Functions**

* Captures webcam frames
* Detects hands using **cvzone**
* Crops and resizes images to **300 × 300**
* Saves images with timestamps
* Displays live preview

---

## 2. Hand Tracking Module

Uses **cvzone's HandTrackingModule** to detect and track hands.

**Functions**

* Hand detection
* Landmark extraction
* Bounding box generation
* Gesture visualization
* Real-time tracking

---

## 3. Gesture Recognition Module

Performs sign language prediction using the trained CNN model.

**Functions**

* Captures webcam input
* Detects and crops the hand
* Preprocesses the image
* Predicts the gesture
* Displays the predicted label in real time

---

## Screenshots
<img width="274" height="267" alt="Screenshot 2024-04-05 000914" src="https://github.com/user-attachments/assets/0555c7eb-5e76-41ae-b8c9-a056b630fd35" />
<br/>
<img width="543" height="336" alt="Screenshot 2024-04-05 004506" src="https://github.com/user-attachments/assets/c5cfb5b1-2d82-4c5a-ae10-9a207062ca7c" />
<br/>
<img width="625" height="341" alt="Screenshot 2024-03-23 163658" src="https://github.com/user-attachments/assets/0fa49796-8057-4ea1-afa1-6a58511e65e4" />
<br/>
<img width="616" height="330" alt="Screenshot 2024-03-23 164004" src="https://github.com/user-attachments/assets/8c34de04-af5f-4cad-aeed-03a941633eef" />

---
