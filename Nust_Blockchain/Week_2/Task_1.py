import hashlib


# assigning variable

Calculate_hash = 'c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c';

# assigning file path in a variable

filename = "/home/poono/Desktop/New Folder/Blockchain_course/Nust_Blockchain/Week_2/Lab5.pdf"
with open(filename, 'rb') as file:
    file_contents = file.read()
    hashed = hashlib.sha256(file_contents).hexdigest()


if  hashed == Calculate_hash:{
     print('Hashes Match')
}
else:{
    print('Hashes dont match')
    
}
taskname = "/home/poono/Desktop/New Folder/Blockchain_course/Nust_Blockchain/Week_2/app.txt"


with open(taskname , 'rb') as file:
 int_content  =file.read()
 olaalgo =hashlib.sha256(int_content).hexdigest() ;

print(olaalgo)

