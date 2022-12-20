import os
from ctypes import windll


def get_active_code_page():
    """get active code page depend on system
    https://stackoverflow.com/questions/66137468/how-to-get-the-codepage-currently-used-in-local-computer
    """
    if os.name == 'nt':
        code_page = windll.kernel32.GetConsoleOutputCP()
        code_page = str(code_page)
    else:
        code_page = 'utf-8'
    return code_page
