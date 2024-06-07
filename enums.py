from enum import Enum


class AdjustmentType(Enum):
    """
    Enum for image adjustment types.
    """
    BRIGHTNESS = "brightness"
    CONTRAST = "contrast"
    SATURATION = "saturation"



class FilterType(Enum):
    """
    Enum for image filter types.
    """
    BLUR = "blur"
    EDGE_DETECTION = "edge_detection"
    SHARPEN = "sharpen"
