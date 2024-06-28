from image_utils import *


def apply_box_blur_filter(image: Image, x: int, y: int) -> Image:
    """
    Method for applying the Box Blur filter.
    :param image: Image to apply filter on.
    :param x: x size of kernel.
    :param y: y size of kernel.
    :return: New filtered image.
    :raise: ValueError if x or y are not positive.
    """
    # Checking if x and y are inputted
    if x <= 0 or y <= 0:
        raise ValueError(constants.UNSPECIFIED_KERNEL_SIZE_ERR_MSG)
    image_array = convert_image_to_array(image)
    kernel = np.ones((x, y)) / (x * y)
    image_array = convolution(image_array, kernel).astype(np.uint8)
    return Image.fromarray(image_array)


def apply_edge_detection_filter(image: Image) -> Image:
    """
    Method for applying the Edge Detection filter.
    :param image: Image to apply filter on.
    :return: New filtered image.
    """
    # Converting the image to grayscale is necessary in this filter
    image = convert_to_grayscale(image)
    image_array = convert_image_to_array(image)
    # Initializing filter kernels
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    # Applying convolution
    grad_x = convolution(image_array, sobel_x)
    grad_y = convolution(image_array, sobel_y)
    # Summing the output
    grad = np.hypot(grad_x, grad_y)
    # Making sure output is in valid range
    image_array = np.clip(grad, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)
    # Converting image back to RGB
    filtered_image = Image.fromarray(image_array)
    return convert_to_rgb(filtered_image)


def apply_sharpen_filter(image: Image, sharpen_magnitude: float) -> Image:
    """
    Method for applying the Sharpen filter.
    :param image: Image to apply filter on.
    :param sharpen_magnitude: Sharpening magnitude.
    :return: New filtered image.
    :raise: ValueError if sharpen_magnitude is smaller than 1.
    """
    # Checking if sharpen_magnitude is valid
    if sharpen_magnitude < 1:
        raise ValueError(constants.INVALID_SHARPEN_MAGNITUDE_ERR_MSG)
    image_array = convert_image_to_array(image)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_array = convolution(image_array, kernel) * sharpen_magnitude
    image_array = np.clip(image_array, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)
    return Image.fromarray(image_array)


def apply_invert_filter(image: Image) -> Image:
    """
    Method for applying the Invert Colors filter.
    :param image: Image to apply filter on.
    :param x: Irrelevant argument.
    :param y: Irrelevant argument.
    :return: New filtered image.
    """
    image_array = convert_image_to_array(image).astype(np.uint8)
    inverted_image_array = constants.MAX_INTENSITY - image_array
    return Image.fromarray(inverted_image_array)


def apply_sepia_filter(image: Image) -> Image:
    """
    Method for applying the Sepia filter.
    :param image: Image to apply filter on.
    :param x: Irrelevant argument.
    :param y: Irrelevant argument.
    :return: New filtered image.
    """
    image_array = convert_image_to_array(image)
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    image_array = image_array.dot(sepia_filter.T)
    image_array = np.clip(image_array, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)
    return Image.fromarray(image_array)
