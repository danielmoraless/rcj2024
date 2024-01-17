from imageai.Classification import ImageClassification
import os

def main():
    cwd = os.getcwd()
    dotpth = os.path.join(cwd, "mobilenet_v2-b0353104.pth")
    assets = os.path.join(cwd, "assets\\")
    img = os.path.join(assets, "img1.jpg")

    pred = ImageClassification()
    pred.setModelTypeAsMobileNetV2()
    pred.setModelPath(dotpth)
    pred.loadModel()

    predic, prob = pred.classifyImage(img, result_count=2)

    print(f"Predicciones: {predic}\nProbabilidades: {prob}")

if __name__ == "__main__":
    main()