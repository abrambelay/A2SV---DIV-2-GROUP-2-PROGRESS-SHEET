class Solution: 
    def select(self, arr, i):
        for i in range(n):
            return arr[i]
    
    def selectionSort(self, arr,n):
        for i in range(n):
            currMn = i
            for j in range(i+1,n):
                if arr[currMn]>arr[j]:
                    currMn = j
            arr[i],arr[currMn] = arr[currMn],arr[i]
        return arr
