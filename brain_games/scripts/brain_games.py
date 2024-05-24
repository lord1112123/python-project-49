#!/usr/bin/env python3
import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))


cli_path = os.path.join(current_path, '..', 'cli.py')
sys.path.append(os.path.dirname(cli_path))

from cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == "__main__":
    main()
