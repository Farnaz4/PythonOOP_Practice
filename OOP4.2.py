class my_calculator:
    def product(self, *nums):
        prod= 1
        print(nums)
        for x in nums:
            prod = prod * x
        print(prod)

#multiple methods can't have the same name in python
#method overloading is not supported in python unlike java
#===================================================

c1 = my_calculator()
c1.product(4,5)
c1.product(4, 5, 9, 15)