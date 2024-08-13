import torch
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import torchvision
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
import os
import random
import string


def load_model(model_path, num_classes):
    model = get_model(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def get_model(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model

def transform_image(image):
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    return transform(image).unsqueeze(0)

def predict(model, image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
    return outputs





def generate_random_filename(folder="Detection_Results", length=10):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    characters = string.ascii_letters + string.digits
    random_filename = ''.join(random.choice(characters) for i in range(length))
    return os.path.join(folder, f"resultant_image_{random_filename}.jpg")

def display_image_with_boxes(image, boxes, labels, scores, score_threshold=0.5):
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    
    ax = plt.gca()
    print("inside func")

    for box, label, score in zip(boxes, labels, scores):
        if score >= score_threshold:
            xmin, ymin, xmax, ymax = box
            width, height = xmax - xmin, ymax - ymin
            edgecolor = 'r' if label == 1 else 'g'
            rect = patches.Rectangle((xmin, ymin), width, height, linewidth=1, edgecolor=edgecolor, facecolor='none')
            ax.add_patch(rect)
            plt.text(xmin, ymin,'defected', fontdict={'fontsize': 10})

    print("for loop finished")
    plt.axis('off')
    # plt.savefig('filename.svg')

    random_filename = generate_random_filename()
    plt.savefig(random_filename)
    plt.show()


    #adding new line
    return random_filename




def show_predict_page():
    st.title("Faster R-CNN Image Prediction")

    model_path = 'D:/Dashboard/rcnn_model2.pth'   #change the path accordingly with the path of the model
    num_classes = 3
    model = load_model(model_path, num_classes)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="Prediction")
    if uploaded_file is not None:
        print("uploaded")
        image = Image.open(uploaded_file).convert("RGB")
        image_tensor = transform_image(image)

        print("starting preds")
        outputs = predict(model, image_tensor)

        print("preds finished")
        boxes = outputs[0]['boxes'].cpu().numpy()
        labels = outputs[0]['labels'].cpu().numpy()
        scores = outputs[0]['scores'].cpu().numpy()

        #display_image_with_boxes(image, boxes, labels, scores)
        #st.image('filename.svg', caption='Resultant Image', use_column_width=True)
        #st.image('filename.jpg', caption='Resultant Image', use_column_width=True)
        random_filename = display_image_with_boxes(image, boxes, labels, scores)

        st.image(random_filename, caption='Resultant Image', use_column_width=True)


        print("image with boxes")