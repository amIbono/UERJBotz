import cv2 as cv
img = cv.imread("opencv\joe.jpeg",-1)
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imwrite('opencv\joecerto.png',img)
print(img[0][0][0])
cv.imshow('Image',img)
cv.waitKey(0)
'cv.destroyAllWindows()'