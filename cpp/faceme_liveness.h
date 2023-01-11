#pragma once

#ifdef __cplusplus
extern "C" {
#endif

/*
Get SDK version
*/
const char* fml_version();

/*
Init SDK
    ret == 0 -> successful, ret < 0 -> model error, ret > 0 -> license error
*/
int fml_init(const char* dictPath, char* licenseKey);

/*
Get Face Detection, Liveness Check result
Check main.cpp for usage
    ret < 0 -> init error
    ret >= 0 -> detected face count
*/
int fml_detect_face(unsigned char* bgrData, int width, int height, int* faceRect, double* livenessScore);

#ifdef __cplusplus
}
#endif