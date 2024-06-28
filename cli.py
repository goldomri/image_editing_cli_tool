from typing import List, Tuple
from enums import AdjustmentType, FilterType, OperationType
import constants
from image_operation import ImageOperation


def parse_command_line_arguments(args: List) -> Tuple:
    """
    Parses command line arguments
    :param args: Command line arguments inputted.
    :return: A tuple containing the input image path and a list of operations to apply on the image.
    :raise: ValueError in case of invalid arguments.
    """
    image_path = _parse_initialization(args)
    all_operations = []
    i = 4
    while i < len(args):
        cur_arg = args[i]
        if cur_arg == constants.FILTER_CMD:
            i, operations = _parse_filter(args, i + 1)

        elif cur_arg == constants.ADJUST_CMD:
            i, operations = _parse_adjustment(args, i + 1)

        elif cur_arg == constants.DISPLAY_CMD:
            i, operations = _parse_display(args, i + 1)

        elif cur_arg == constants.OUTPUT_CMD:
            i, operations = _parse_output(args, i + 1)

        else:
            raise ValueError(constants.INVALID_COMMAND_ERR_MSG)

        all_operations.extend(operations)
    return image_path, all_operations


def _parse_initialization(args) -> str:
    """
    Responsible for parsing the start of the command line arguments.
    :param args: Command line arguments inputted.
    :return: Input image path.
    :raise: ValueError in case of invalid arguments.
    """
    # Checking if first argument is edit_image
    if len(args) < 2 or args[1] != constants.EDIT_CMD:
        raise ValueError(constants.INVALID_FIRST_ARGUMENT_ERR_MSG)
    # Checking if second argument is --image
    if len(args) < 4 or args[2] != constants.IMAGE_CMD:
        raise ValueError(constants.INVALID_IMAGE_ARGUMENT_ERR_MSG)
    return args[3]


def _parse_filter(args, i) -> Tuple:
    """
    Responsible for parsing a filter command from the command line.
    :param args: Command line arguments inputted.
    :param i: Current index to start iterating on
    :return: A tuple containing the next index of command line arguments and a list of the parsed filter operation.
    :raise: ValueError if got invalid filter arguments.
    """
    if i >= len(args) or args[i] not in [f.value for f in FilterType]:
        raise ValueError(constants.INVALID_Filter_ERR_MSG)
    filter = args[i]
    operations = []

    # Edge detection doesn't get arguments
    if filter in [FilterType.EDGE_DETECTION.value, FilterType.INVERT.value, FilterType.SEPIA.value]:
        operations.append(ImageOperation(type=OperationType.FILTER.value, sub_type=filter))
        return i + 1, operations

    elif filter == FilterType.BLUR.value:
        # Checking if got correct arguments
        if i + 4 >= len(args):
            raise ValueError(constants.INVALID_BLUR_ARGUMENTS_ERR_MSG)
        x = args[i + 1]
        y = args[i + 3]
        x_value = args[i + 2]
        y_value = args[i + 4]
        if x != constants.X_CMD or y != constants.Y_CMD or not x_value.isdigit() or not y_value.isdigit():
            raise ValueError(constants.INVALID_BLUR_ARGUMENTS_ERR_MSG)

        operations.append(
            ImageOperation(type=OperationType.FILTER.value, sub_type=filter, x=int(x_value), y=int(y_value)))
        return i + 5, operations

    elif filter == FilterType.SHARPEN.value:
        # Checking if got correct arguments
        if i + 2 >= len(args):
            raise ValueError(constants.INVALID_SHARPEN_ARGUMENT_ERR_MSG)
        x = args[i + 1]
        x_value = args[i + 2]
        if x != constants.X_CMD or not _is_float(x_value):
            raise ValueError(constants.INVALID_SHARPEN_ARGUMENT_ERR_MSG)

        operations.append(ImageOperation(type=OperationType.FILTER.value, sub_type=filter, x=float(x_value)))
        return i + 3, operations


def _parse_adjustment(args, i) -> Tuple:
    """
    Responsible for parsing an adjustment command from the command line.
    :param args: Command line arguments inputted.
    :param i: Current index to start iterating on
    :return: A tuple containing the next index of command line arguments and a list of the parsed adjustments.
    :raise: ValueError if got invalid adjustment arguments.
    """
    # First adjustment
    if i >= len(args) or args[i] not in [a.value for a in AdjustmentType]:
        raise ValueError(constants.INVALID_ADJUSTMENT_ERR_MSG)
    operations = []
    # Going over all the adjustments inputted in a chain
    while i < len(args) and args[i] in [a.value for a in AdjustmentType]:
        adjustment = args[i]
        i += 1
        # Checking if inputted value is signed int
        if i >= len(args) or not _is_signed_int(args[i]):
            raise ValueError(constants.INVALID_ADJUSTMENT_VALUE_ERR_MSG)
        value = int(args[i])
        operations.append(ImageOperation(type=OperationType.ADJUSTMENT.value, sub_type=adjustment, value=value))
        # Moving to the next adjustment
        i += 1
    return i, operations


def _parse_display(args, i) -> Tuple:
    """
    Responsible for parsing a display command from the command line.
    :param args: Command line arguments inputted.
    :param i: Current index to start iterating on
    :return: A tuple containing the next index of command line arguments and a list of the parsed display operation.
    """
    return i, [ImageOperation(type=OperationType.DISPLAY.value)]


def _parse_output(args, i) -> Tuple:
    """
    Responsible for parsing an output command from the command line.
    :param args: Command line arguments inputted.
    :param i: Current index to start iterating on
    :return: A tuple containing the next index of command line arguments and a list of the parsed output operation.
    :raise: ValueError in case there is no output destination inputted.
    """
    if i >= len(args):
        raise ValueError(constants.INVALID_OUTPUT_ARGUMENT_ERR_MSG)
    return i + 1, [ImageOperation(type=OperationType.OUTPUT.value, output_path=args[i])]


def _is_signed_int(s):
    """
    Helper function to check if a string is a signed int.
    :param s: String to check.
    :return: True if string is a signed int, False otherwise.
    """
    if s is None:
        return False
    try:
        int(s)
        return True
    except ValueError:
        return False


def _is_float(s):
    """
    Helper function to check if a string is a float.
    :param s: String to check.
    :return: True if string is a float, False otherwise.
    """
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False
