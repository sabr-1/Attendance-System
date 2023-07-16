import face_recognition
import cv2
import os
import numpy as np
import csv
from datetime import datetime

# Initialize video capture from webcam
video_capture = cv2.VideoCapture(0)

# Directory containing the face images
faces_directory = "faces/"

# Lists to store known face encodings and names
known_face_encodings = []
known_face_names = []

# Loop through all files in the faces directory
for filename in os.listdir(faces_directory):
    image_path = os.path.join(faces_directory, filename)
    image = face_recognition.load_image_file(image_path)

    # Generate face encodings for the image
    face_encoding = face_recognition.face_encodings(image)[0]

    # Extract the face name from the image filename
    face_name = os.path.splitext(filename)[0]
    
    # Append the face encoding and face name to the respective lists
    known_face_encodings.append(face_encoding)
    known_face_names.append(face_name.capitalize())

# Create a copy of known face names for tracking student attendance
students = known_face_names.copy()

# Initialize face locations and encodings
face_locations = []
face_encodings = []

# Get current date
now = datetime.now()
current_date = now.strftime("%d-%m-%y")

# Open a CSV file for writing attendance
f = open("Attendance/"+f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Set up font properties for displaying attendance on the frame
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 100)
fontScale = 1.5
fontColor = (255, 0, 0)
thickness = 3
lineType = 2

while True:
    # Read a frame from the video capture
    _, frame = video_capture.read()

    # Resize the frame to speed up face recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the frame from BGR (OpenCV) to RGB (face_recognition)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare face encodings with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Calculate face distance to find the best match
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        # Get the name of the best match
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # If the face belongs to a known person
        if name in known_face_names:
            # Display the name and attendance status on the frame
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                        lineType)

        # If the face belongs to a student, remove from the students list
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H:%M:%S")

            # Write the student's name and time to the attendance CSV file
            lnwriter.writerow([name, current_time])

    # Display the frame with attendance information
    cv2.imshow("Attendance", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture and destroy all windows
video_capture.release()
cv2.destroyAllWindows()

# Close the attendance CSV file
f.close()
