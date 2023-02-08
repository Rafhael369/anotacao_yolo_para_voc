import os
import csv
import numpy as np

text_files = []
PASTA_ENTRADA = "yolo/"
PASTA_SAIDA = "voc/"

for filename in os.listdir(PASTA_ENTRADA):
    if filename.endswith(".txt"):
        text_files.append(filename)

for txt in text_files:
    voc_annotations = []
    with open(PASTA_ENTRADA+txt, 'r') as f:
        annotations = f.readlines()

    for annotation in annotations:
        classid, x, y, w, h = annotation.strip().split()
        classid = int(classid)
        x = float(x)
        y = float(y)
        w = float(w)
        h = float(h)
        xmin = int((x - w / 2) * 1280)
        ymin = int((y - h / 2) * 720)
        xmax = int((x + w / 2) * 1280)
        ymax = int((y + h / 2) * 720)

        voc_annotations.append((xmin, ymin, xmax, ymax, classid))

    with open(PASTA_SAIDA+txt, "w") as file:
        file.write(str(len(voc_annotations)) + "\n")
        for line in voc_annotations:
            file.write(str(line).replace("(", "").replace(")", "").replace(", ", " ") + "\n")
