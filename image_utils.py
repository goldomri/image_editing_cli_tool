import numpy as np
from PIL import Image


class ImageUtils:
    """
    Static class for relevant image util methods
    """

    @staticmethod
    def convert_image_to_array(image: Image) -> np.ndarray:
        """
        Converts and image to a numpy array.
        :param image: Input image.
        :return: Image in numpy array form.
        """
        return np.array(image, dtype=np.float32)

    @staticmethod
    def convert_to_rgb(image: Image) -> Image:
        """
        Converts an image to RGB.
        :param image: Input image.
        :return: Image in RGB format.
        """
        return image.convert('RGB')

    @staticmethod
    def convert_to_grayscale(image: Image) -> Image:
        """
        Converts an image to grayscale.
        :param image: Input image.
        :return: Image in grayscale format.
        """
        return image.convert('L')
