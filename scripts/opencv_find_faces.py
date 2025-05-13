import cv2
import numpy as np

# Load YuNet model from OpenCV Zoo
model_path = project.folder + "/modules/opencv/face_detection_yunet_2023mar.onnx"
face_detector = cv2.FaceDetectorYN.create(
    model_path,
    "",
    (320, 320),
    score_threshold=0.5,
    nms_threshold=0.3,
    top_k=5000
)

# Get image from TouchDesigner
img = op('null_to_opencv').numpyArray(delayed=False)
img_uint8 = (img * 255).astype(np.uint8)
bgr = cv2.cvtColor(img_uint8, cv2.COLOR_RGBA2BGR)

# Resize to match model input
(h, w) = bgr.shape[:2]
face_detector.setInputSize((w, h))

# Detect
_, faces = face_detector.detect(bgr)

# Output results
out = op('faces_out')
out.clear()
out.appendRow(['Face', 'X', 'Y', 'Width', 'Height', 'Confidence'])

if faces is not None:
    for i, face in enumerate(faces):
        x, y, w_box, h_box, score, *landmarks = face.flatten()
        out.appendRow([
            f'Face {i}',
            str(int(x)), str(int(y)),
            str(int(w_box)), str(int(h_box)),
            f'{score:.2f}'
        ])
