import numpy as np
import colorsys
import constants


class ImageAdjustment:
    """
    Class responsible for image adjustments.
    """

    @staticmethod
    def adjust_brightness(image_array: np.ndarray, value: int) -> np.ndarray:
        """
        Adjusts brightness of an image which is represented as a numpy array.
        :param image_array: The image in numpy array form.
        :param value: Brightness value to adjust the image. Should be in range [-255, 255]. Negative values decrease
        brightness while positive values increase brightness.
        :return: New adjusted image as a numpy array.
        :raise: ValueError in case the value isn't in range [-255, 255].
        """
        # Checking if value is valid
        if value > constants.MAX_BRIGHTNESS_VAL or value < constants.MIN_BRIGHTNESS_VAL:
            raise ValueError(constants.INVALID_BRIGHTNESS_VAL_ERR_MSG)
        return np.clip(image_array + value, constants.MIN_INTENSITY, constants.MAX_INTENSITY).astype(np.uint8)

    @staticmethod
    def adjust_contrast(image_array: np.ndarray, value: int) -> np.ndarray:
        """
        Adjusts contrast of an image which is represented as a numpy array.
        :param image_array: The image in numpy array form.
        :param value: Contrast value to adjust the image. Should be in range [-255, 255]. Negative values decrease
        contrast while positive values increase contrast.
        :return: New adjusted image as a numpy array.
        :raise: ValueError in case the value isn't in range [-255, 255].
        """
        # Checking if value is valid
        if value > constants.MAX_CONTRAST_VAL or value < constants.MIN_CONTRAST_VAL:
            raise ValueError(constants.INVALID_BRIGHTNESS_VAL_ERR_MSG)

        # Calculating contrast factor
        factor = (constants.CONTRAST_NORM_CONST * (value + constants.MAX_INTENSITY)) / (
                constants.MAX_INTENSITY * (constants.CONTRAST_NORM_CONST - value))

        return np.clip(constants.CONTRAST_MID_VAL + factor * (image_array - constants.CONTRAST_MID_VAL),
                       constants.MIN_INTENSITY,
                       constants.MAX_INTENSITY).astype(np.uint8)

    @staticmethod
    def adjust_saturation(image_array: np.ndarray, value: int) -> np.ndarray:
        """
        Adjusts saturation of an image which is represented as a numpy array.
        :param image_array: The image in numpy array form.
        :param value: Saturation value to adjust the image. Should be in range [-100, 100]. Negative values decrease
        saturation while positive values increase saturation.
        :return: New adjusted image as a numpy array.
        :raise: ValueError in case the value isn't in range [-100, 100].
        """
        # GEN: I used chatGPT to get the formula for adjusting saturation of an image. input prompt was "What is the
        # formula for adjusting image saturation?"

        # Checking if value is valid
        if value > constants.MAX_SATURATION_VAL or value < constants.MIN_SATURATION_VAL:
            raise ValueError(constants.INVALID_SATURATION_VAL_ERR_MSG)

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
        return np.clip(image_array * constants.MAX_INTENSITY,
                       constants.MIN_INTENSITY,
                       constants.MAX_INTENSITY).astype(np.uint8)
