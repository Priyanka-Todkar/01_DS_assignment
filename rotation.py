# Q3. Write a program to check if two strings are a rotation of each other? 
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    temp = str1 + str1

    if str2 in temp:
        return True
    else:
        return False

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


if are_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")