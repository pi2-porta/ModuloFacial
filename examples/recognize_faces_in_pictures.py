import face_recognition
import numpy as     
import base64

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
anderson_image = face_recognition.load_image_file("a1.jpg")

unknown_image = face_recognition.load_image_file("anderson.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    anderson_face_encoding = face_recognition.face_encodings(anderson_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

# print('Type enconding: ')
# print(type(anderson_face_encoding))

# anderson_face_encoding = str(face_recognition)

# print('Type enconding: ')
# print(type(anderson_face_encoding))

# anderson_face_encoding = np.array(anderson_face_encoding)

# print('Type enconding: ')
# print(type(anderson_face_encoding))

# print('*', end='\n')

known_faces = [
    biden_face_encoding,
    obama_face_encoding,
    anderson_face_encoding
]



# for face in known_faces:
#     # print(face)
#     # print()
#     # for line in face:
#     #     print(line, end=', ')
    
#     print('Lista')
#     print(face.tolist())
#     print()

    

    # print('Lista')
    # print(face.array())
    # print()

    # aux = base64.b64encode(face)
    # print(aux)
    # print()
    # aux = base64.b64decode(aux)
    # print(aux)
    # print()

    # print('', end='\n')

print(unknown_face_encoding.tolist())


# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a picture of Anderson? {}".format(results[2]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

print()

a0 = anderson_face_encoding.tolist()
a1 = unknown_face_encoding.tolist()

# print(a0, end='\n\n\n')

# print(a1, end='\n\n\n')
