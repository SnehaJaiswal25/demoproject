import os


# Python program to compare two version number

# Method to compare two versions.
# Return 1 if v2 is smaller,
# -1 if v1 is smaller,,
# 0 if equal
def versionCompare(v1, v2):
    # This will split both the versions by '.'
    arr1 = v1.split(".")
    arr2 = v2.split(".")
    n = len(arr1)
    m = len(arr2)
    print('n =', n, 'm = ', m)

    # converts to integer from string
    arr1 = [int(i) for i in arr1]
    arr2 = [int(i) for i in arr2]

    # compares which list is bigger and fills
    # smaller list with zero (for unequal delimeters)
    if n > m:
        for i in range(m, n):
            arr2.append(0)
    elif m > n:
        for i in range(n, m):
            arr1.append(0)

    print(arr1, '|', arr2)

    # returns 1 if version 1 is bigger and -1 if
    # version 2 is bigger and 0 if equal
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return 1
        elif arr2[i] > arr1[i]:
            return -1
    return 0


# this method is just to check if files exists or not
def check_file(file1, file2) -> list:
    bool1 = os.path.exists(file1)
    bool2 = os.path.exists(file2)

    return [bool1, bool2]


# Driver program to check above comparison function

file1 = "C:/Users/suttamjaiswal/Desktop/folder1/file1.txt"
file2 = "C:/Users/suttamjaiswal/Desktop/folder2/file2.txt"

bool_list = check_file(file1, file2)

if bool_list[0].__eq__(True) and bool_list[1].__eq__(True):

    ver1 = open(file1, "r");
    version1 = ver1.readline();
    print(version1);

    ver2 = open(file2, "r");
    version2 = ver2.readline();
    print(version2);

    ans = versionCompare(version1, version2)
    if ans < 0:
        print(version1 + " is smaller")
    elif ans > 0:
        print(version2 + " is smaller")
    else:
        print("Both versions are equal")

elif bool_list[0].__eq__(True) and bool_list[1].__eq__(False):
    print(f'{file2} does not exist..!!')

elif bool_list[0].__eq__(False) and bool_list[1].__eq__(True):
    print(f'{file1} does not exist..!!')

else:
    print('files does not exists..!!')
