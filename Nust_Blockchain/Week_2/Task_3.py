import hashlib

# FIRST FILE 

filename = "/home/poono/Desktop/New Folder/Blockchain_course/Nust_Blockchain/Week_2/m1.bin"
with open(filename, "rb") as file:
    file_contents = file.read()
    hashed_MD5 = hashlib.md5(file_contents).hexdigest()
    hashed_SHA1 = hashlib.sha1(file_contents).hexdigest()

print("Hashed MD5 1 IS : " + hashed_MD5 )
print("Hashed MD5 1 IS : " + hashed_SHA1 )




# Second File


filename = "/home/poono/Desktop/New Folder/Blockchain_course/Nust_Blockchain/Week_2/m2.bin"
with open(filename, "rb") as file:
    file_contents = file.read()
    hashed_MD5 = hashlib.md5(file_contents).hexdigest()
    hashed_SHA1 = hashlib.sha1(file_contents).hexdigest()

print("Hashed MD5  2 IS  : " + hashed_MD5 )
print("Hashed MD5  2 IS : " + hashed_SHA1 )


