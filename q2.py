#Write a function find_max(nums) that returns the largest number in a list WITHOUT using max().
def find_max(nums):
    if not nums:
        return None  # Handles an empty list

    largest = nums[0]

    for number in nums:
        if number > largest:
            largest = number

    return largest

print(find_max([4, 9, 2, 15, 7]))  # 15