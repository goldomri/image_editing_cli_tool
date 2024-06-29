from dataclasses import dataclass
from enums import AdjustmentType, FilterType, OperationType
from typing import Optional, Union


@dataclass
class ImageOperation:
    """
    Class representing an operation to be done on an image
    """
    type: OperationType
    sub_type: Optional[Union[AdjustmentType, FilterType]] = None
    x: Optional[Union[int, float]] = None
    y: Optional[int] = None
    value: Optional[int] = None
    output_path: Optional[str] = None
