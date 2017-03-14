
def insertionSort(ar):    
    for i in range(1, len(ar)):
        to_insert = ar[i]
        j = i - 1
        while(j >= 0):
            if ar[j] > to_insert:
                ar[j + 1] = ar[j]
                ar[j] = to_insert
            j -= 1
        print ' '.join(str(k) for k in ar)
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
