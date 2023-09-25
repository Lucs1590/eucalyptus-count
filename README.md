# Eucalyptus Count

This project is made to count the number of eucalyptus trees in a given image.

To do it, basically the steps are:

1. Read the image
2. Convert it to HSV color space
3. Get the intersection between upper and lower bounds mapped to trackbars
4. Apply a Gaussian blur to the image
5. Detect the contours of the image
6. Draw the contours on the image

Doing it you will get the number of eucalyptus trees in the terminal.

The green contours are the ones that were detected as eucalyptus following the determined rules.
The red contours are the ones that didn't follow the rules.

An example of the result is shown below:

![Detections](https://raw.githubusercontent.com/Lucs1590/eucalyptus-count/main/images/detections.jpeg)

## How to run

To run the project, you need to have Python 3 installed on your machine. Then, you need to install the needed libraries. To do it, run the following command:

```bash
pip install -r requirements.txt
```

After that, you can run the project with the following command:

```bash
python src/trackbar_new.py
```

If you want to understand how the code works, you can check the [trackbar_new.py](src/trackbar_new.py) file. But if you want to see a simpler version of color detection, you can check the [highlight_color.py](src/highlight_color.py) file.
