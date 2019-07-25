import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
import  time
import cv2
#path_pic=input("请输入图片")
# path:文件地址 num：图片的帧数 list_source：图片通用名，列表

def  showdiff(path, num, list_source):
    tpye_source=len(list_source) #对比试验个数
    imglist=[]
    title=[]
    title="test"
    for i in range(1, num):
        #cv2.namedWindow(title)
        for j in range(0,tpye_source):
            in_path=path+list_source[j]+'-00'+str(i)+'.jpeg'
            imglist=cv2.imread(in_path) #读入图片
            fontInPic=list_source[j]                                   #初始化所展示图片所属title
            #cv2.namedWindow(title, cv2.WINDOW_FULLSCREEN)

            #cv2.setWindowProperty(title, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.putText(imglist, fontInPic+'-'+str(i), (100, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (13, 46, 89), 3, 8)
            cv2.imshow(title, imglist)
            cv2.waitKey(10)
            Comd=input('Please decide stop?')
            if Comd!='\r':
                time.sleep(1)









path='/Users/zhiqiang37/Documents/vbv/seq11_高触发/'
num= 8
list_source=['rec_crf23_seq11','rec_crf25_seq11']
showdiff(path,num,list_source)








