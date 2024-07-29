#!/usr/bin/env python
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description="Start NetGaze Agent")
    parser.add_argument("operation", type=str, help="Operation to perform. [start]/[version]")

    args = parser.parse_args()

    operation = args.operation
    port = args.port

    if operation == 'start':
        if port:
            _start()
        _start()
    elif operation == 'version':
        _version()
    else:
        print(f'Invalid operation - {operation}')


def _start():
    logging.info(f"Starting...")


def _version():
    print("Version...")


if __name__ == "__main__":
    main()
