import numpy as np
import cv2

confidenceThreshold = 0.5
NMSThreshold = 0.3

modelConfiguration = r'model/yolov3_custom.cfg'
modelWeights = r'model/yolov3_custom_last.weights'

labelsPath = r"model/classes.names"
labels = open(labelsPath).read().strip().split('\n')

np.random.seed(10)
COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

outputLayer = net.getLayerNames()
outputLayer = [outputLayer[i - 1] for i in net.getUnconnectedOutLayers()]


from googletrans import Translator

# Create Translator objects for Hindi and Kannada
translatorHI = Translator()
translatorKN = Translator()

import pyttsx3
engine = pyttsx3.init()

# Function to voice out the result text
def voice_out_result(result_text):
    engine.say(result_text)
    engine.runAndWait()



def webcam_pred():

    confidenceThreshold = 0.5
    NMSThreshold = 0.3

    modelConfiguration = r'model/yolov3_custom.cfg'
    modelWeights = r'model/yolov3_custom_last.weights'

    labelsPath = r"model/classes.names"
    labels = open(labelsPath).read().strip().split('\n')

    np.random.seed(10)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    outputLayer = net.getLayerNames()
    outputLayer = [outputLayer[i - 1] for i in net.getUnconnectedOutLayers()]

    video_capture = cv2.VideoCapture(0)

    (W, H) = (None, None)

    while True:
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 1)
        if W is None or H is None:
            (H,W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB = True, crop = False)
        net.setInput(blob)
        layersOutputs = net.forward(outputLayer)

        boxes = []
        confidences = []
        classIDs = []

        for output in layersOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > confidenceThreshold:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY,  width, height) = box.astype('int')
                    x = int(centerX - (width/2))
                    y = int(centerY - (height/2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        #Apply Non Maxima Suppression
        detectionNMS = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, NMSThreshold)
        if(len(detectionNMS) > 0):
            for i in detectionNMS.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                # text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
                text = labels[classIDs[i]]
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                hi = str(translatorHI.translate(text, src="en", dest="hi").text)
                kn = str(translatorKN.translate(text, src="en", dest="te").text)
                
                # Convert translated text to UTF-8 encoding
                
                # hi = hi.encode('utf-8').decode('utf-8')                
                # kn = kn.encode('utf-8').decode('utf-8')

                print(hi)
                print(kn)
                
                # Display translated texts on the right side of the frame
                cv2.putText(frame, hi, (x + w + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                cv2.putText(frame, kn, (x + w + 10, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                
                voice_out_result(text)  # Voice out the result text

        cv2.imshow('Output', frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    #Finally when video capture is over, release the video capture and destroyAllWindows
    video_capture.release()
    cv2.destroyAllWindows()



def image_pred(frame):


    (H,W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB = True, crop = False)
    net.setInput(blob)
    layersOutputs = net.forward(outputLayer)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY,  width, height) = box.astype('int')
                x = int(centerX - (width/2))
                y = int(centerY - (height/2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    #Apply Non Maxima Suppression
    detectionNMS = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, NMSThreshold)
    text = "No Gesture Found"
    if(len(detectionNMS) > 0):
        for i in detectionNMS.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = '{}:{:.2f}'.format(labels[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            text = labels[classIDs[i]]
            # text = 'Detected {} Gesture with {:.2f} %Accuracy'.format(labels[classIDs[i]], confidences[i])

    return frame, text

