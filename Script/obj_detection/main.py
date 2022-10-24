import os
import json
import torch
import torchvision.transforms as transforms
import ctypes
import cv2
import matplotlib.pyplot as plt
# from cuda import cudart

from functions import *


KEYPOINT_WIDTH = 224
KEYPOINT_HEIGHT = 224

OBJ_THRESH1 = 0.45
OBJ_THRESH2 = 0.6
IOU_THRESHOLD = 0.5

MODEL_WEIGHTS = 'resnet18_baseline_att_224x224_A_epoch_249.pth'
PLUGIN_LIBRARY = "libmyplugins.so"


transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225]),
])
precision = 'fp32'
ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_path=precision)
ssd_model.to(device)
ssd_model.eval()

nvidia_ssd_processing_utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')
traced_model = torch.jit.trace(ssd_model, [torch.randn((1, 3, 300, 300)).to("cuda")])
traced_model.state_dict()
trt_model = traced_model


# ctypes.CDLL(PLUGIN_LIBRARY)
# cudart.cudaDeviceSynchronize()    

##
def run(image):
    transformed_image = transform(image)
    tensor = torch.tensor(transformed_image, dtype=torch.float32)
    tensor = tensor.unsqueeze(0).to(device)
    with torch.no_grad():
        detections = trt_model(tensor)
    results_per_input = nvidia_ssd_processing_utils.decode_results(detections)
    best_results_per_input = [nvidia_ssd_processing_utils.pick_best(results, OBJ_THRESH1) for results in
                                results_per_input]                                  

    for image_idx in range(len(best_results_per_input)):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        orig_h, orig_w = image.shape[0], image.shape[1]
        bboxes, classes, confidences = best_results_per_input[image_idx]
        save_img = image[:, :].copy() # 왜 있는거지?
        org_height = image.shape[0]
        org_width = image.shape[1]

        for idx in range(len(bboxes)):
            if classes[idx] != 1:
                continue
            if classes[idx] == 1 and confidences[idx] < OBJ_THRESH2:
                continue  

            # get the bounding box coordinates in xyxy format
            x1, y1, x2, y2 = bboxes[idx]
            # resize the bounding boxes from the normalized to 300 pixels
            x1, y1 = int(x1 * 300), int(y1 * 300)
            x2, y2 = int(x2 * 300), int(y2 * 300)
            # resizing again to match the original dimensions of the image
            x1, y1 = int((x1 / 300) * orig_w), int((y1 / 300) * orig_h)
            x2, y2 = int((x2 / 300) * orig_w), int((y2 / 300) * orig_h)

            ww = x2 - x1
            hh = y2 - y1

            ### Preprocess input ###
            copy_img = image[:, :, ::-1].copy()

            nx1, nx2, ny1, ny2 = bbox_rescale(x1, x2, y1, y2, org_width, org_height)

            crop_img = copy_img[ny1:ny2, nx1:nx2].copy()
            try:
                crop_img = cv2.resize(crop_img, dsize=(KEYPOINT_WIDTH, KEYPOINT_HEIGHT),
                                        interpolation=cv2.INTER_AREA)
            except:
                print(crop_img.shape, nx1, nx2, ny1, ny2)


            

            # 객체 바운딩 박스
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)            
            color = (255, 0, 0)

    return image


img = cv2.imread('D:/projects/bbeojung.kr/Script/obj_detection/test_input.jpg', cv2.IMREAD_COLOR)
output = run(img)
plt.imsave( 'D:/projects/bbeojung.kr/Script/obj_detection/test.jpg', output )