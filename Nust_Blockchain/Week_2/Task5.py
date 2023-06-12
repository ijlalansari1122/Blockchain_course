import hashlib;


file_name ='./Lab5.pdf';






# def_1


def hashed(block):
    block =hashlib.sha256(block).hexdigest()
    return hashed





# def 2

def  generatehashed():
    
    with open(file_name, 'rb') as file:
     file_opened=file.read()
    
    blocksize=len(file_opened) //1024;
    
    dataBlocks =[file_opened[i:i+blocksize]for i in range(0, len(file_opened),blocksize)]
    data_hashed =[hashed(block) for block in dataBlocks]
     
    return data_hashed.copy();    
    
    
# def 3 
    
def total_HASH(a, b):
    return  a+b
    
         
# def 4

def  Merkel_Tree():
    
  value = generatehashed();  
      
  while len(value)>1:
      
   data_array=[];
   for i in range(0 , len(value), 2):
       
       if  i+1<len(value):
           
        calculated_total =total_HASH(value[i] ,value[i+1])
           
        hashed_value =calculated_total.encode();
           
        data_array.append(hashed(hashed_value));
       else:
           data_array.append[value[i]];
           
           
           value = data_array
           
           
  return value[0];
         


print('THE MERKLE TREE IS '+ Merkel_Tree())    
    
