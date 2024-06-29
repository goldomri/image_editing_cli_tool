# Image Editing CLI Tool

## Introduction

This project is an Image Editing CLI Tool designed to apply custom filters and adjustments to images using image
processing techniques.

## Features

- **Filters**:
    - <ins>*Box Blur*</ins>: Blurs the image by averaging the pixel values in a user-defined neighborhood.
      <br>
      <img src="images/blur.jpg" width="200">
    - <ins>*Edge Detection*</ins>: Uses the Sobel operator to highlight edges in the image.
      <br>
      <img src="images/edge_detection.jpg" width="200">
    - <ins>*Sharpen*</ins>: Enhances edges by increasing the contrast between adjacent pixels.
      <br>
      <img src="images/sharpen.jpg" width="200">
    - <ins>*Invert*</ins>: Inverts colors of an image by switching each pixel value to it's opposite value.
      <br>
      <img src="images/invert.jpg" width="200">
    - <ins>*Sepia*</ins>: Imparts a mellow tone to an image, giving it a vintage appearance.
      <br>
      <img src="images/sepia.jpg" width="200">
- **Adjustments**:
    - <ins>*Brightness*</ins>: Adjusts the brightness of the image.
      <br>
      <img src="images/brightness_pos.jpg" width="200"> <img src="images/brightness_neg.jpg" width="200">
    - <ins>*Contrast*</ins>: Modifies the contrast of the image.
      <br>
      <img src="images/contrast_pos.jpg" width="200"> <img src="images/contrast_neg.jpg" width="200">
    - <ins>*Saturation*</ins>: Alters the saturation of the image.
      <br>
      <img src="images/saturation_pos.jpg" width="200"> <img src="images/saturation_neg.jpg" width="200">
    - <ins>*Temperature*</ins>: Adjusts the temperature of the image.
      <br>
      <img src="images/temperature_pos.jpg" width="200"> <img src="images/temperature_neg.jpg" width="200">
    - <ins>*Exposure*</ins>: Modifies the exposure of the image.
      <br>
      <img src="images/exposure_pos.jpg" width="200"> <img src="images/exposure_neg.jpg" width="200">
- **Layering**: Supports applying multiple filters and adjustments in sequence.
- **Display / Save**: Allows users to display the edited image or save it to a designated path.

## Usage

Then, use the tool by running the following command from the command line:

```
python main.py edit_image --image <path-to-image> [--filter <filter-name> --filter-specific_name 
<filter-specific_value>] [--adjust <adjustment-name> <value>] [--filter <filter-name> --filter-specific_name 
<filter-specific_value>] ... [--display] [--output <output_path>]
```

### Examples

- Apply a blur filter with kernel size of [3,3] and increase brightness by 60 units, while displaying the result image:
  ```
  python main.py edit_image --image input.png --filter blur --x 3 --y 3 --adjust brightness 60 --display
  ```
- Decrease contrast by 20 units and apply a sharpening filter with magnitude 1.1, while saving the result image:
  ```
  python main.py edit_image --image input.png --adjust contrast -20 --filter sharpen --x 1.1 --output output.png
  ```

## API

The tool supports the following commands:

- **`--image <path>`**: Specifies the path to the image file.
- **`edit_image`**: The primary command to edit images - Necessary.
- **`--image <path-to-image>`**: Image to load and edit - Necessary.
- **`--filter <filter-name> --filter-specific_name <filter-specific_value>`**: Applies a specified filter with the
  given arguments. filter options:
    1. <ins>*Blur*</ins> - Blurs the image with a given blur kernel size. Should receive x and y arguments representing
       the blur kernel size. x and y should be positive integers smaller than image width and height.
       Example command could be: **`--filter blur --x 5 --y 7`** to apply a blur filter with kernel size of [5, 7].

    2. <ins>*Edge Detection*</ins> - Detects edges of an image. Doesn't need to receive arguments.
       Example command could be: **`--filter edge_detection`** to apply an edge detection filter.

    3. <ins>*Sharpen*</ins> - Sharpens and image with a given magnitude factor. Should receive x arguments representing
       the magnitude of the filter. x should be a float greater than 1.
       Example command could be: **`--filter sharpen --x 1.2`** to apply a sharpening filter with magnitude of 1.2.

    4. <ins>*Invert*</ins> - Inverts colors of an image. Doesn't need to receive arguments.
       Example command could be: **`--filter invert`** to apply an inversion filter.

    5. <ins>*Sepia*</ins> - Gives an image a warm brown tone, which makes it look like an old photograph. Doesn't 
       need to
       receive arguments.
       Example command could be: **`--filter sepia`** to apply a sepia filter.

- **`--adjust <adjustment-name> <value>`**: Applies a specified adjustment with the given value. adjustment options:
    1. <ins>*Brightness*</ins> - Adjusts the brightness of an image with a given adjustment value. Value should be an
       integer in range [-255, 255].
       Example command could be: **`--adjustment brightness 30`** to increase brightness by 30.

    2. <ins>*Contrast*</ins> - Adjusts the contrast of an image with a given adjustment value. Value should be an
       integer in range [-255, 255].
       Example command could be: **`--adjustment contrast -20`** to decrease contrast by 20.

    3. <ins>*Saturation*</ins> - Adjusts the saturation of an image with a given adjustment value. Value should be an
       integer in range [-100, 100].
       Example command could be: **`--adjustment saturation 50`** to increase saturation by 50.
    4. <ins>*Temperature*</ins> - Adjusts the temperature of an image with a given adjustment value. Value should be an
       integer in range [-100, 100].
       Example command could be: **`--adjustment temperature -40`** to decrease saturation by 40.

    5. <ins>*Exposure*</ins> - Adjusts the exposure of an image with a given adjustment value. Value should be an
       integer in range [-100, 100].
       Example command could be: **`--adjustment exposure 70`** to increase saturation by 70.

  In addition, multiple --adjust parameters can be chained to apply several adjustments in one command. for example:
  **`--adjustment brightness -10 saturation 70`** is a valid command, and it will decrease brightness by 10 and then
  increase saturation by 70.

- **`--display`**: Displays the image after completing the previous actions.

- **`--output <output-path>`**: Saves the image in the given path after completing the previous actions.
