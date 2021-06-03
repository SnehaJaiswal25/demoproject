import os
from sneha_project import version_check


def test_file_is_present():
    # here we are giving valid file names with valid addresses
    # os.path.exists checks if file is there or not
    file1 = "C:/Users/suttamjaiswal/Desktop/folder1/file1.txt"
    file2 = "C:/Users/suttamjaiswal/Desktop/folder2/file2.txt"

    bool_list = version_check.check_file(file1, file2)

    assert bool_list[0].__eq__(True)
    assert bool_list[1].__eq__(True)


def test_file_not_present():
    # here we are giving invalid file names
    # os.path.exists checks if file is there or not
    file1 = "C:/Users/suttamjaiswal/Desktop/folder1/file3.txt"
    file2 = "C:/Users/suttamjaiswal/Desktop/folder2/file4.txt"

    bool_list = version_check.check_file(file1, file2)

    assert bool_list[0].__eq__(False)
    assert bool_list[1].__eq__(False)


def test_versions():
    # if versions are same return is 0
    assert version_check.versionCompare('1.11.1', '1.11.1') == 0
    # if version1 > version2 then return is 1
    assert version_check.versionCompare('1.11.2', '1.11.1') == 1
    # if version 1 < version2 then return is -1
    assert version_check.versionCompare('1.11.1', '1.11.2') == -1
