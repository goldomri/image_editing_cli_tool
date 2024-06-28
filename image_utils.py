import numpy as np
from PIL import Image
import constants


def convert_image_to_array(image: Image) -> np.ndarray:
    """
    Converts and image to a numpy array.
    :param image: Input image.
    :return: Image in numpy array form.
    """
    return np.array(image, dtype=np.float32)


def convert_to_rgb(image: Image) -> Image:
    """
    Converts an image to RGB.
    :param image: Input image.
    :return: Image in RGB format.
    """
    return image.convert('RGB')


def convert_to_grayscale(image: Image) -> Image:
    """
    Converts an image to grayscale.
    :param image: Input image.
    :return: Image in grayscale format.
    """
    return image.convert('L')


def convolution(image_array: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Applies a convolution with specified kernel to the image array.
    :param image_array: Image to convolve on in numpy array form.
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
