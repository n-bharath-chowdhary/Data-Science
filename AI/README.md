

# Detecting Faces with Python for an image from internet using OpenCV

## Installation

Download or Clone this repository

## Usage

[* you can use this module with python . An example is hown below from command line]

[--> detecting_faces uses two inputs. 1.The url of the image 2.name of the image]

syntax: detecting_faces('url','arbitrary name')

$ python

$ from detecting_faces import *

$ detecting_faces('https://tennishead.net/wp-content/uploads/2020/02/Roger-Federer-and-Rafael-Nadal.jpg','Federer_Nadal')

## Output
 
First File shows the input image

![Test Image 2](https://github.com/n-bharath-chowdhary/Data-Science/blob/master/AI/preprocessed_image.png)

Second Image shows the detcted faces

![Test Image 1](https://github.com/n-bharath-chowdhary/Data-Science/blob/master/AI/post_processed_image.png)

Third Image shows the eye detector

![Test Image 3](https://github.com/n-bharath-chowdhary/Data-Science/blob/master/AI/eye_detector_image.png)

The output shows that indeed a false detction of eye and it missed one of Roger's eye (sorry Roger!). This paves way to create a better model for eye and face detector.
Let us see that in some of the upcoming modules.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

