
def merge_sort(nums):
    if len(nums) > 1:
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
           if left[i] < right[j]:
              nums[k] = left[i]
              i = i + 1

           else:
              nums[k] = right[j]
              j = j + 1
           k = k + 1

        while i < len(left):
            nums[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1


numbers = [6, 8, 10, 16, 14, 12, 4, 5, 7, 9]
merge_sort(numbers)
print(numbers)
