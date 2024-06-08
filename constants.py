# Image Constants
MIN_INTENSITY = 0
MAX_INTENSITY = 255
MIN_BRIGHTNESS_VAL = -255
MAX_BRIGHTNESS_VAL = 255
MIN_CONTRAST_VAL = -255
MAX_CONTRAST_VAL = 255
CONTRAST_NORM_CONST = 259
CONTRAST_MID_VAL = 128
MIN_SATURATION_VAL = -100
MAX_SATURATION_VAL = 100

# Error Messages
INVALID_BRIGHTNESS_VAL_ERR_MSG = "Brightness adjustment value should be between -255 to 255."
INVALID_CONTRAST_VAL_ERR_MSG = "Contrast adjustment value should be between -255 to 255."
INVALID_SATURATION_VAL_ERR_MSG = "Saturation adjustment value should be between -100 to 100."
CONVOLUTION_KERNEL_SIZE_ERR_MSG = "Convolution kernel size should be smaller than image size."
UNSPECIFIED_KERNEL_SIZE_ERR_MSG = "Kernel size should be inputted by specifying x and y arguments."
UNSPECIFIED_SHARPEN_MAGNITUDE_ERR_MSG = "Sharpening magnitude should be inputted by specifying x argument."
INVALID_SHARPEN_MAGNITUDE_ERR_MSG = "Sharpening magnitude should be a float greater than 1."
INVALID_ADJUSTMENT_ERR_MSG = "Invalid adjustment type."
INVALID_Filter_ERR_MSG = "Invalid filter type."
INVALID_ADJUSTMENT_VALUE_ERR_MSG = "Every adjustment should get an integer value."
INVALID_BLUR_ARGUMENTS_ERR_MSG = "Blur filter should get x and y arguments, both positive integers."
INVALID_SHARPEN_ARGUMENT_ERR_MSG = "Sharpen filter should get x argument, a float."
INVALID_OUTPUT_ARGUMENT_ERR_MSG = "Output operation should get a file destination path."
INVALID_COMMAND_ERR_MSG = "Invalid command."
INVALID_FIRST_ARGUMENT_ERR_MSG = "First argument of the program should be edit_image."
INVALID_IMAGE_ARGUMENT_ERR_MSG = "Program should get an image path in format: '--image <image_path>'."


# Commands
EDIT_CMD = "edit_image"
IMAGE_CMD = "--image"
FILTER_CMD = "--filter"
ADJUST_CMD = "--adjust"
X_CMD = "--x"
Y_CMD = "--y"
DISPLAY_CMD = "--display"
OUTPUT_CMD = "--output"


