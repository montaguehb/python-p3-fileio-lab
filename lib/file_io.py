def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w", encoding="utf-8")  as file:
        file.write(file_content)
        file.close()


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a", encoding="utf-8") as file:
        file.write(append_content)
        file.close()


def read_file(file_name):
    with open(f"{file_name}.txt", 'r', encoding="utf-8") as file:
        return file.read()
