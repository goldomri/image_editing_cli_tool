import numpy as np
from abc import ABC, abstractmethod


class Filter(ABC):
    """
    Abstract class for image filters
    """

    CONVOLUTION_KERNEL_SIZE_ERR_MSG = "Convolution kernel size should be smaller than image size."

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
        kernel_height, kernel_width = kernel.shape
        # Checking if kernel size is valid
        if kernel_height > self._original_image_array.shape[0] or kernel_width > self._original_image_array[1]:
            raise ValueError(Filter.CONVOLUTION_KERNEL_SIZE_ERR_MSG)

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
        return new_image_array

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

    UNSPECIFIED_KERNEL_SIZE_ERR_MSG = "Kernel size should be inputted by specifying x and y arguments."

    def apply_filter(self, x=None, y=None) -> np.ndarray:
        """
        Method for applying the Box Blur filter.
        :param x: x size of kernel.
        :param y: y size of kernel.
        :return: New filtered image as a numpy array.
        """
        # Checking if x and y are inputted
        if not x or not y:
            raise ValueError(BoxBlurFilter.UNSPECIFIED_KERNEL_SIZE_ERR_MSG)
        kernel = np.ones((x, y)) / (x * y)
        return self.convolution(kernel)
