import hashlib


File_name =('./Lab5.pdf')


# function for generating hashes

def generatehashes(value):
     
 hashed =hashlib.sha256(value).hexdigest()
 return hashed 
    
    
# function for parsing

def  parsing():
    with open(File_name, "rb") as file:
        file_data = file.read()
        Size_BLOCK = len(file_data) // 1024
        blocks = [file_data[i:i+Size_BLOCK] for i in range(0, len(file_data), Size_BLOCK)]
        # hash generate
        hashes = [generatehashes(block) for block in blocks]
     
    return hashes.copy()

# for total hash

def  total_hash(x , y):
   add= x+y
   return add; 

#  main function with loops and conditions
def MarkleTree():
               
    values = parsing()
    
    while len(values) > 1:
        
        Data_array = []
        for i in range(0, len(values), 2):
            if i+1 < len(values):
          
                Total=total_hash(values[i],values[i+1])
                
                hashed_value= Total.encode()
                
                Data_array.append(generatehashes(hashed_value))
            else:
                Data_array.append(values[i])
                
        values = Data_array


    return values[0]

# main function call


print("The RootMerkle is :", MarkleTree())
