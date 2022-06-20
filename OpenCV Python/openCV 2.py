import cv2
import random

img = cv2.imread("opencv\joe.jpeg",-1)
#print(img.shape) #(height,width,channels)

for i in range(500):
    randomColor1 = random.randint(0,255)
    randomColor2 = random.randint(0,255)
    randomColor3 = random.randint(0,255)
    for j in range(img.shape[1]):
        img[i][j] = [255,255,255]

'''tag = img[450:650,300:600]
img[100:300,650:950] = tag'''

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()