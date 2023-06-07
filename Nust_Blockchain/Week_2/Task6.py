import hashlib


File_name =('./Lab5.pdf')


def generatehashes(value):
    return hashlib.sha256(value).hexdigest()
    
    
    


def  parsing():
    
    with open(File_name, "rb") as file:
        file_data = file.read()
        Size_BLOCK = len(file_data) // 1024
        blocks = [file_data[i:i+Size_BLOCK] for i in range(0, len(file_data), Size_BLOCK)]
        hashes = [generatehashes(block) for block in blocks]
        return hashes.copy()



def  total_hash(x , y):
   return x+y
    


def MarkleTree():
               
    values = parsing()
    
    while len(values) > 1:
        
        Data_array = []
        for i in range(0, len(values), 2):
            if i+1 < len(values):
                Total_HASH=total_hash(values[i] ,values[i+1])
                hashed_value= Total_HASH.encode()
                Data_array.append(generatehashes(hashed_value))
            else:
                Data_array.append(values[i])
        values = Data_array


    return values[0]



print("The RootMerkle is :", MarkleTree())
