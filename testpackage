# testpackage.py

import cv2

class testpackage:
    def calculate_porosity(image_path):
        
        """
        This function takes the path of a thin section image and returns the porosity of the rock/sediment.

        :param image_path: The path of the thin section image.
        :return: porosity of the rock/sediment as a percentage.
        """
        # Load the thin section image
        img = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply a threshold to the image to separate the rock/sediment from the voids
        ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # Measure the total area of the image
        total_area = gray.shape[0] * gray.shape[1]

        # Measure the area of the voids in the image
        voids_area = cv2.countNonZero(thresh)

        # Calculate the porosity
        porosity = (voids_area / total_area) * 100

        return porosity


# In[ ]:




