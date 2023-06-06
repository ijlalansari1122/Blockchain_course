import hashlib


# 

array = ['part1' , 'part2' ,'part3' , 'part4' ,'part5' ,'part6' , 'part7' , 'part8']

# PART1
part1=hashlib.sha256(array[0].encode()).hexdigest();


# PART2
part2=hashlib.sha256(array[1].encode()).hexdigest();

# PART3
part3=hashlib.sha256(array[2].encode()).hexdigest();

# PART4

part4=hashlib.sha256(array[3].encode()).hexdigest();


# PART5

part5=hashlib.sha256(array[4].encode()).hexdigest();


# PART6

part6=hashlib.sha256(array[5].encode()).hexdigest();

# PART7

part7=hashlib.sha256(array[6].encode()).hexdigest();



# PART8

part8=hashlib.sha256(array[7].encode()).hexdigest();



# Sum_1

sum1_1 = part1+part2;
Hashed_sum1 =hashlib.sha256(sum1_1.encode()).hexdigest();


# 
sum2_2 =part3+part4;

Hashed_sum2= hashlib.sha256(sum2_2.encode()).hexdigest();
# 
Sum1= Hashed_sum1+Hashed_sum2;

Hashed1= hashlib.sha256(Sum1.encode()).hexdigest();


# sum2

sum3_3= part5+part6

Hashed_sum3 =hashlib.sha256(sum3_3.encode()).hexdigest();

sum4_4 =part7 + part8;

Hashed_sum4 = hashlib.sha256(sum4_4.encode()).hexdigest();

Sum2 =Hashed_sum3+Hashed_sum4;

Hashed2 =hashlib.sha256(Sum2.encode()).hexdigest();


#  FINAL SUM

Final_SUM = Hashed1 + Hashed2;

Total_Sum = hashlib.sha256(Final_SUM.encode()).hexdigest();


print(Total_Sum);




# TOTal sum


total_sum =Sum1+Sum2;

# print(total_sum);












