def average(array):
    myset = set(array)
    sum = 0
    length = len(myset)
    for i in myset:
        sum += i
    avg = sum/length
    return avg
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)