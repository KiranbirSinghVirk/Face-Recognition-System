import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
from gtts import gTTS
import playsound
import speech_recognition as sr


class FaceRecognitionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")

        # Create and set up the main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        # Create buttons
        self.start_button = tk.Button(self.main_frame, text="Start Attendance", command=self.start_attendance)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def start_attendance(self):
        messagebox.showinfo("Information", "Attendance started!")

        # Call your attendance function here
        attendance()

    def quit_app(self):
        self.root.destroy()

def attendance():
    #video capturing
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
            if(matches[best_match_index]):
                name = known_faces_names[best_match_index]
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " is present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
                tts = gTTS(text="{student} is present".format(student=name), lang='en')
                tts.save("hello.mp3")
                playsound.playsound("hello.mp3")
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

        cv2.imshow("attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()        

def main():
    # Set up your video_capture, known_face_encodings, known_faces_names, students, face_locations, face_encodings
    # ...
    video_capture= cv2.VideoCapture(0)

#load images
    karan_image = face_recognition.load_image_file("faces/karan1.jpg")
    karan_encoding = face_recognition.face_encodings(karan_image)[0]

    known_face_encodings = [karan_encoding]
    known_faces_names = ["karan"]
    students = known_faces_names.copy()
    face_locations = []
    face_encodings = []
    #when attendance is marked(date)
    now = datetime.now()
    current_date = now.strftime("%y-%m-%d")
    f = open(f"{current_date}.csv", "w+", newline="")
    lnwriter = csv.writer(f)



    r = sr.Recognizer()
    print("speak...")
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    if(text=="mark attendance"):
        attendance()
    # Initialize the Tkinter GUI
    root = tk.Tk()
    app = FaceRecognitionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
