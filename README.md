# red-ded-2
 Getting the video feed from the camera.  Detecting any rectangular red color object.  Given: one of the dimension(length or breadth) of the rectangular object is known to you.  To find: print the unknown dimension of the object with the help of the known dimension. 
# Red Rectangle Detection

This code captures a video feed from the camera and detects any rectangular red colour object. Given one of the dimensions (length or breadth) of the rectangular object, it prints the unknown dimension of the object with the help of the known dimension.

## Requirements

- Python 3.x
- OpenCV

## Usage

To use the code, you will need to hardcode the known length or breadth of the rectangle in the `known_length` variable at the beginning of the script. Then, run the script using the following command:

## Example

Assuming that the known length of the rectangle is 10 pixels, the output of the code might look like this:
Unknown length: 5 pixels
Unknown length: 5 pixels
Unknown length: 5 pixels
...


## Notes

- You can only hardcode one side of the rectangle in the code.
- The code assumes that the dimensions of the rectangle are in pixels.
- The code is designed to detect rectangles within a specific range of red colors in the HSV color space. You may need to adjust the lower and upper bounds of the red color range to suit your needs.
