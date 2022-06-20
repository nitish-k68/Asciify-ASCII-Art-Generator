from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math

#taking the video file as an input
fileName="MS Dhoni.mp4"


#Character Map - using characters for mapping to pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


#taking charlist from Character Map
charlist = Character["complex"]


#length of character
charlen=len(charlist)
interval=charlen/256


charwidth=15
charheight=15


#Ratio of height and width of the input video
scale_factor=0.08


def get_char(i):
    return charlist[math.floor(i*interval)]


cap=cv2.VideoCapture(fileName)


Font=ImageFont.truetype('C:\\Windows\\Fonts\\Georgia.ttf', 17)


while True:

    _,img=cap.read()
    img=Image.fromarray(img)

    
    #taking height and width of input video 
    width,height=img.size
    img=img.resize((int(scale_factor*width),int(scale_factor*height*(charwidth/charheight))),Image.NEAREST)
    width,height=img.size
    pixel=img.load()


    #Calculating height and width of the output video
    outputImage=Image.new("RGB",(charwidth*width,charheight*height),color=(0,0,0))
    dest=ImageDraw.Draw(outputImage)



    #Mapping the characters
    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]
            h=int(0.299*r+0.587*g+0.114*b)
            pixel[j,i]=(h,h,h)
            dest.text((j*charwidth,i*charheight),get_char(h),font=Font,fill=(r,g,b))

    open_cv_image=np.array(outputImage)
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
    cv2.imshow("AScii Art",open_cv_image)
cap.release()
cv2.destroyAllWindows()