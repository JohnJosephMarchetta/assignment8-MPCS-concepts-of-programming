
#calculating GCD by euclidean algo

def greatest_common_divisor(a,b):
# check first which integer is bigger and effectively re-assign that to a
    if a >= b:
        if b==0:
            return a
        else: 
            r= a % b
            return greatest_common_divisor(b,r)
    else:
        if a == 0:
            return b
        else:
            r = b % a
            return greatest_common_divisor(a,r)
 # return the greatest common divisor
print(greatest_common_divisor(12,16))
