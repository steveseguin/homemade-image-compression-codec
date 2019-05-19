import cv2
import numpy as np

image = cv2.imread("image.jpg")
cv2.imshow("1",image)

dct = cv2.dct(np.float32(image[:,:,0])/255)

blur = cv2.GaussianBlur(image[:,:,0],(15,15),0)

dct2 = cv2.dct(np.float32(blur)/255)


idct = cv2.idct(dct[0:int(639/5),0:int(960/5)]-dct2[0:int(639/5),0:int(960/5)])

cv2.imshow("3",np.uint8(np.clip(idct/idct.max(), 0, 1)*255))
cv2.waitKey(0)