class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        arr = []
        for val in counter:
            arr.append(val)
        arr.sort(key = lambda char : counter[char])
        st = ""
        for c in arr:
            st=c*counter[c]+st
        return st
