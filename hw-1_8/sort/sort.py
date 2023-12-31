def sort_arr(nums: list[int]) -> list:
    if nums is None:
        return []
    if len(nums) < 2:
        return nums
    pivo = nums[0]
    less = [i for i in nums[1:] if i <= pivo]
    great = [i for i in nums[1:] if i > pivo]
    return sort_arr(less) + [pivo] + sort_arr(great)
