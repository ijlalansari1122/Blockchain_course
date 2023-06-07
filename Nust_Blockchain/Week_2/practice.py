import hashlib;

filename='./Lab5.pdf';


array1=[]
array2=[]
array3=[]

with open(filename , 'rb') as file:
   filed_open =len(file.read());
   file.seek(0)
   
   
   file_size=int(filed_open/7);
   
   for i in range(8):
     file_hash=hashlib.sha256();
     data=file.read(file_size)
    file_hash.update(data)
    
array1.append(file_hash.hexdigest())



for i in range(0,7,2):
    array2.append(hashlib.sha256((array1[0+i]+array1[1+i]).encode()).hexdigest())
    
    
    
    


for i in range(0,3,2):
    array3.append(hashlib.sha256((array2[0+i]+array2[1+i]).encode()).hexdigest())
    
    
    
    final_hash= hashlib.sha256((array3[0]+array3[1]).encode()).hexdigest();
    
    
    print(final_hash)
    
    
    
