import hashlib
import bcrypt


File_name =('/home/poono/Desktop/New Folder/Blockchain_course/Nust_Blockchain/Week_2/Lab5.pdf')





with open(File_name, "rb") as file:
    file_contents = file.read()
    initial_hash = hashlib.sha256(file_contents).hexdigest()


blocksize =len(File_name) // 8

dataBlocks =[File_name[i:i+blocksize]for i in range(0 , len(File_name),blocksize)];
hashed_1 =dataBlocks.encode()
Hashed_value =[hashlib.sha256(hashed_1).hexdigest() for block in dataBlocks
    ]


print(Hashed_value)


