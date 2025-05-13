import cv2
import numpy as np

# Load DNN model
modelFile = project.folder + '/modules/opencv/res10_300x300_ssd_iter_140000.caffemodel'
configFile = project.folder + '/modules/opencv/deploy.prototxt'
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# Grab image from TOP

OP_PATH = 'null_to_opencv'

top = op(OP_PATH)
img = top.numpyArray(delayed=False)
img_uint8 = (img * 255).astype(np.uint8)
bgr = cv2.cvtColor(img_uint8, cv2.COLOR_RGBA2BGR)
(h, w) = bgr.shape[:2]

# Preprocess
blob = cv2.dnn.blobFromImage(bgr, 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)
net.setInput(blob)
detections = net.forward()

# Output to DAT
out = op('faces_out')
out.clear()
out.appendRow(['Face', 'X', 'Y', 'Width', 'Height', 'Confidence'])

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (x1, y1, x2, y2) = box.astype('int')
        out.appendRow([
            f'Face {i}', str(x1), str(y1),
            str(x2 - x1), str(y2 - y1),
            f'{confidence:.2f}'
        ])