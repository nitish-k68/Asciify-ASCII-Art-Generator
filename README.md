# Asciify-ASCII-Art-Generator


## Project Description : 

ASCII (American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
Other than texts, we can use this for images and videos. So here we are converting video(mp4) to ASCII encoded strings that look like the video.


## How to run the project (include all dependencies) :

* Necessary libraries to be installed – OpenCV, PIL(python image library), numpy, math
* Input (.MP4) video file for ASCII video creation.
* Rename “filename”  as the input file directory.
* Use “Font” from the default windows fonts folder (.ttf file).
* e.g. Font=ImageFont.truetype(**'C:\\Windows\\Fonts\\Georgia.ttf'**, 17)
* Specify the character list to be used from **character** list.
* e.g. charlist = Character["mode"]  //mode can be “standard” or “complex”
* Setting **charwidth, charheight, scale_factor


## Internal working of a project :

First, we will take the input video from the project directory. Then we will select a character list for mapping our output frames also, we will be setting the character dimensions to fit our output frame. After this, we will resize the input frames that we have extracted from the source video file, then we will calculate height and width of output frame with respect to the input frames and character size. 

Then  we will be mapping the output frame through rows and columns. After that, we will fill the output frame with assigned characters using the **ImageDraw.draw()** function, then we will display every frame with some time lag using **cv2.waitkey()**. 

We can use the **cv2.waitkey()** function to change the speed of the video.


## Key learning takeaways from this project :

*	Better understanding of the python language
*	Work experience on the project-based libraries/frameworks like OpenCV, PIL(python image library), numpy
*	Better knowledge of image processing 


## Resources/References used while working on the project :

*	https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles
*	https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/
*	https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
*	https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
*	https://pillow.readthedocs.io/en/stable/reference/Image.html


