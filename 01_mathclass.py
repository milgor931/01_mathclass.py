import math
import collections

class Statistics:
    def _init_(self, nums):
        self.nums = nums

    def printStats(self, nums):
        print("Min: " + str(self.min(nums)))
        print("Max: " + str(self.max(nums)))
        print("Mean: " + str(self.mean(nums)))
        print("Median: " + str(self.median(nums)))
        print("Mode: " + str(self.mode(nums))

    def min(self, nums):
        min = 1000000
        for x in nums:
            if x < min:
                min = x
        return min

    def max(self, nums):
        max = 0
        for x in nums:
            if x > max:
                max = x
        return max

    def mean(self, nums):
        sum  = 0
        for x in nums:
            sum += x
        return sum/len(nums)

    def median(self, nums):
        ordered = sorted(nums)

        if len(ordered)%2 != 0:
            return ordered[int(len(ordered) /2)]
        else:
            total = ordered[int((len(ordered)) /2)] + ordered[int((len(ordered) -1) /2) ]
            return total/2

    def mode(self, nums):
        count = collections.Counter(nums)
        most = ""
        for item in count:
            if count[item] > most:
                most = item
        return most

m = Statistics()

nums = [142, 6, 13, 36, 54, 4, 9, 78, 78, 102]
print(nums)
m.printStats(nums)
m.mode(nums)
