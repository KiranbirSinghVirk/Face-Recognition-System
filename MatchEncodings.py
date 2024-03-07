import os
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
video_capture = cv2.VideoCapture(0)
now = datetime.now()
current_date = now.strftime("%y-%m-%d")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Specify the path to the folder on the F drive
folder_path = "F:\detdes\encodings"

# List all files in the folder
# files = os.listdir(folder_path)
name = input("enter your name")
# # Provide the name of the file you want to match data with
file_name = "{fname}.pkl".format(fname=name)

# # Check if the file exists in the folder
# if file_name in files:
    # Construct the full path to the file
file_path = "F:\detdes\encodings\{fname}.pkl".format(fname=name)

    # Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()
face_locations = []
face_encodings = []
    # Get user input
def attendance():
    #video capturing
    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces('F:\detdes\encodings\{fname}.pkl'.format(fname=name), face_encoding)
            face_distance = face_recognition.face_distance('F:\detdes\encodings\{fname}.pkl'.format(fname=name), face_encoding)
            best_match_index = np.argmin(face_distance)
            if(matches[best_match_index]):
                print("matched")
            #     name = known_faces_names[best_match_index]
            # if name in known_faces_names:
            #     font = cv2.FONT_HERSHEY_SIMPLEX
            #     bottomLeftCornerOfText = (10, 100)
            #     fontScale = 1.5
            #     fontColor = (255, 0, 0)
            #     thickness = 3
            #     lineType = 2
            #     cv2.putText(frame, name + " is present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
            #     # tts = gTTS(text="{student} is present".format(student=name), lang='en')
            #     # tts.save("hello.mp3")
            #     # playsound.playsound("hello.mp3")
            #     if name in students:
            #         students.remove(name)
            #         current_time = now.strftime("%H-%M-%S")
            #         lnwriter.writerow([name, current_time])

        cv2.imshow("attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()    
#user_input = input("Enter your input: ")

    # Match the user input with the file content
# if user_input in file_content:
#     print("Input matches data in the file.")
# else:
#     print("Input does not match data in the file.")
# # else:
# #     print(f"The file {file_name} does not exist in the folder.")
attendance()
