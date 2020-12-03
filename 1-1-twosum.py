with open('input.txt', 'r') as inputText:
    array = []
    lines = inputText.readlines()
    for line in lines:
       array.append(int(line))

numSet = set()

# hash technique
def twoSum(arr, target):
    for i in array:
        diff = abs(target - i)
        if diff in numSet:
            return diff*i
        else:
            numSet.add(i)

if __name__ == "__main__":
    print(twoSum(array, 2020))