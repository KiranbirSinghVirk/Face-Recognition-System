import cv2
import face_recognition
import pickle
import numpy as np

known_faces_names=["kb"]
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
        results = face_recognition.compare_faces(saved_face_encodings, current_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
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
                text = f"{name} is present"
                # engine = pyttsx3.init()
                # engine.setProperty('rate', 150)  # Adjust the speed of speech if needed
                # engine.say(text)
                # engine.runAndWait()
                if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])
   
        # for i, result in enumerate(results):
        #     if result:
        #         print(f"Face {i+1} recognized!")

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
