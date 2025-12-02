from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import sys
from PyQt5.QtWidgets import *


# 2. ViT feature extractor + model
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")



class Vit(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('열기')
        self.setGeometry(200, 200, 700, 500)

        fileButton = QPushButton('파일', self)
        probButton = QPushButton('추론', self)
        quitButton = QPushButton('나가기', self)

        fileButton.setGeometry(100, 100, 100, 100)
        probButton.setGeometry(300, 100, 100, 100)
        quitButton.setGeometry(500, 100, 100, 100)

        fileButton.clicked.connect(self.fileOpenFunction)
        probButton.clicked.connect(self.probFunction)
        quitButton.clicked.connect(self.quitFunction)


    def fileOpenFunction(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file >', './')
        self.img = cv.imread(fname[0])
        if self.img is None: sys.exit('파일을 찾을 수 없습니다.')

        self.img_show = np.copy(self.img)
        cv.imshow('Painting', self.img_show)


    def probFunction(self):
        img_rgb = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        # 3. 이미지 전처리 
        inputs = processor(images=pil_img, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probs = logits.softmax(dim= -1)
            

        img = np.copy(self.img)
        pred_idx = int(torch.argmax(probs[0]))
        pred_label = model.config.id2label[pred_idx]
        pred_prob = float(probs[0][pred_idx] * 100)
        cv.putText(img, f"Predict: {pred_label}", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv.putText(img, f"Prob: {pred_prob:.2f}%", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)         
        cv.imshow('Painting', img)
        print("번째 이미지 예측: ")
        print(f"  클래스: {pred_label}")
        print(f"  확률: {pred_prob:.2f}\n")

    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()
    
app = QApplication(sys.argv)
win = Vit()
win.show()
app.exec_()


