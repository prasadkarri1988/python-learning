class ForLoop:

    def printAllForward(self, nums):
        for i in range(0, len(nums)):
            print(f"{i} value {nums[i]}")

    def printAllBackward(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            print(f"{i} value {nums[i]}")


loop = ForLoop()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
loop.printAllForward(nums)
loop.printAllBackward(nums)
