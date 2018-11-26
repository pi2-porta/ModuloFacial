import face_recognition
import cv2
import requests
import base64
import numpy as np
import threading
import find_target

face_locations = None
frame = None

def capture():
    global face_locations
    global frame
    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        # Find all the faces and face enqcodings in the frame of video
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def recognition():
    global face_locations

    while True:
        if(face_locations):
            macs = []
            results = []
            for (top, right, bottom, left) in face_locations:

                face = frame[top:bottom+1, left:right+1]
                _, img_encoded = cv2.imencode('.jpg', face)
                jpg_as_text = base64.b64encode(img_encoded)
                payload = {'photo': jpg_as_text}
                r = requests.post('http://127.0.0.1:8000/search/', data=payload)
                macs.append(r.text[1:-1])

            for mac in macs:
                t = threading.Thread(target=find_target.find_target, args=(mac,results,))
                t.start()
                t.join()

            print(results)
            if results.count(True) > 0:
                print('abrir porta') #ALTERAR PARA REQUISICAO


        # # Loop through each face in this frame of video
        # for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #     # See if the face is a match for the known face(s)
        #     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        #
        #     name = "Unknown"
        #
        #     # If a match was found in known_face_encodings, just use the first one.
        #     if True in matches:
        #         first_match_index = matches.index(True)
        #         name = known_face_names[first_match_index]
        #
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        # # Display the resulting image
        # # cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!


if __name__ == "__main__":
    c = threading.Thread(target=capture, args=())
    r = threading.Thread(target=recognition, args=())
    c.start()
    r.start()
