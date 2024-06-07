import numpy as np
from abc import ABC, abstractmethod
import constants
from PIL import Image
from image_utils import ImageUtils


class Filter(ABC):
    """
    Abstract class for image filters
    """

    def convolution(self, image_array: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Applies a convolution with specified kernel to the image array.
        :param kernel: Kernel of the convolution.
        :return: The new image array after convolution operation.
        :raise: ValueError in case the kernel size is bigger than the image size.
        """
        # Checking if image is in grayscale, if so we need to add another dimension
        if image_array.ndim == 2:
            image_array = image_array[:, :, np.newaxis]

        kernel_height, kernel_width = kernel.shape
        # Checking if kernel size is valid
        if kernel_height > image_array.shape[0] or kernel_width > image_array.shape[1]:
            raise ValueError(constants.CONVOLUTION_KERNEL_SIZE_ERR_MSG)

        # Padding the image in preparation for convolution operation
        pad_height, pad_width = kernel_height // 2, kernel_width // 2
        padded_image = np.pad(image_array, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)),
                              mode='reflect')
        # Creating output array
        new_image_array = np.zeros_like(image_array)
        # Applying convolution operation
        for i in range(new_image_array.shape[0]):
            for j in range(new_image_array.shape[1]):
                for k in range(new_image_array.shape[2]):
                    new_image_array[i, j, k] = np.sum(kernel * padded_image[i:i + kernel_height, j:j + kernel_width, k])

        # If the original image was in grayscale we need to remove the added dimension.
        if new_image_array.shape[2] == 1:
            new_image_array = new_image_array.squeeze(axis=2)
        return new_image_array

    @abstractmethod
    def apply_filter(self, image: Image, x=None, y=None) -> Image:
        """
        Abstract method for applying the filter.
        :param image: Image to apply filter on.
        :param x: Optional parameter for the filter.
        :param y: Optional parameter for the filter.
        :return: New filtered image.
        """
        pass


class BoxBlurFilter(Filter):
    """
    Class for applying the Box Blur filter.
    """

    def apply_filter(self, image: Image, x=None, y=None) -> Image:
        """
        Method for applying the Box Blur filter.
        :param image: Image to apply filter on.
        :param x: x size of kernel.
        :param y: y size of kernel.
        :return: New filtered image.
        """
        # Checking if x and y are inputted
        if not x or not y:
            raise ValueError(constants.UNSPECIFIED_KERNEL_SIZE_ERR_MSG)
        image_array = ImageUtils.convert_image_to_array(image)
        kernel = np.ones((x, y)) / (x * y)
        image_array = self.convolution(image_array, kernel).astype(np.uint8)
        return Image.fromarray(image_array)


class EdgeDetectionFilter(Filter):
    """
    Class for applying the Edge Detection filter.
    """

    def apply_filter(self, image: Image, x=None, y=None) -> Image:
        """
        Method for applying the Edge Detection filter.
        :param image: Image to apply filter on.
        :param x: Irrelevant argument.
        :param y: Irrelevant argument.
        :return: New filtered image.
        """
        # Converting the image to grayscale is necessary in this filter
        image = ImageUtils.convert_to_grayscale(image)
        image_array = ImageUtils.convert_image_to_array(image)
        # Initializing filter kernels
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        # Applying convolution
        grad_x = self.convolution(image_array, sobel_x)
        grad_y = self.convolution(image_array, sobel_y)
        # Summing the output
        grad = np.hypot(grad_x, grad_y)
        # Making sure output is in valid range
        image_array = np.clip(grad, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)
        # Converting image back to RGB
        filtered_image = Image.fromarray(image_array)
        return ImageUtils.convert_to_rgb(filtered_image)


class SharpenFilter(Filter):
    """
    Class for applying the Sharpening filter.
    """

    def apply_filter(self, image: Image, x=None, y=None) -> Image:
        pass


if __name__ == "__main__":
    img = Image.open("test.jpg")
    filter = BoxBlurFilter()
    new_image = filter.apply_filter(img, 1, 1)
    new_image.show()

