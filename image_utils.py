import numpy as np
from PIL import Image
class ImageUtils:
    """
    Static class for relevant image util methods
    """

    @staticmethod
    def convert_image_to_array(image: Image) -> np.ndarray:
        return np.array(image, dtype=np.float32)

    @staticmethod
    def convert_to_rgb(image: Image) -> Image:
        return image.convert('RGB')

    @staticmethod
    def convert_to_grayscale(image: Image) -> Image:
        return image.convert('L')

