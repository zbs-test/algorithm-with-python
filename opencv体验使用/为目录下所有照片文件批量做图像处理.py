# 在linux上测试
import cv2
import os

imgpath = './imgs/'#目录
filelist = os.listdir(imgpath)
print("check filelist is ok: ",filelist)

for i in filelist:

    img = cv2.imread(imgpath+i,cv2.IMREAD_UNCHANGED)
    print('img.shape: ', img.shape)

    logo = cv2.imread('./data/opencv_logo.png',cv2.IMREAD_UNCHANGED)
    logo = cv2.resize(logo, (20, 20))
    print('logo.shape: ', logo.shape)

    butterfly= cv2.imread('./data/butterfly.jpg', cv2.IMREAD_UNCHANGED)
    butterfly = cv2.resize(butterfly, (20, 20))
    print('butterfly.shape: ', butterfly.shape)

    img = cv2.resize(img, (600, 600))

    cv2.imshow('imgs/'+i, img)
    cv2.moveWindow('imgs/'+i, 0, 0)
    y = 100
    x = 50
    (b, g, r) = img[y, x]
    # print color values to screen
    print('bgr: ', b, g, r)

    #先行后列
    #img[y:y+height,x:width]
    img[100:100 + logo.shape[0], 300:300 + logo.shape[1]] = logo[:, :, 0:3]# 两张图片的shape不一样
    img[300:300 + logo.shape[1], 100:100 + logo.shape[0]] = butterfly[:, :, 0:3]

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text='col=width=X0,row=height-Y0', org=(0, 0), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2,bottomLeftOrigin=False)  # text,
    cv2.putText(img, text='col=width=X10,row=height-Y30', org=(10, 30), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,
    cv2.putText(img, text='col=width=X100,row=height-Y300', org=(100, 300), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,
    cv2.putText(img, text='col=width-X300,row=height-Y100', org=(300, 100), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,

    cv2.imshow('img+logo', img)
    cv2.imwrite('./res/'+i,img)#输出到src目录
    cv2.moveWindow('img+logo', x=img.shape[0], y=0)

    # 3s展示一个
    cv2.waitKey(3000)
