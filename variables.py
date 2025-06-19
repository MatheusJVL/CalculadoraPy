from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
ICON_PATH = FILES_DIR / 'icon.ico'

BIG_TEXT = 40
MEDIUM_TEXT = 24
SMALL_TEXT = 18

DEFAULT_MARGIN = 15
MINIMUN_WIDTH = 500

PRIMARY_COLOR = '#e07b39'
DARK_PRIMAARY_COLOR = '#b8622e'
DARKEST_PRIMARY_COLOR = '#944e26'

import re
 
 
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')
 
 
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str):
    return len(string) == 0


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def converToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number