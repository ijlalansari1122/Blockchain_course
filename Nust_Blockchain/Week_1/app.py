import bcrypt;
import hashlib;

# string

Name_id = 'Ijlalansari'
Convert_id = Name_id.encode()
print(Convert_id)

def  function1(value1):
     name1= hashlib.sha256(value1).hexdigest()
     name2= hashlib.blake2s(value1).hexdigest()
     name3= hashlib.sha512(value1).hexdigest()
     name4= hashlib.sha1(value1).hexdigest()
     salt =bcrypt.gensalt();
     bcrypt_name = bcrypt.hashpw(Convert_id, salt)
     ripemd160_Name = hashlib.new("ripemd160", Convert_id).hexdigest()
     return name1, name2 ,name3 , name4, bcrypt_name,ripemd160_Name


print('the first hashes are:' , function1(Convert_id) )

# part 2

Name_id2 = 'Parvez elahi re-arrested from outside Lahore court a'
Convert_id2 = Name_id2.encode()
print(Convert_id2)

def  function2(value):
     name1= hashlib.sha256(value).hexdigest()
     name2= hashlib.blake2s(value).hexdigest()
     name3= hashlib.sha512(value).hexdigest()
     name4= hashlib.sha1(value).hexdigest()
     salt =bcrypt.gensalt();
     bcrypt_name = bcrypt.hashpw(Convert_id, salt)
     ripemd160_Name = hashlib.new("ripemd160", Convert_id).hexdigest()
     return name1, name2 ,name3 , name4, bcrypt_name,ripemd160_Name

# fn_2
print('the second hashes are:' ,function2(Convert_id2))