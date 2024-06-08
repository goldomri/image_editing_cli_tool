from typing import List, Tuple
from enums import AdjustmentType, FilterType, OperationType
from image_adjustments import ImageAdjustment
from image_filters import *


class ImageProcessor:
    """
    Class applying all the image operation according to given list of operations.
    """

    def __init__(self, image_path: str, operations: List):
        try:
            self._image = Image.open(image_path)
        except IOError as e:
            raise IOError(f"Unable to open image: {e}.")

        self._operations = operations

        self._adjustments = {
            AdjustmentType.BRIGHTNESS.value: ImageAdjustment.adjust_brightness,
            AdjustmentType.CONTRAST.value: ImageAdjustment.adjust_contrast,
            AdjustmentType.SATURATION.value: ImageAdjustment.adjust_saturation
        }

        self._filters = {
            FilterType.BLUR.value: BoxBlurFilter(),
            FilterType.EDGE_DETECTION.value: EdgeDetectionFilter(),
            FilterType.SHARPEN.value: SharpenFilter(),
        }

    def apply_operations(self) -> None:
        """
        Applies all operations on the image in order of input.
        :return: None.
        """
        for operation in self._operations:
            operation_type = operation[0]
            if operation_type == OperationType.ADJUSTMENT.value:
                self._adjust_image(operation)

            elif operation_type == OperationType.FILTER.value:
                self._filter_image(operation)

            elif operation_type == OperationType.DISPLAY.value:
                self._display_image()

            elif operation_type == OperationType.OUTPUT.value:
                self._save_image(operation[1])

    def _adjust_image(self, adjustment_operation: Tuple) -> None:
        """
        Adjusts the image.
        :param adjustment_operation: A tuple consisting the adjustment type and necessary values.
        :return: None. Changes self._image to the adjusted image.
        """
        adjustment_type = adjustment_operation[1]
        value = adjustment_operation[2]
        self._image = self._adjustments[adjustment_type](self._image, value)

    def _filter_image(self, filter_operation: Tuple) -> None:
        """
        Filters the image.
        :param filter_operation: A tuple consisting the filter type and necessary values.
        :return: None. Changes self._image to the filtered image.
        """
        filter_type = filter_operation[1]
        filter = self._filters[filter_type]
        if filter_type == FilterType.BLUR.value:
            self._image = filter.apply_filter(self._image, filter_operation[2], filter_operation[3])

        elif filter_type == FilterType.SHARPEN.value:
            self._image = filter.apply_filter(self._image, filter_operation[2])

        elif filter_type == FilterType.EDGE_DETECTION.value:
            self._image = filter.apply_filter(self._image)

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
        """
        try:
            self._image.save(output_path)
        except IOError as e:
            raise IOError(f"Unable to save image: {e}.")
