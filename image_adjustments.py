from PIL import Image
import numpy as np


class ImageAdjustment:
    """
    Class responsible for image adjustments.
    """
    MAX_INTENSITY = 255
    MIN_INTENSITY = 0

    @staticmethod
    def adjust_brightness(image_array: np.ndarray, value: float) -> np.ndarry:
        """
        Adjusts brightness of an image which is represented as a numpy array.
        :param image_array: The image in numpy array form.
        :param value: Brightness value to adjust the image
        :return: New adjusted image as a numpy array
        """
        return np.clip(image_array + value, ImageAdjustment.MIN_INTENSITY, ImageAdjustment.MAX_INTENSITY)

    @staticmethod
    def adjust_contrast(image_array: np.ndarry, value: float) -> np.ndarray:




