from django.shortcuts import render
from structure.models import Employeess
# Create your views here.
import os
import cv2
import numpy as np
import datetime
from rest_framework.response import Response
from rest_framework import viewsets,status
from hrmanagement.settings import BASE_DIR
from rest_framework.decorators import api_view
from .models import Attendence
from .serializer import attendence
# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return Response({"message": "Got some data!", "data": request.data,"status":status.HTTP_200_OK})


def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        cam = cv2.VideoCapture(0)
        success, frame = cam.read()  # read the camera frame
        if  frame is not None:
            return cv2.VideoCapture(0),cv2.waitKey(250)
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@api_view(['POST'])
def video_feed(request):
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames())

@api_view(['POST'])
def create_dataset(request):
    #print request.POST
    employee_id = request.data['employee_id']
    snippet = Employeess.objects.filter(employee_id=employee_id)
    if snippet.exists():
        snippet = Employeess.objects.get(employee_id=employee_id)
        if  snippet.sample_taken==False:
            # print (cv2.__version__)
            ret, frame = cv2.VideoCapture(0).read()
            cam = cv2.VideoCapture(0)
            faceDetect = cv2.CascadeClassifier('f:/django/test/ml/haarcascade_frontalface_default.xml')
            # cap = cv2.VideoCapture(1)

            # Our identifier
            # We will put the id here and we will store the id with a face, so that later we can identify whose face it is
            id = snippet.id
            # Our dataset naming counter
            sampleNum = 0
            # Capturing the faces one by one and detect the faces and showing it on the window
            while(True):
                # Capturing the image
                # cam.read will return the status variable and the captured colored image
                ret, img = cam.read()
                # the returned img is a colored image but for the classifier to work we need a greyscale image
                # to convert
                if img is not None:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                else:
                    return Response({"message": "Please turn of camera ", "status": status.HTTP_400_BAD_REQUEST})
                # To store the faces
                # This will detect all the images in the current frame, and it will return the coordinates of the faces
                # Takes in image and some other parameter for accurate result
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                # In above 'faces' variable there can be multiple faces so we have to get each and every face and draw a rectangle around it.
                for (x, y, w, h) in faces:
                    # Whenever the program captures the face, we will write that is a folder
                    # Before capturing the face, we need to tell the script whose face it is
                    # For that we will need an identifier, here we call it id
                    # So now we captured a face, we need to write it in a file
                    sampleNum = sampleNum + 1
                    # Saving the image dataset, but only the face part, cropping the rest
                    cv2.imwrite('f:/django/test/ml/dataset/user.' + str(id) + '.' + str(sampleNum) + '.jpg',gray[y:y + h, x:x + w])
                    # @params the initial point of the rectangle will be x,y and
                    # @params end point will be x+width and y+height
                    # @params along with color of the rectangle
                    # @params thickness of the rectangle
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Before continuing to the next loop, I want to give it a little pause
                    # waitKey of 100 millisecond
                    cv2.waitKey(250)

                #Showing the image in another window
                #Creates a window with window name "Face" and with the image img
                cv2.imshow("Face",img)
                #Before closing it we need to give a wait command, otherwise the open cv wont work
                # @params with the millisecond of delay 1
                cv2.waitKey(1)
                #To get out of the loop
                if(sampleNum>35):
                    break
            #releasing the cam
            cam.release()
            # destroying all the windows
            cv2.destroyAllWindows()
            snippet.sample_taken=True
            snippet.save()
            return Response({"message": "Suucessfully Video Recorded ", "status": status.HTTP_200_OK})
        else:
            return Response({"message": "Video Recorded already", "status": status.HTTP_400_BAD_REQUEST})
    else:
        return Response({"message": "Invalid Employee Id","status": status.HTTP_400_BAD_REQUEST})
@api_view(['POST'])
def trainer(request):
    '''
        In trainer.py we have to get all the samples from the dataset folder,
        for the trainer to recognize which id number is for which face.

        for that we need to extract all the relative path
        i.e. dataset/user.1.1.jpg, dataset/user.1.2.jpg, dataset/user.1.3.jpg
        for this python has a library called os
    '''
    import os
    from PIL import Image

    #Creating a recognizer to train
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #Path of the samples
    path = 'f:/django/test/ml/dataset'

    # To get all the images, we need corresponing id
    def getImagesWithID(path):
        # create a list for the path for all the images that is available in the folder
        # from the path(dataset folder) this is listing all the directories and it is fetching the directories from each and every pictures
        # And putting them in 'f' and join method is appending the f(file name) to the path with the '/'
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] #concatinate the path with the image name
        #print imagePaths

        # Now, we loop all the images and store that userid and the face with different image list
        faces = []
        Ids = []
        for imagePath in imagePaths:
            # First we have to open the image then we have to convert it into numpy array
            faceImg = Image.open(imagePath).convert('L') #convert it to grayscale
            # converting the PIL image to numpy array
            # @params takes image and convertion format
            faceNp = np.array(faceImg, 'uint8')
            # Now we need to get the user id, which we can get from the name of the picture
            # for this we have to slit the path() i.e dataset/user.1.7.jpg with path splitter and then get the second part only i.e. user.1.7.jpg
            # Then we split the second part with . splitter
            # Initially in string format so hance have to convert into int format
            ID = int(os.path.split(imagePath)[-1].split('.')[1]) # -1 so that it will count from backwards and slipt the second index of the '.' Hence id
            # Images
            faces.append(faceNp)
            # Label
            Ids.append(ID)
            #print ID
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(Ids), np.array(faces)

    # Fetching ids and faces
    ids, faces = getImagesWithID(path)

    #Training the recognizer
    # For that we need face samples and corresponding labels
    recognizer.train(faces, ids)

    # Save the recogzier state so that we can access it later
    recognizer.save('f:/django/test/ml/recognizer/trainingData.yml')
    cv2.destroyAllWindows()

    return Response({"message": "Training Done", "status": status.HTTP_200_OK})

@api_view(['POST'])
def detect(request):
    faceDetect = cv2.CascadeClassifier('f:/django/test//ml/haarcascade_frontalface_default.xml')

    # cam = cv2.VideoCapture(0)
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # creating recognizer
    rec = cv2.face.LBPHFaceRecognizer_create();
    # loading the training data
    rec.read('f:/django/test//ml/recognizer/trainingData.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

            getId,conf = rec.predict(gray[y:y+h, x:x+w]) #This will predict the id of the face

            #print conf;
            if conf<35:
                userId = getId
                cv2.putText(img, "Detected",(x,y+h), font, 2, (0,255,0),2)
            else:
                cv2.putText(img, "Unknown",(x,y+h), font, 2, (0,0,255),2)

            # Printing that number below the face
            # @Prams cam image, id, location,font style, color, stroke

        cv2.imshow("Face",img)
        if(cv2.waitKey(1) == ord('q')):
            break
        elif(userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            print(userId)
            snippet = Employeess.objects.get(id=userId)
            if snippet.status=="ACTIVE":
                try:
                    attendence = Attendence.objects.get(employee_id=snippet, date=datetime.date.today())
                    if attendence.out_time_recorded==False:
                        attendence.out_time_recorded=True
                        attendence.save()
                        return Response(
                            {"message": "Out Time recorded successfully " + snippet.firstname + ' ' + snippet.lastname,
                             "status": status.HTTP_200_OK})
                    else:
                        return Response({"message": "Already Taken Out time", "status": status.HTTP_400_BAD_REQUEST})
                except:
                    attendence = Attendence.objects.create(employee_id=snippet)
                    return Response(
                        {"message": "In Time recorded successfully " + snippet.firstname + ' ' + snippet.lastname,
                         "status": status.HTTP_200_OK})
            else:
                return Response({"message": snippet.firstname + ' ' + snippet.lastname+",Your Attendence is not recorded cause ,you are "+snippet.status, "status": status.HTTP_400_BAD_REQUEST})




    cam.release()
    cv2.destroyAllWindows()
    return Response({"message": "Invalid Employee Id", "status": status.HTTP_400_BAD_REQUEST})

@api_view(['POST'])
def employee_attendence_summery(request):
    if 'ID' in request.data:
        try:
            userId=request.data["ID"]
            start_date = request.data["start_date"]
            end_date = request.data["end_date"]

            snippet=Employeess.objects.filter(employee_id=userId)
            if snippet.exists:
                snip=Employeess.objects.get(employee_id=userId)
                snippet2=Attendence.objects.filter(employee_id=snip,date__range=[start_date, end_date])
                serializer = attendence(snippet2, many=True)

            return Response(
                {"message": serializer.data, "status": status.HTTP_200_OK, "action": 'Attendence Found'})
        except:
            return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})
    else:
        try:
            start_date = request.data["start_date"]
            end_date = request.data["end_date"]

            snippet = Employeess.objects.filter(pk=request.data["pk"])
            if snippet.exists:
                snip = Employeess.objects.get(pk=request.data["pk"])
                snippet2 = Attendence.objects.filter(employee_id=snip, date__range=[start_date, end_date])
                serializer = attendence(snippet2, many=True)

            return Response(
                {"message": serializer.data, "status": status.HTTP_200_OK, "action": 'Attendence Found'})
        except:
            return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})

