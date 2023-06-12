import hashlib;

file_name ='./Lab5.pdf';


def Parsing():
    
  with open(file_name , 'rb') as file:
   opened_file=file.read()    
  # parsing file into 8 parts
  block_size=len(opened_file) //8;
  data_Blocks=[opened_file[i:i+block_size] for i in range(0 , len(opened_file) ,block_size)    ]
  hashed =[hashing(block) for block in data_Blocks]
  
  return hashed.copy();
# hash of each block

def  hashing(value):
    hashed_value =hashlib.sha256(value).hexdigest();
    return hashed_value;

# addition

def HASH_SUM(x,y):
    add= x+y;
    return add;


    


# main function

def  Merkle_tree():
    
 values_1 =Parsing();
 while len(values_1)>1:
   data_values=[];
   for i in range(0 ,len(values_1), 2):
     if  i+1<len(values_1):
        hashed_sum=HASH_SUM(values_1[i] ,values_1[i+1])
        hash_encoded=hashed_sum.encode();
        total_hash=hashing(hash_encoded)   
        data_values.append(total_hash)
 else:data_values.append(values_1[i])  
 
 values_1=data_values;
 
 
 return values_1[0]; 
        
        
      # main function call
      
      
print('THE MAIN TREE OF MERKLE IS'+ Merkle_tree()) 
               
