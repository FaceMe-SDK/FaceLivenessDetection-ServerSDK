import sys
sys.path.append('.')
sys.path.append('../python')

from flask import Flask, request, jsonify
from time import gmtime, strftime
import os
import base64
import json
import cv2
import numpy as np

from faceme_liveness import fml_version
from faceme_liveness import fml_init
from faceme_liveness import fml_detect_face

app = Flask(__name__) 

app.config['SITE'] = "http://0.0.0.0:8888/"
app.config['DEBUG'] = False

licenseKey = "XXXXX-XXXXX-XXXXX-XXXXX"		# Please request license to support@faceme.tw
modelFolder = os.path.abspath(os.path.dirname(__file__)) + '/../model'

version = fml_version()
print("version: ", version.decode('utf-8'))

ret = fml_init(modelFolder.encode('utf-8'), licenseKey.encode('utf-8'))
if ret != 0:
    print(f"init failed: {ret}");
    exit(-1)

@app.route('/check_liveness', methods=['POST'])
def check_liveness():
  file = request.files['image']
  image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
  
  faceRect = np.zeros([4], dtype=np.int32)
  livenessScore = np.zeros([1], dtype=np.double)
  ret = fml_detect_face(image, image.shape[1], image.shape[0], faceRect, livenessScore)
  if ret == -1:
      result = "license error!"
  elif ret == -2:
      result = "init error!"
  elif ret == 0:
      result = "no face detected!"
  elif ret > 1:
      result = "multiple face detected!"
  elif livenessScore[0] > 0.5:
      result = "genuine"
  else:
      result = "spoof"
  
  status = "ok"
  response = jsonify({"status": status, "data": {"result": result, "face_rect": {"x": int(faceRect[0]), "y": int(faceRect[1]), "w": int(faceRect[2] - faceRect[0] + 1), "h" : int(faceRect[3] - faceRect[1] + 1)}, "liveness_score": livenessScore[0]}})

  response.status_code = 200
  response.headers["Content-Type"] = "application/json; charset=utf-8"
  return response

@app.route('/check_liveness_base64', methods=['POST'])
def check_liveness_base64():
  content = request.get_json()
  imageBase64 = content['image']
  image = cv2.imdecode(np.frombuffer(base64.b64decode(imageBase64), dtype=np.uint8), cv2.IMREAD_COLOR)

  faceRect = np.zeros([4], dtype=np.int32)
  livenessScore = np.zeros([1], dtype=np.double)
  ret = fml_detect_face(image, image.shape[1], image.shape[0], faceRect, livenessScore)
  if ret == -1:
      result = "license error!"
  elif ret == -2:
      result = "init error!"
  elif ret == 0:
      result = "no face detected!"
  elif ret > 1:
      result = "multiple face detected!"
  elif livenessScore[0] > 0.5:
      result = "genuine"
  else:
      result = "spoof"
  
  status = "ok"
  response = jsonify({"status": status, "data": {"result": result, "face_rect": {"x": int(faceRect[0]), "y": int(faceRect[1]), "w": int(faceRect[2] - faceRect[0] + 1), "h" : int(faceRect[3] - faceRect[1] + 1)}, "liveness_score": livenessScore[0]}})

  response.status_code = 200
  response.headers["Content-Type"] = "application/json; charset=utf-8"
  return response


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)