with open('input.txt', 'r') as inputText:
    array = []
    lines = inputText.readlines()
    for line in lines:
       array.append(int(line))

# use three pointer technique O(n^2) bc two nested loops
def threeSum(arr, target):
    sortedArr = sorted(arr)

    for pointerOne in range(len(arr)):
        left = pointerOne + 1
        right = len(arr) - 1
        while (left < right):
            if (sortedArr[pointerOne] + sortedArr[left] + sortedArr[right]) == target:
                return sortedArr[pointerOne] * sortedArr[left] * sortedArr[right]
            elif (sortedArr[pointerOne] + sortedArr[left] + sortedArr[right]) > target:
                right -= 1
            elif (sortedArr[pointerOne] + sortedArr[left] + sortedArr[right]) < target:
                left += 1

# hash technique O(n^2)
def threeSumHash(arr, target):
    for i in range(len(arr)):
        s = set()
        curr_sum = abs(target - arr[i])
        for j in range(i+1, len(arr)):
            if (curr_sum - arr[j]) in s:
                return arr[i] * arr[j] * (curr_sum - arr[j])
            s.add(arr[j])


if __name__ == "__main__":
    print(threeSumHash(array, 2020))