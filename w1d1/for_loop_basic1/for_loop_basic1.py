# # to run type python3 for_loop_basic1.py, and hit enter
# # 1. Basic
for nums in range(0, 151):
    print(nums)
# 2. Multiples of 5
for nums in range(5, 1000, 5):
    print(nums)
# 3. Counting, the Dojo Way
for nums in range(1, 101):
    if nums % 5 == 0:
        print("Coding")
    elif nums % 10 == 0:
        print("Coding Dojo")  # on running, this is never printed
    else:
        print(nums)
# 4. Add odd integers from 0 to 500,000 and print the final sum
sum = 0
for nums in range(0, 12):
    if nums % 2 != 0:
        sum += nums
print(sum) #unindent to move it outside the for loop
# 4. Countdown by Fours
for nums in range(2018, 0, -4):
    print(nums)
# 5. Flexible Counter
for nums in range(lowNum, highNum, 3):
    if nums % 3 == 0:
        print(nums)