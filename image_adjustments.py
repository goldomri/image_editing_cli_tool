import colorsys
from image_utils import *


def adjust_brightness(image: Image, value: int) -> Image:
    """
    Adjusts brightness of an image.
    :param image: Input image.
    :param value: Brightness value to adjust the image. Should be in range [-255, 255]. Negative values decrease
    brightness while positive values increase brightness.
    :return: New adjusted image.
    :raise: ValueError in case the value isn't in range [-255, 255].
    """
    # Checking if value is valid
    if value > constants.MAX_BRIGHTNESS_VAL or value < constants.MIN_BRIGHTNESS_VAL:
        raise ValueError(constants.INVALID_BRIGHTNESS_VAL_ERR_MSG)
    image_array = convert_image_to_array(image)
    image_array = np.clip(image_array + value, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)
    return Image.fromarray(image_array)


def adjust_contrast(image: Image, value: int) -> Image:
    """
    Adjusts contrast of an image.
    :param image: Input image.
    :param value: Contrast value to adjust the image. Should be in range [-255, 255]. Negative values decrease
    contrast while positive values increase contrast.
    :return: New adjusted image.
    :raise: ValueError in case the value isn't in range [-255, 255].
    """
    # Checking if value is valid
    if value > constants.MAX_CONTRAST_VAL or value < constants.MIN_CONTRAST_VAL:
        raise ValueError(constants.INVALID_CONTRAST_VAL_ERR_MSG)

    image_array = convert_image_to_array(image)
    # Calculating contrast factor
    contrast_factor = (constants.CONTRAST_NORM_CONST * (value + constants.MAX_INTENSITY)) / (
            constants.MAX_INTENSITY * (constants.CONTRAST_NORM_CONST - value))

    image_array = np.clip(constants.CONTRAST_MID_VAL + contrast_factor * (image_array - constants.CONTRAST_MID_VAL),
                          constants.MIN_INTENSITY,
                          constants.MAX_INTENSITY).astype(np.uint8)
    return Image.fromarray(image_array)


def adjust_saturation(image: Image, value: int) -> Image:
    """
    Adjusts saturation of an image.
    :param image: Input image.
    :param value: Saturation value to adjust the image. Should be in range [-100, 100]. Negative values decrease
    saturation while positive values increase saturation.
    :return: New adjusted image.
    :raise: ValueError in case the value isn't in range [-100, 100].
    """
    # GEN: I used chatGPT to get the formula for adjusting saturation of an image. input prompt was "What is the
    # formula for adjusting image saturation?"

    # Checking if value is valid
    if value > constants.MAX_SATURATION_VAL or value < constants.MIN_SATURATION_VAL:
        raise ValueError(constants.INVALID_SATURATION_VAL_ERR_MSG)

    image_array = convert_image_to_array(image)
    # Normalizing values between 0 and 1
    image_array = image_array / float(constants.MAX_INTENSITY)
    saturation_factor = 1 + value / float(constants.MAX_SATURATION_VAL)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            # Converting every pixel from RGB to HLS
            r, g, b = image_array[i, j]
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            # Adjusting Saturation value
            s = min(max(s * saturation_factor, 0), 1)
            # Converting back from HLS to RGB
            r, g, b = colorsys.hls_to_rgb(h, l, s)
            image_array[i, j] = [r, g, b]
    # Converting values back to range of [0, 255]
    image_array = np.clip(image_array * constants.MAX_INTENSITY,
                          constants.MIN_INTENSITY,
                          constants.MAX_INTENSITY).astype(np.uint8)
    return Image.fromarray(image_array)


def adjust_temperature(image: Image, value: int) -> Image:
    """
    Adjusts color temperature of an image.
    :param image: Input image.
    :param value: Temperature value to adjust the image. Should be in range [-100, 100]. Negative values decrease
    temperature while positive values increase temperature.
    :return: New adjusted image.
    :raise: ValueError in case the value isn't in range [-100, 100].
    """
    # Checking if value is valid
    if value > constants.MAX_TEMPERATURE_VAL or value < constants.MIN_TEMPERATURE_VAL:
        raise ValueError(constants.INVALID_TEMPERATURE_VAL_ERR_MSG)

    image_array = convert_image_to_array(image)
    value = (value / 100.0) * 50

    r, g, b = image_array[:, :, 0], image_array[:, :, 1], image_array[:, :, 2]
    # Changing red and blue values according to input
    r = np.clip(r + value, constants.MIN_INTENSITY, constants.MAX_INTENSITY)
    b = np.clip(b - value, constants.MIN_INTENSITY, constants.MAX_INTENSITY)
    adjusted_image = np.stack((r, g, b), axis=2).astype(np.uint8)
    return Image.fromarray(adjusted_image)


def adjust_exposure(image: Image, value: float) -> Image:
    """
    Adjusts exposure of an image.
    :param image: Input image.
    :param value: Exposure value to adjust the image. Should be in range [-100, 100]. Negative values decrease
    exposure while positive values increase exposure.
    :return: New adjusted image.
    :raise: ValueError in case the value isn't in range [-100, 100].
    """
    # Checking if value is valid
    if value > constants.MAX_EXPOSURE_VAL or value < constants.MIN_EXPOSURE_VAL:
        raise ValueError(constants.INVALID_EXPOSURE_VAL_ERR_MSG)
    # Calculating exposure factor
    exposure_factor = 1 + value / float(constants.MAX_EXPOSURE_VAL)
    image_array = convert_image_to_array(image)
    image_array = np.clip(image_array * exposure_factor, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(
        np.uint8)
    return Image.fromarray(image_array)
