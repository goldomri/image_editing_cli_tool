from typing import List
from enums import AdjustmentType, FilterType, OperationType
from image_adjustments import *
from image_filters import *
from image_utils import *
from image_operation import ImageOperation


class ImageEditor:
    """
    Class applying all the image operation according to given list of operations.
    """

    def __init__(self, image_path: str, operations: List[ImageOperation]):
        try:
            self._image = Image.open(image_path)
            self._image = convert_to_rgb(self._image)
        except IOError as e:
            raise IOError(f"Unable to open image: {e}.")

        self._operations = operations

        self._adjustments = {
            AdjustmentType.BRIGHTNESS.value: adjust_brightness,
            AdjustmentType.CONTRAST.value: adjust_contrast,
            AdjustmentType.SATURATION.value: adjust_saturation,
            AdjustmentType.TEMPERATURE.value: adjust_temperature,
            AdjustmentType.EXPOSURE.value: adjust_exposure
        }

        self._filters = {
            FilterType.BLUR.value: apply_box_blur_filter,
            FilterType.EDGE_DETECTION.value: apply_edge_detection_filter,
            FilterType.SHARPEN.value: apply_sharpen_filter,
            FilterType.INVERT.value: apply_invert_filter,
            FilterType.SEPIA.value: apply_sepia_filter
        }

    def apply_operations(self) -> None:
        """
        Applies all operations on the image in order of input.
        :return: None.
        """
        for operation in self._operations:
            operation_type = operation.type
            if operation_type == OperationType.ADJUSTMENT.value:
                self._adjust_image(operation)

            elif operation_type == OperationType.FILTER.value:
                self._filter_image(operation)

            elif operation_type == OperationType.DISPLAY.value:
                self._display_image()

            elif operation_type == OperationType.OUTPUT.value:
                self._save_image(operation.output_path)

    def _adjust_image(self, adjustment_operation: ImageOperation) -> None:
        """
        Adjusts the image.
        :param adjustment_operation: An ImageOperation representing the adjustment.
        :return: None. Changes self._image to the adjusted image.
        """
        adjustment_type = adjustment_operation.sub_type
        value = adjustment_operation.value
        self._image = self._adjustments[adjustment_type](self._image, value)

    def _filter_image(self, filter_operation: ImageOperation) -> None:
        """
        Filters the image.
        :param filter_operation: An ImageOperation representing the filter.
        :return: None. Changes self._image to the filtered image.
        """
        filter_type = filter_operation.sub_type

        # filters with two parameters
        if filter_type == FilterType.BLUR.value:
            self._image = self._filters[filter_type](self._image, filter_operation.x, filter_operation.y)

        # filters with one parameter
        elif filter_type == FilterType.SHARPEN.value:
            self._image = self._filters[filter_type](self._image, filter_operation.x)

        # Filters with no parameters
        elif filter_type in [FilterType.EDGE_DETECTION.value, FilterType.INVERT.value, FilterType.SEPIA.value]:
            self._image = self._filters[filter_type](self._image)

    def _display_image(self) -> None:
        """
        Displays the current image.
        :return: None.
        """
        self._image.show()

    def _save_image(self, output_path: str) -> None:
        """
        Saves the current image in a designated path.
        :param output_path: Path in which to save image into.
        :return: None.
        :raise: IOError in case there was a problem in saving the image.
        """
        try:
            self._image.save(output_path)
        except IOError as e:
            raise IOError(f"Unable to save image: {e}.")
