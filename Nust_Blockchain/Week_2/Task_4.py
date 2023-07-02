import hashlib


#
# hashed
def hashed(value):
    return hashlib.sha256(value.encode()).hexdigest()       
# added 
def added(x ,y):
 return x+y     
        
array = ['part1' , 'part2' ,'part3' , 'part4' ,'part5' ,'part6' , 'part7' , 'part8']

# PART1
# 

# part1 and part2 concatenated and hashed

Hashed_sum1 =hashed(added(array[0],array[1]))

# part3 and part4 concatenated and hashed

Hashed_sum2= hashed(added(array[2],array[3]));

# hashed_sum1 and hashed_sum2 concatenated and hashed

Hashed1= hashed(added(Hashed_sum1,Hashed_sum2));
# part 5 and 6 hashed and concatenated

Hashed_sum3 =hashed(added(array[4],array[5]));

# part 7 and 8 hashed and concatenated

Hashed_sum4 = hashed(added(array[6],array[7]));

Hashed2 =hashed(added(Hashed_sum3,Hashed_sum4))

print( hashed(added(Hashed1,Hashed2)));



