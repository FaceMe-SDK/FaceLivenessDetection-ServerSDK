import sys
sys.path.append('.')

import cv2
import numpy as np
import os
import base64

from faceme_liveness import fml_version
from faceme_liveness import fml_init
from faceme_liveness import fml_detect_face


licenseKey = "XXXXX-XXXXX-XXXXX-XXXXX"      # Please request license to support@faceme.tw
modelFolder = os.path.abspath(os.path.dirname(__file__)) + '/../model'

if __name__ == '__main__':

    version = fml_version()
    print("version: ", version.decode('utf-8'))

    ret = fml_init(modelFolder.encode('utf-8'), licenseKey.encode('utf-8'))
    if ret != 0:
        print(f"init failed: {ret}")
        exit(-1)

    imagePath = os.path.abspath(os.path.dirname(__file__)) + '/../test_image/spoof.png'
    image = cv2.imread(imagePath)
    if image is None:
        print("image is null!")
        exit(-1)
        
    faceRect = np.zeros([4], dtype=np.int32)
    livenessScore = np.zeros([1], dtype=np.double)
    ret = fml_detect_face(image, image.shape[1], image.shape[0], faceRect, livenessScore)
    if ret == -1:
        print("license error!")
    elif ret == -2:
        print("init error!")
    elif ret == 0:
        print("no face detected!");
    elif ret > 1:
        print("multiple face detected!");
    elif livenessScore[0] > 0.5:
        print(f"genuine -> face rect: {faceRect[0]}, {faceRect[1]}, {faceRect[2]}, {faceRect[3]}, liveness score: {livenessScore[0]}")
    else:
        print(f"spoof -> face rect: {faceRect[0]}, {faceRect[1]}, {faceRect[2]}, {faceRect[3]}, liveness score: {livenessScore[0]}")

    exit(0)