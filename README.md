# Face Recognition Based Attendance System

The Face Recognition Based Attendance System is a Python-based project that utilizes face recognition to automate attendance tracking. The system captures live video from a webcam, detects faces in the video stream, and matches them against a database of known faces to record attendance.

## Features

- Real-time face detection and recognition
- Automatic attendance logging in a CSV file
- Display of recognized faces and attendance status on the video feed

## Requirements

- Python 3.11
- OpenCV
- face_recognition

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/face-attendance-system.git

   ```

2. Install the required Python packages:

   ```shell
   pip install -r requirements.txt

   ```

3. Create Two directories with name Faces and Attendance respectively.

4. Place face images of the known individuals in Faces directory.

5. Each face image should contain only one face and be named after the person (e.g., john.jpg).

6. Run the program:

   ```shell
   python face_attendance.py

   ```

7. The program will open a window showing the video feed from the webcam.

8. As faces are detected and recognized, their names and attendance status (present) will be displayed on the video feed.

9. The attendance records will be stored in a CSV file named with the current date (DD-MM-YY.csv) in the Attendance directory.

10. To quit the program, press 'q' on the keyboard.

## Limitations

- The face recognition accuracy depends on the quality of the face images in the faces directory and environmental factors such as lighting and camera resolution.
- The system assumes that each person has only one face image in the faces directory. If multiple images are present, the system will use the first image for face recognition.

## Acknowledgements

- This project utilizes the face_recognition library by Adam Geitgey.
- The project was inspired by various face recognition and attendance tracking projects available online.

## License

This project is licensed under the MIT License.
