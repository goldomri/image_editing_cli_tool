from enum import Enum


class AdjustmentType(Enum):
    """
    Enum for image adjustment types.
    """
    BRIGHTNESS = "brightness"
    SATURATION = "saturation"
    CONTRAST = "contrast"


class FilterType(Enum):
    """
    Enum for image filter types.
    """
    BLUR = "blur"
    EDGE_DETECTION = "edge_detection"
    SHARPEN = "sharpen"
