def large_power(base,exoponent):
    ans=base**exoponent
    if ans>=5000:
        return True
    else:
        return False
    
def divisible_by_ten(num):
    check=num%10==0
    if check==0:
        return True
    else:
        return False

    
print(large_power(2,12))

print(divisible_by_ten(88))
        