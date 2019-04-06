import argparse
import csv
import os

from .reader import read_data
from .utils import get_header_from_file

__version__ = '0.1.1'


def quoting_type(s):
    if s == 'all':
        return csv.QUOTE_ALL
    elif s == 'minimal':
        return csv.QUOTE_MINIMAL
    elif s == 'nonnumeric':
        return csv.QUOTE_NONNUMERIC
    elif s == 'none':
        return csv.QUOTE_NONE
    else:
        raise argparse.ArgumentTypeError('separator is wrong')


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        column=None,
        delimiter=',',
        encoding='utf-8',
        header='first_line',
        header_columns=[],
        quotechar='"',
        quoting=csv.QUOTE_NONE,
        sort=False,
    )
    parser.add_argument('-c', '--column', nargs='*',
                        help='set column to display')
    parser.add_argument('-d', '--delimiter',
                        help='set delimiter character in file')
    parser.add_argument('-e', '--encoding',
                        help='set encoding')
    parser.add_argument('--header',
                        help='set path to header file')
    parser.add_argument('--quotechar',
                        help='set quote character in file')
    parser.add_argument('--quoting', type=quoting_type,
                        help='set quoting')
    parser.add_argument('--sort', action='store_true',
                        help='sort row data with header column name')

    parser.add_argument('data', help='set path to data file')
    args = parser.parse_args()

    if args.header != 'first_line':
        if not os.path.isfile(args.header):
            raise ValueError(f'"{args.header}" is not path to header file')
        args.header_columns = get_header_from_file(args.header)

    return args


def main():
    args = parse_argument()
    with open(args.data, mode='r', encoding=args.encoding) as f:
        reader = csv.reader(f, delimiter=args.delimiter, quoting=args.quoting,
                            quotechar=args.quotechar)
        if args.header == 'first_line':
            args.header_columns = next(reader)
        read_data(args, reader)


if __name__ == '__main__':
    main()
