

class TopTen:

    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:

            raise StopIteration
        
values = TopTen()

print(values.__next__())

print(next(values))

for i in values:
    print(i)







# nums = [2,8,9,5]

# print(nums[7])

# for i in nums:
#     print(i)

# it = iter(nums)

# print(next(it))


# print(it.__next__())
# print(it.__next__())
