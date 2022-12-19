import os

from src.note_split.cli import create_cli
from src.note_split.file_io import read_file, write_file
from src.note_split.note_manipulation import parse_input_text

DELIMITER = "==="


def main():
    args = create_cli()

    try:
        dir = os.path.dirname(args.file) + "/"

        filename = os.path.basename(args.file)
    except UnboundLocalError:
        pass

    print("Reading " + filename)
    try:
        file_text = read_file(dir + filename)
    except FileNotFoundError as e:
        print(e)

    print("Parsing text from " + filename)
    output_files = parse_input_text(file_text)

    if args.dryrun is None:
        print("Writing " + str(len(output_files)) + " files")
        for file in output_files:
            filename = file
            try:
                write_file((dir + filename), output_files[file])
            except FileNotFoundError as e:
                print(e)
    else:
        print("Writing " + str(len(output_files)) +
              " notes to standard output\n")
        for file in output_files:
            print("- " + file)
            for line in output_files[file]:
                print(line, end="")
            print("")

    print("Done")


if __name__ == "__main__":
    main()
