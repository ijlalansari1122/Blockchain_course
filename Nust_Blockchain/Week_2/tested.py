import hashlib


   
#
# hashed
def hashed(value ):
    return hashlib.sha256(value.encode()).hexdigest()
    
def added(x ,y):
    return hashed(x+y)
            
           
# added 
        # 
array = ['part1' , 'part2' ,'part3' , 'part4' ,'part5' ,'part6' , 'part7' , 'part8']

# PART1
# 
# for i in array:
#     hashed(i)
# part1 and part2 concatenated and hashed

Hashed_sum1 =added(array[0],array[1])

# part3 and part4 concatenated and hashed

Hashed_sum2= added(array[2],array[3]);

# hashed_sum1 and hashed_sum2 concatenated and hashed

Hashed1= added(Hashed_sum1,Hashed_sum2);
# part 5 and 6 hashed and concatenated

Hashed_sum3 =added(array[4],array[5]);

# part 7 and 8 hashed and concatenated

Hashed_sum4 = added(array[6],array[7]);

Hashed2 =added(Hashed_sum3,Hashed_sum4)

finalhashed = added(Hashed1 ,Hashed2)

print(finalhashed);



