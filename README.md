<p align="center">
  <img width="640" src="https://user-images.githubusercontent.com/122285115/211849833-8f007605-c9f8-4f60-9b95-5ad606920d61.jpg">
  <h4 align="center">A 100% spoofing-prevention rate for both 3D printed and resin facial masks, confirms FaceMe® as a leading facial recognition solution for preventing biometric fraud in remote applications, such as online banking, requiring identity verification before granting access to sensitive data or valuable assets.</h4>  
  <h4><a target="_blank" href="https://www.ibeta.com/wp-content/uploads/2022/03/220304-CyberLink-PAD-Level-2-Confirmation-Letter.pdf">FaceMe® iBeta Presentation Attack Detection Report</h4>
</p>

> **Note**
>
> SDK is fully on-premise, processing all happens on hosting server and no data leaves server.

## Project Structure
```graphql
# Code & components for pages
./FaceLivenessDetection-ServerSDK
  ├─ bin/linux_x86_64                 - # Core library files
  │  ├─ libfaceme_liveness1.so
  │  ├─ libfm_models.so
  │  └─ libimutils.so
  ├─ cpp                              - # C++ example
  │  ├─ CMakeLists.txt                - # CMake file for build example
  │  ├─ faceme_liveness.h             - # C++ header file to include library
  │  └─ main.cpp                      - # C++ example code
  ├─ flask                            - # Python flask API serving example
  │  ├─ app.py                        - # Flask example code
  │  └─ requirement.txt               - # Python requirement list
  ├─ model                            - # NN dictionary files for library
  │  ├─ data1.bin
  │  └─ data2.bin
  ├─ python                           - # Python example
  │  ├─ faceme_liveness.py            - # Python library Import Interface file
  │  ├─ main.py                       - # Python example code
  │  └─ requirements.txt              - # Python requirement list
  ├─ test_image                       - # Test Images
  │  ├─ genuine.jpg
  │  └─ spoof.png
  └─ Dockerfile                       - # Docker script for python flask API serving example
```

## Setup Project
#### - Linux
- Download repo and extract it
- Install system dependencies
```
sudo apt-get update -y
sudo apt-get install -y libcurl4-openssl-dev libssl-dev libopencv-dev
```
- Copy libraries into system folder
```
cp ./bin/linux_x86_64/libfm_models.so /usr/lib
cp ./bin/linux_x86_64/libimutils.so /usr/lib
```
#### - Windows
Contact us by Email support@faceme.tw
#### - Request license
Subscribe free trial at our [Subscription Page]()  
You will get email with trial license key ("XXXXX-XXXXX-XXXXX-XXXXX").
  
## C++ Example
- Replace license key in main.cpp https://github.com/FaceMe-SDK/FaceLivenessDetection-ServerSDK/blob/eaf9ce81dff32b329d66853461f5d8acb38c5568/cpp/main.cpp#L1-L7
- Build project
```
cd cpp
mkdir build && cd build
cmake ..
make
```
- Run project
```
./example_liveness --image ../../test_image/spoof.png --model ../../model
```

## Python Example
- Replace license key in main.py https://github.com/FaceMe-SDK/FaceLivenessDetection-ServerSDK/blob/eaf9ce81dff32b329d66853461f5d8acb38c5568/python/main.py#L11-L17
- Install dependencies
```
cd python
pip install -r requirement.txt
```
- Run project
```
python main.py
```
## Python Flask Example
- Replace license key in app.py https://github.com/FaceMe-SDK/FaceLivenessDetection-ServerSDK/blob/eaf9ce81dff32b329d66853461f5d8acb38c5568/flask/app.py#L19-L25
- Install dependencies
```
cd flask
pip install -r requirement.txt
```
- Run project
```
python app.py
```
<p align="center">
  <img width="480" src="https://user-images.githubusercontent.com/122285115/211873670-053fccc6-ffcf-443d-8d6d-6c3e2c161374.png">&emsp;&emsp;
  <img width="480" src="https://user-images.githubusercontent.com/122285115/211873784-0ba680ca-aad4-4535-bd6c-cefc328afdb3.png">
</p>


## Docker Flask Example
- Replace license key in app.py https://github.com/FaceMe-SDK/FaceLivenessDetection-ServerSDK/blob/eaf9ce81dff32b329d66853461f5d8acb38c5568/flask/app.py#L19-L25
- Build docker image
```
docker build --pull --rm -f "Dockerfile" -t facemeliveness:latest "."
```
- Run image
```
docker run facemeliveness
```
## - Request license
Subscribe free trial at our [Subscription Page]()
You will get email with trial license key ("XXXXX-XXXXX-XXXXX-XXXXX").
