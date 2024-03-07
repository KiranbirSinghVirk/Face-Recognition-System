import face_recognition
import cv2
import os
import pickle

i=0
for i in range(0,1):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('faces\{name}.jpg'.format(name=input("enter your name")), frame)

    # Load the image
    image_path = "faces\{name}.jpg".format(name=input("enter your name"))  # Replace with the path to your image
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
    file_path = os.path.join(folder_path, "{name}.pkl".format(name=input("enter your name")))

    with open(file_path, 'wb') as output_file:
        pickle.dump(face_encodings_list, output_file)
        

    print(f"Face encodings saved to {file_path}")


    
    cv2.imshow("attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()


