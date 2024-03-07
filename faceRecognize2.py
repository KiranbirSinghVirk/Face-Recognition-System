#import modules
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
from gtts import gTTS
import playsound
import speech_recognition as sr
import pyttsx3
import pickle
import os

def loadImage():
    i=0
    for i in range(0,1):
        name
        =input("enter your name")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite('faces\{name1}.jpg'.format(name1=name
        ), frame)
        known_faces_names.append(name
        )
        students.append(name
        )
        # Load the image
        image_path = "faces\{name1}.jpg".format(name1=name
        )  # Replace with the path to your image
        image = face_recognition.load_image_file(image_path) 
        # Find face locations and encodings in the image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        # Specify the path to the folder on the F drive to save the encoding
        folder_path = "F:\detdes\encodings"  # Replace with the desired output folder path

        # Check if faces are found
        if len(face_encodings) > 0:
        # Create a list to store face encodings
            face_encodings_list = []

        # Append the face encodings to the list
            for encoding in face_encodings:
                face_encodings_list.append(encoding.tolist())

        # Save face encodings to a file
        file_path = os.path.join(folder_path, "{name1}.pkl".format(name1=name
        ))

        with open(file_path, 'wb') as output_file:
            pickle.dump(face_encodings_list, output_file)
            
        
        print(f"Face encodings saved to {file_path}")


        
        cv2.imshow("attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
    cap.release()
    cv2.destroyAllWindows()


def attendance():
# Load the saved face encoding
    with open("F:\detdes\encodings\kb.pkl", "rb") as file:
        saved_face_encodings = pickle.load(file)

    # Initialize the webcam (assuming it's the first camera, you can change the index accordingly)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a single frame
        ret, frame = cap.read()

        # Find face locations in the current frame
        current_face_locations = face_recognition.face_locations(frame)

        # Encode face(s) in the current frame
        current_face_encodings = face_recognition.face_encodings(frame, current_face_locations)

        # Compare with the saved encoding
        for current_encoding in current_face_encodings:
            matches = face_recognition.compare_faces(saved_face_encodings, current_encoding)
            face_distance = face_recognition.face_distance(saved_face_encodings, current_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " is present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])
        # Display the frame
        cv2.imshow('Face Recognition', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

#load images
# karan_image = face_recognition.load_image_file("faces/karan1.jpg")
# karan_encoding = face_recognition.face_encodings(karan_image)[0]
# Lakshay_image = face_recognition.load_image_file("faces/lakshay.jpg")
# Lakshay_encoding = face_recognition.face_encodings(Lakshay_image)[0]

# known_face_encodings = [karan_encoding]
known_faces_names = ["kb", "lakshay"]
students = known_faces_names.copy()
face_locations = []
face_encodings = []
#when attendance is marked(date)
now = datetime.now()
current_date = now.strftime("%y-%m-%d")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)
loadImage()
attendance()


# r = sr.Recognizer()
# print("speak...")
# with sr.Microphone() as source:
#     audio = r.listen(source)
# text = r.recognize_google(audio)
# if(text=="mark attendance"):
#     attendance()
# # if(text=="register me"):
# #     loadImage()