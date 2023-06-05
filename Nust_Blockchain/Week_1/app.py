import bcrypt;
import hashlib;

# string

Name_id = 'Ijlalansari'

# convert to encode

Convert_id = Name_id.encode()

print(Convert_id)

salt =bcrypt.gensalt();
bcrypt_name = bcrypt.hashpw(Convert_id, salt)
#MD-5

print(bcrypt_name)

Blake2  = hashlib.blake2s(Convert_id).hexdigest()
#MD-5
print(Blake2)


md5_name  = hashlib.sha256(Convert_id).hexdigest()
# #MD-5
print(md5_name)

sha_512  = hashlib.sha512(Convert_id).hexdigest()
#MD-5
print(sha_512)

sha_256  = hashlib.sha256(Convert_id).hexdigest()
print(sha_256)

Sha_1  = hashlib.sha1(Convert_id).hexdigest()
print(Sha_1)

#sha-1
ripemd160_Name = hashlib.new("ripemd160", Convert_id).hexdigest()
print(ripemd160_Name) 

 

 


# -

# avalanche effect








# 
# 
# 
# 
# string
# 
Name_id = 'Parvez elahi re-arrested from outside Lahore court'
# 
# convert to encode
# 
Convert_id=Name_id.encode()
# 
print(Convert_id)
# 
salt =bcrypt.gensalt();
bcrypt_name = bcrypt.hashpw(Convert_id, salt)
#MD-5
# 
print(bcrypt_name)
# 
Blake2  = hashlib.blake2b(Convert_id).hexdigest()
#MD-5
print(Blake2)
# 
# 
md5_name  = hashlib.sha256(Convert_id).hexdigest()
#MD-5
print(md5_name)
# 
sha_512  = hashlib.sha512(Convert_id).hexdigest()
#MD-5
print(sha_512)
# 
sha_256  = hashlib.sha256(Convert_id).hexdigest()
print(sha_256)
# 
Sha_1  = hashlib.sha1(Convert_id).hexdigest()
print(Sha_1)
# 
#sha-1
ripemd160_Name = hashlib.new("ripemd160", Convert_id).hexdigest()
print(ripemd160_Name) 



