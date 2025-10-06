# Face Attendance System

A real-time **facial recognition-based attendance system** built using **Python**, **OpenCV**, and **Firebase**. The system leverages **face_recognition** and **cvzone** libraries to identify students and maintain attendance records in a cloud database. It is designed for **secure, automated, and efficient tracking of attendance** in educational institutions or organizations.

## Features

- **Real-Time Face Recognition:** Captures video from a webcam and identifies faces in real time.
- **Firebase Integration:**  
  - **Authentication & Database:** Student data and attendance records are securely stored and managed in **Firebase Realtime Database**.  
  - **Cloud Storage:** Student images are fetched from **Firebase Storage**.
- **Role-Based Dashboard Display:** Shows student details such as Name, Roll Number, Starting Year, Total Attendance, and Last Attendance Time.
- **Attendance Tracking:** Automatically updates attendance if a student is recognized after a configurable time interval.
- **Interactive Visuals:**  
  - Dynamic overlays with student images and information.  
  - Custom backgrounds and mode-specific displays using OpenCV and cvzone.

## Tech Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV, face_recognition, cvzone, NumPy  
- **Backend & Cloud:** Firebase Realtime Database, Firebase Storage  
- **Utilities:** PrettyTable for tabular display  

## How It Works

1. The system loads pre-encoded face data from a serialized file (`EncodedFile.p`).  
2. Captures video frames from the webcam and detects faces using `face_recognition`.  
3. Matches detected faces with the known student encodings.  
4. Fetches student details and images from Firebase.  
5. Updates attendance in the Firebase Realtime Database if conditions are met.  
6. Displays student information and image overlays on a dynamic OpenCV window.  

## Usage

- Run the Python script with access to the webcam.  
- Ensure `serviceAccountKey.json` and `EncodedFile.p` are available in the project directory.  
- Press `q` to exit the real-time attendance window.
