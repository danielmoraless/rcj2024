from ultralytics import YOLO
import cv2

"""
Este test simplemente implementa tracking del modelo yolov8n.pt
y muestra los resultados en una ventana.
"""

def main():
    modelo = YOLO("yolov8n.pt")

    try:
        camara = cv2.VideoCapture(0)

        while camara.isOpened():
            ret, frame = camara.read()

            if not ret:
                break
            else:
                resultados = modelo.track(frame, persist=True)

                cv2.imshow("TRACKEANDO", resultados[0].plot())

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        camara.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()