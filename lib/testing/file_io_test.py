import os
from lib.file_io import write_file, append_file, read_file

def test_write_file():
    file_name = "testfile"
    file_content = "This is a test."
    write_file(file_name, file_content)
    with open(file_name + ".txt", 'r') as file:
        assert file.read() == file_content
    os.remove(file_name + ".txt")

def test_append_file():
    file_name = "testfile"
    initial_content = "This is a test."
    append_content = " This is appended."
    write_file(file_name, initial_content)
    append_file(file_name, append_content)
    with open(file_name + ".txt", 'r') as file:
        assert file.read() == initial_content + append_content
    os.remove(file_name + ".txt")

def test_read_file():
    file_name = "testfile"
    file_content = "This is a test."
    write_file(file_name, file_content)
    assert read_file(file_name) == file_content
    os.remove(file_name + ".txt")
