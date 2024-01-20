from imageai.Classification import ImageClassification
from imageai.Detection import VideoObjectDetection
import os
import cv2

cwd = os.getcwd()
assets = os.path.join(cwd, "assets\\")

"""
Clasificación de objectos con MobileNet V2
"""
def clasificacion():
    dotpth = os.path.join(cwd, "mobilenet_v2-b0353104.pth")
    img = os.path.join(assets, "img1.jpg")

    pred = ImageClassification()
    pred.setModelTypeAsMobileNetV2()
    pred.setModelPath(dotpth)
    pred.loadModel()

    predic, prob = pred.classifyImage(img, result_count=2)

    print("\nResultados de clasificacion:")
    print(f"\tPredicciones: {predic}\nProbabilidades: {prob}")

"""
Detección de objectos con RetinaNet
"""

# Analisis de cada frame
def funcionPorFrame(n_frame, output, c_output):
    print(f"\nInfo del frame #{n_frame}:")
    print(f"\t- Info de cada objeto: {output}")
    print(f"\t- Cuenta de objetos detectados: {c_output}")

# Deteccion de objetos en vivo
def deteccionEnVivo():
    detec = VideoObjectDetection() # detector
    detec.setModelTypeAsRetinaNet()
    detec.setModelPath(os.path.join(cwd, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
    detec.loadModel()
    try:
        camara = cv2.VideoCapture(0)
        detec.detectObjectsFromVideo(camera_input=camara,
                                    save_detected_video=False,
                                    per_frame_function=funcionPorFrame,
                                    frames_per_second=60)
    finally:
        camara.release()
    print("\n[+] Deteccion en progreso...")

def main():
    clasificacion()
    deteccionEnVivo()

if __name__ == "__main__":
    main()