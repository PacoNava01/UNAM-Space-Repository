'''
Script de seguimiento de marcadores ArUco con la ayuda de servomotores
El programa buscara seguir el centro del marcador Aruco indicado
'''
from Open_cam import *
import json
import cv2
import numpy as np
import cv2.aruco as aruco
from collections import deque
import json
import os
from dataclasses import dataclass
from ArUco import *
from Hardware import PID_camera

# ============================================================
# CONFIGURACIÓN
config_path = r"Francisco\Camara\Cam_config.json"
with open(config_path, "r") as f:
    config = json.load(f)

CAMERA_INDEX = config["CAMERA_INDEX"]
FRAME_WIDTH = config["FRAME_WIDTH"]
FRAME_HEIGHT = config["FRAME_HEIGHT"]
FRAME_FPS = config["FRAME_FPS"]
BUFFER_SECONDS = config["BUFFER_SECONDS"]

MARKER_LENGTH = 0.10  # metros

# IMPORTANTE:
# Estos valores son SOLO de ejemplo.
# Lo correcto es obtenerlos mediante calibración.
CAMERA_MATRIX = np.array([
    [800.0,   0.0, 640.0],
    [  0.0, 800.0, 480.0],
    [  0.0,   0.0,   1.0]
], dtype=np.float64)

DIST_COEFFS = np.zeros((5, 1), dtype=np.float64)
# ============================================================

# ============================================================
# Inicializamos los servos

# ============================================================

if __name__ == "__main__":

