import unicodedata


def get_header_from_file(path):
    with open(path, mode='r') as f:
        return [line.strip() for line in f]


def generate_spaces(text_width, max_width):
    """
    >>> generate_spaces(4, 6)
    '  '
    """
    return ' ' * (max_width - text_width)


def get_east_asian_width(text):
    """
    >>> get_east_asian_width('text')
    4
    >>> get_east_asian_width('文字')
    4
    """
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in ('F', 'W', 'A'):
            width += 2
        else:
            width += 1
    return width
