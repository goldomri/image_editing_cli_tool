import sys
from cli import parse_command_line_arguments
from image_editor import ImageEditor


def edit_image() -> None:
    """
    Main function for running the whole program. Allows the user to apply multiple filters and adjustments to an
    image using the command line.
    :return: None
    """
    arguments = sys.argv
    image_path, operations = parse_command_line_arguments(arguments)
    image_processor = ImageEditor(image_path, operations)
    image_processor.apply_operations()


if __name__ == '__main__':
    edit_image()
