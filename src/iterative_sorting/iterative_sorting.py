# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        while cur_index < len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    counter = []
    for i in range(len(arr)):
        if arr[i] < 0:
            return 'Negative number not allowed'
        if arr[i] > maximum:
            maximum = arr[i]
            counter += [0] * ((maximum + 1) - len(counter))
        counter[arr[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i + 1]
    counter.insert(0, 0)
    counter.pop()
    sort = [0] * len(arr)
    for x in arr:
        sort[counter[x]] = x
        counter[x] -= 1
    return sort

