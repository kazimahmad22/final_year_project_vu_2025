import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('images/image 1.jpg')


def denoise(image_path):
    noisy_img = cv.imread(image_path)
    noisy_img_rgb = cv.cvtColor(noisy_img, cv.COLOR_BGR2RGB)

    gasblur_img = cv.GaussianBlur(noisy_img, ksize=(5, 5), sigmaX=0)
    gasblur_img_rgb = cv.cvtColor(gasblur_img, cv.COLOR_BGR2RGB)

    meidanblur_img = cv.medianBlur(noisy_img, ksize=5)
    meidanblur_img_rgb = cv.cvtColor(meidanblur_img, cv.COLOR_BGR2RGB)

    plt.figure(figsize=(2, 2))
    plt.subplot(2, 2, 1)
    plt.title('Noisy Image')
    plt.imshow(noisy_img_rgb)
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Guassian Image')
    plt.imshow(gasblur_img_rgb)
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('Median Image')
    plt.imshow(meidanblur_img_rgb)
    plt.axis('off')

    plt.show()


denoise('images/image 1.jpg')
