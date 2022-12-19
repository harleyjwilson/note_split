import argparse
import os


def create_cli():
    parser = argparse.ArgumentParser(
        description="A tool to split one note to many in your zettelkasten."
    )
    parser.add_argument("file", type=os.path.abspath, help="a note file")
    parser.add_argument(
        "-d",
        "--dryrun",
        default=None,
        action="store_true",
        help="dry run process to standard output",
    )
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s 0.0.1")
    args = None
    try:
        args = parser.parse_args()
    except SystemExit:
        pass

    return args
