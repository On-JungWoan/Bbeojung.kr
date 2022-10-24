import cv2
import torch
import PIL.Image
import torchvision.transforms as transforms

class ExtractObjects(object):
    def __init__(self, topology):
        self.topology = topology

    def __call__(self, image, object_counts, objects, normalized_peaks, left=0, top=0, w_scale=0.0, h_sacle=0.0):
        topology = self.topology
        height = 224
        width = 224

        K = topology.shape[0]
        count = int(object_counts[0])
        K = topology.shape[0]
        output_data = []
        for i in range(count):
            color = (0, 255, 0)
            obj = objects[0][i]
            C = obj.shape[0]
            data = []
            for j in range(C):
                k = int(obj[j])
                if k >= 0:
                    peak = normalized_peaks[0][j][k]
                    x = int((round(float(peak[1]) * width) * w_scale) + left)
                    y = int((round(float(peak[0]) * height) * h_sacle) + top)
                else:
                    x, y = 0.0, 0.0
                data.append((k, x, y))
            output_data.append(data)
        return output_data


class DrawObjects(object):
    def __init__(self, topology):
        self.topology = topology

    def __call__(self, image, object_counts, objects, normalized_peaks, left=0, top=0, w_scale=0.0, h_sacle=0.0):
        topology = self.topology
        height = 224
        width = 224

        K = topology.shape[0]
        count = int(object_counts[0])
        K = topology.shape[0]
        for i in range(count):
            color = (0, 255, 0)
            obj = objects[0][i]
            C = obj.shape[0]
            for j in range(C):
                k = int(obj[j])
                if k >= 0:
                    peak = normalized_peaks[0][j][k]
                    x = int((round(float(peak[1]) * width) * w_scale) + left)
                    y = int((round(float(peak[0]) * height) * h_sacle) + top)
                    cv2.circle(image, (x, y), 3, color, 2)

def bbox_rescale(x1, x2, y1, y2, width, height):
    x1 = min(x1, x1 - (width * 0.05)) if min(x1, x1 - (width * 0.05)) > 0 else 0
    x2 = max(x2, x2 + (width * 0.05)) if max(x2, x2 + (width * 0.05)) <= width else width
    y1 = min(y1, y1 - (height * 0.05)) if min(y1, y1 - (height * 0.05)) > 0 else 0
    y2 = max(y2, y2 + (height * 0.05)) if max(y2, y2 + (height * 0.05)) <= height else height

    return int(x1), int(x2), int(y1), int(y2)                    



def preprocess(image):
    mean = torch.Tensor([0.485, 0.456, 0.406]).cuda()
    std = torch.Tensor([0.229, 0.224, 0.225]).cuda()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(image)
    image = transforms.functional.to_tensor(image).to(device)
    image.sub_(mean[:, None, None]).div_(std[:, None, None])
    return image[None, ...]


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')