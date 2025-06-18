from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(data="omni.yml", epochs=5)  #definir quantas epochs vai ter de treino, quanto mais melhor
    metrics = model.val()

if __name__ == '__main__':
    main()