from itertools import count

from .utils import generate_spaces
from .utils import get_east_asian_width


def _normalize(value):
    _value = value
    if value.find('\n') >= 0:
        converted_str = ', '.join(value.split())
        _value = f'[{converted_str}]'
    return _value


def read_data(args, reader):
    number_of_header_columns = len(args.header_columns)
    column_length = [get_east_asian_width(c) for c in args.header_columns]
    max_column_length = max(column_length)

    bar = '-' * 72
    for line_num, row in enumerate(reader, 1):
        print(f'\n##### line no: {line_num}')
        print(bar)

        row_data = zip(count(1), args.header_columns, row)
        if args.sort:
            row_data.sort(key=lambda x: x[1])

        for i, (seqnum, column, value) in enumerate(row_data):
            if args.column and (column not in args.column):
                continue

            spaces = generate_spaces(column_length[i], max_column_length)
            print(f'{seqnum:03}: {column}{spaces}: {_normalize(value)}')
        print(bar)

        number_of_row_columns = len(row)
        if number_of_header_columns != number_of_row_columns:
            msgh = f'number of header columns is {number_of_header_columns}'
            msgr = f'but row has {number_of_row_columns}'
            print(f'ERROR: {msgh}, {msgr}\n')

        char = input('Enter to next line, or q (quit): ')
        if char == 'q' or char == 'quit':
            break
