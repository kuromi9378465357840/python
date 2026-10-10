# nums= [1,2,3,4,5,6,7,8,9,10]


a = int(input("Enter a number: "))
b = int(input("Generate table upto: "))

nums = range(1, b+1)

# def gen_func(nums):
#     for n in nums:
#         yield n*a

# my_gen = gen_func(nums)

my_gen = (n*a for n in nums)
for i in my_gen:
    print(i)