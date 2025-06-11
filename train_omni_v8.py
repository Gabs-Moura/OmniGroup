from ultralytics import YOLO

# para marcar as imagens
# https://www.makesense.ai/

def main():
    # Load a model
    #model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="omni.yml", epochs=5)  # train the model
    metrics = model.val()

if __name__ == '__main__':
    main()