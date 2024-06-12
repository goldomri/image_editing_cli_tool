from enum import Enum


class AdjustmentType(Enum):
    """
    Enum for image adjustment types.
    """
    BRIGHTNESS = "brightness"
    CONTRAST = "contrast"
    SATURATION = "saturation"
    TEMPERATURE = "temperature"
    EXPOSURE = "exposure"


class FilterType(Enum):
    """
    Enum for image filter types.
    """
    BLUR = "blur"
    EDGE_DETECTION = "edge_detection"
    SHARPEN = "sharpen"
    INVERT = "invert"
    SEPIA = "sepia"


class OperationType(Enum):
    """
    Enum for image operation types.
    """
    ADJUSTMENT = "adjustment"
    FILTER = "filter"
    DISPLAY = "display"
    OUTPUT = "output"
