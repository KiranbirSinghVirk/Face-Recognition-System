import cv2
import numpy as np
# # Capture the image from the webcam
images=[]
encodingOfImages=[]
i=0
for i in range(0,1):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('faces\{name}.jpg'.format(name=input("enter your name")), frame)
    encoding= cv2.imencode('.jpg', frame)[0]
    folder_path = 'F:\detdes\encodings'

    #encoding_path = 'F:\detdes\encodings.npy'
    encoding_filename = 'encoding.npy'
    encoding_path = 'F:\detdes\encodings' + encoding_filename
    np.save(encoding_path, encoding)
    # Save the image
    cv2.imshow("attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

# # Encode the image
# encodingImage = encoded_image = cv2.imencode('.jpg', frame)[1]
# encodingOfImages.append(encodingImage)
# Print the encoded image
print("done")
print(images)