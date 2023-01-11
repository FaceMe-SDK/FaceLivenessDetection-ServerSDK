import ctypes, ctypes.util
from ctypes import *
from numpy.ctypeslib import ndpointer
import sys
import os

lib_path = os.path.abspath(os.path.dirname(__file__)) + '/../bin/linux_x86_64/libfaceme_liveness1.so'
liveness_engine = cdll.LoadLibrary(lib_path)

fml_version = liveness_engine.fml_version
fml_version.argtypes = []
fml_version.restype = ctypes.c_char_p

fml_init = liveness_engine.fml_init
fml_init.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
fml_init.restype = ctypes.c_int32

fml_detect_face = liveness_engine.fml_detect_face
fml_detect_face.argtypes = [ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'), ctypes.c_int32, ctypes.c_int32, ndpointer(ctypes.c_int32, flags='C_CONTIGUOUS'), ndpointer(ctypes.c_double, flags='C_CONTIGUOUS')]
fml_detect_face.restype = ctypes.c_int32

