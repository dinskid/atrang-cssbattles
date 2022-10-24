import numpy as np
from skimage.metrics import structural_similarity as _ssim
from torchvision import models

def pixel_diff(imga, imgb):
    w, h = imga.size
    pixels = w * h
    imga = np.asarray(imga.convert('L'), dtype=np.uint8)
    imgb = np.asarray(imgb.convert('L'), dtype=np.uint8)
    diff = np.abs(imga - imgb)
    return np.sum(diff) / (pixels * 255) 

def _get_freq(img):
    w, h, c = img.shape
    f_img = np.zeros((256, 256, 256))
    for i in range(w):
        for j in range(h):
            r, g, b = img[i,j]
            f_img[r,g,b] += 1

    return f_img


def color_diff(imga, imgb):
    imga = np.asarray(imga.convert('RGB'), dtype=np.uint8)
    imgb = np.asarray(imgb.convert('RGB'), dtype=np.uint8)
    w, h, c = imga.shape

    f_imga = _get_freq(imga)
    f_imgb = _get_freq(imgb)
    
    return np.sum(np.abs(f_imga - f_imgb)) / (w * h * c)

def ssim(imga, imgb):
    imga = np.asarray(imga.convert('RGB'), dtype=np.uint8)
    imgb = np.asarray(imgb.convert('RGB'), dtype=np.uint8)
    return _ssim(imga, imgb, channel_axis=2)

def distance(imga, imgb):
    imga = np.asarray(imga, dtype=np.uint8)
    imgb = np.asarray(imgb, dtype=np.uint8)
    resnet = models.resnet50(pretrained=True)


