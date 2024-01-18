nums=[1,2,3,1]
output=True

def conDup(nums):
    hashset= set(nums)
    print(hashset)
    for n in nums:
        if n in hashset:
            print (output)
            break
        else:
            output==False
            print (output)
conDup(nums)