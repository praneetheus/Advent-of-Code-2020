import collections

with open('2-input.txt', 'r') as inputText:
    array = []
    lines = inputText.readlines()
    
    for line in lines:
       array.append(line.split())

def partOne():
    valid = 0
    for a in array:
        nums = a[0].split("-")
        match = [s for s in a[1] if s.isalnum()]
        c = collections.Counter(a[2])
        freq = c[match[0]]
        # if freq in range(int(nums[0]), int(nums[1]) + 1):
        #     valid += 1
        # if freq >= int(nums[0]) and freq <= int(nums[1]):
        #     valid += 1
        if int(nums[0]) <= freq <= int(nums[1]):
            valid += 1
    print(valid)

def partTwo():
    valid = 0

    for a in array:
        nums = a[0].split("-")
        match = [s for s in a[1] if s.isalnum()]
        letArr = list(a[2])

        if bool(letArr[int(nums[0]) - 1] == match[0]) ^ bool(letArr[int(nums[1]) - 1] == match[0]):
            valid += 1

    print(valid)

partOne()
partTwo()
