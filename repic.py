import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
import cv2
#path_pic=input("请输入图片")
# path:文件地址 num：输入文件的个数 list_source：图片通用名，列表

def  showdiff(path, num, list_source):
    num_source=len(list_source)
    imglist=[]

    for i in range(1, num):
        for j in num_source:
            imglist[j]=cv2.imread(path+list_source[j]+str(i)+'.jpeg')
            title=list_source[j]

        cv2.namedWindow(title,cv2.WINDOW_FULLSCREEN)

        img_con1 = cv2.imread(path + 'rec_crf23seq4-00' + str(i) + '.jpeg')
        img_con2 = cv2.imread(path + 'rec_crf25seq4-00' + str(i) + '.jpeg')
        title_1 = 'crf23-pic' + str(i)
        title_2 = 'crf25-pic' + str(i)
        cv2.namedWindow(title_1, cv2.WINDOW_FULLSCREEN)
        # cv2.namedWindow("测试图像",cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty(title_1, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.putText(img_con1, "crf23", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (13, 46, 89), 3, 8)
        cv2.imshow(title_1, img_con1)

        cv2.waitKey(2000)
        # cv2.namedWindow(title_1, cv2.WINDOW_FULLSCREEN)
        # cv2.setWindowProperty(title_2, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.putText(img_con2, "crf25", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (13, 46, 89), 3, 8)
        cv2.imshow(title_1, img_con2)
        # cv2.imshow("测试图像",img_con2)
        cv2.waitKey(2000)



