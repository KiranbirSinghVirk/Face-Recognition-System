#Importing libraries
import tkinter as tk               #for gui             
from PIL import Image, ImageTk      #for image
import face_recognition            #to recognize faces
import cv2                         #to use camera
import numpy as np                 #to handle data
import csv                         #to maintain attendence record
from datetime import datetime      #for date and time
import speech_recognition as sr    #for voice input
import pyttsx3                     #for voice output

# Function to handle attendance marking
def attendance():
    # Counter to track attendance announcements
    attendance_counter = 0
    
    # Video capturing
    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (0, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " is present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
                text = f"{name} is present"
                engine = pyttsx3.init()
                engine.setProperty('rate', 150)  # Adjust the speed of speech if needed
                engine.say(text)
                engine.runAndWait()
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])
                attendance_counter += 1  # Increment attendance counter
                if attendance_counter >= 3:  # Check if attendance has been marked 3 times
                    root.after(3000, root.destroy)  # Close the window after 3 seconds

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

# Function to handle speech recognition
def recognize_speech():
    speak_now_label.config(text="Speak now...")
    root.update()
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    if text == "mark attendance":
        attendance()
    else:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speed of speech if needed
        engine.say("Command is not recognized")
        engine.runAndWait()
        recognize_speech()

# GUI Setup
root = tk.Tk()
root.title("Attendance System")
root.attributes('-fullscreen', True)  # Full-screen mode

# Function to handle closing the window
def on_closing():
    if video_capture.isOpened():
        video_capture.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Set up background image
background_image = Image.open("background_image.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Label to display "Speak now..." message
speak_now_label = tk.Label(root, text="", font=("Arial", 24))
speak_now_label.pack(pady=20)

# Video capture setup
video_capture = cv2.VideoCapture(0)

# Load face encodings
karan_image = face_recognition.load_image_file("faces/karan1.jpg")
karan_encoding = face_recognition.face_encodings(karan_image)[0]
Lakshay_image = face_recognition.load_image_file("faces/lakshay.jpg")
Lakshay_encoding = face_recognition.face_encodings(Lakshay_image)[0]

known_face_encodings = [karan_encoding, Lakshay_encoding]
known_faces_names = ["karan", "lakshay"]
students = known_faces_names.copy()

# Date setup for CSV filename
now = datetime.now()
current_date = now.strftime("%y-%m-%d")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Start speech recognition immediately
recognize_speech()

# Start GUI
root.mainloop()
        



