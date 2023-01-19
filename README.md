# testpackage
This package defines a single function called "calculate_porosity" which takes the path of the thin section image as an input, and returns the porosity of the rock/sediment as a percentage.
The function uses OpenCV to load the image, convert it to grayscale, apply a threshold to separate the rock/sediment from the voids, measure the total area of the image, measure the area of the voids in the image, and finally calculates the porosity.

To use this package, you will need to import it in your code and call the "calculate_porosity" function with the path of the thin section image as an input.

It's important to note that the threshold values used in this example may not be appropriate for all images and the method used to threshold the image may not work well depending on the characteristics of the image. You may need to adjust the threshold values and the method used to threshold the image to get accurate results.

Also, this package is just an example, you may need to add more functionalities, validations, and error handling to make it more robust.
