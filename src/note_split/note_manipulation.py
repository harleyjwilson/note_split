DELIMITER = "==="


def parse_input_text(file_text):
    output_files = {}
    temp_note = []
    in_split = False

    for line in file_text:
        if in_split:
            if not line[0: len(DELIMITER)] == DELIMITER:
                temp_note.append(line)
            else:
                in_split = False
                output_files.update({generate_filename(
                    temp_note[0]): temp_note.copy()})
                temp_note.clear()
        elif not in_split:
            if line[0: len(DELIMITER)] == DELIMITER:
                in_split = True

    return output_files


def generate_filename(title):
    filename = title.translate({ord(letter): None for letter in
                                '/:|"<>.,;=#[]'})
    filename = filename.strip() + ".md"

    return filename
