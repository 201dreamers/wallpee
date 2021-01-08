"""Contains stuff, needed for working commad line arguments and options"""

from optparse import OptionParser, Values


def parse_cli_args() -> Values:
    """Function that parses arguments and keys from command line interface
    returns dict with options and its values
    """
    optparser = OptionParser(usage='usage: wallpee [options] path_for_image')

    optparser.add_option(
        '-v', '--version',
        action='store_true', help='Show version of wallpee'
    )
    optparser.add_option(
        '-p', '--path', metavar='PATH',
        action='store', help='Specify path for downloaded images'
    )
    options, args = optparser.parse_args()
    return options
