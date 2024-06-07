import numpy as np
from abc import ABC, abstractmethod
import constants
from PIL import Image


class Filter(ABC):
    """
    Abstract class for image filters
    """

    def __init__(self, image_array: np.ndarray):
        """
        Constructor of class.
        :param image_array: The image in numpy array form.
        """
        self._original_image_array = image_array

    def convolution(self, kernel: np.ndarray) -> np.ndarray:
        """
        Applies a convolution with specified kernel to the image array.
        :param kernel: Kernel of the convolution.
        :return: The new image array after convolution operation.
        :raise: ValueError in case the kernel size is bigger than the image size.
        """
        if self._original_image_array.ndim == 2:
            self._original_image_array = self._original_image_array[:, :, np.newaxis]

        kernel_height, kernel_width = kernel.shape
        # Checking if kernel size is valid
        if kernel_height > self._original_image_array.shape[0] or kernel_width > self._original_image_array.shape[1]:
            raise ValueError(constants.CONVOLUTION_KERNEL_SIZE_ERR_MSG)

        # Padding the image in preparation for convolution operation
        pad_height, pad_width = kernel_height // 2, kernel_width // 2
        padded_image = np.pad(self._original_image_array, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)),
                              mode='reflect')
        # Creating output array
        new_image_array = np.zeros_like(self._original_image_array)
        # Applying convolution operation
        for i in range(new_image_array.shape[0]):
            for j in range(new_image_array.shape[1]):
                for k in range(new_image_array.shape[2]):
                    new_image_array[i, j, k] = np.sum(kernel * padded_image[i:i + kernel_height, j:j + kernel_width, k])

        # If the original image was grayscale (single channel), remove the singleton dimension.
        if new_image_array.shape[2] == 1:
            new_image_array = new_image_array.squeeze(axis=2)
        return new_image_array

    def get_original_image_array(self) -> np.ndarray:
        """
        Getter for the original image array field.
        :return: Original image array field.
        """
        return self._original_image_array

    @abstractmethod
    def apply_filter(self, x=None, y=None) -> np.ndarray:
        """
        Abstract method for applying the filter.
        :param x: Optional parameter for the filter.
        :param y: Optional parameter for the filter.
        :return: New filtered image as a numpy array.
        """
        pass


class BoxBlurFilter(Filter):
    """
    Class for applying the Box Blur filter.
    """

    def apply_filter(self, x=None, y=None) -> np.ndarray:
        """
        Method for applying the Box Blur filter.
        :param x: x size of kernel.
        :param y: y size of kernel.
        :return: New filtered image as a numpy array.
        """
        # Checking if x and y are inputted
        if not x or not y:
            raise ValueError(constants.UNSPECIFIED_KERNEL_SIZE_ERR_MSG)
        kernel = np.ones((x, y)) / (x * y)
        return self.convolution(kernel).astype(np.uint8)


class EdgeDetectionFilter(Filter):
    """
    Class for applying the Edge Detection filter.
    """

    def apply_filter(self, x=None, y=None) -> np.ndarray:
        """
        Method for applying the Edge Detection filter.
        :param x: Irrelevant argument.
        :param y: Irrelevant argument.
        :return: New filtered image as a numpy array.
        """
        # Initializing filter kernels
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        # Applying convolution
        grad_x = self.convolution(sobel_x)
        grad_y = self.convolution(sobel_y)
        # Summing the output
        grad = np.hypot(grad_x, grad_y)
        # Making sure output is in valid range
        return np.clip(grad, constants.MAX_INTENSITY, constants.MIN_INTENSITY).astype(np.uint8)

class SharpenFilter(Filter):
    """
    Class for applying the Sharpening filter.
    """

    def apply_filter(self, x=None, y=None) -> np.ndarray:
        edge_detection_filter = EdgeDetectionFilter(self.get_original_image_array())



if __name__ == "__main__":
    img = Image.open("test.jpg").convert('L')
    img_arr = np.array(img, dtype=np.float32)
    filter = EdgeDetectionFilter(img_arr)
    new_img_arr = filter.apply_filter()
    new_image = Image.fromarray(new_img_arr).show()