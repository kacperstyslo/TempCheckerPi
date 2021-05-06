# !/usr/bin/env python3
from config import AppConfig


def preconfigure_info() -> str:
    return "App is now prefiguring, wait . . . "


if __name__ == '__main__':
    print(preconfigure_info())
    app_config = AppConfig()
    app_config()
