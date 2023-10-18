# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target_sum):
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))


                return pairs
            
users_input = input("Enter the integers of the array, seperated by spaces: ")
my_array = list(map(int, users_input.split()))

target = int(input("Enter the target sum: "))

result = find_pairs(my_array, target)

print(result)