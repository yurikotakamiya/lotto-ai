import platform


def is_linux():
    p = platform.platform()
    return 'linux' in p.lower()
