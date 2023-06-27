import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from ecdsa import  SECP256k1



def Bitcoin_KEYS():
    ECDSAprivatekey = ec.generate_private_key(ec.SECP256K1 ,default_backend)
    public_key = ECDSAprivatekey.public_key()
    return ECDSAprivatekey, public_key;
   
   
   
   
#    hashes

def Hashes(value ):
    return hashlib.sha256(value).digest()
   
   
     
   
   
def ripemd(values):
    return hashlib.new('ripemd160', values).digest()
       
# FN_2    
   
   
def concatenated(x ,y):
    return x +y
       
   
   
   
    
def generate_bitcoin_address(public_key):
     
    sha256_hash = Hashes(public_key)
 
    ripemd160_hash = ripemd(sha256_hash)
 
    version_byte = b'\x00'
    extended_ripe_hash = concatenated(version_byte ,ripemd160_hash)

 
    sha256_hash2 = Hashes(extended_ripe_hash)

 
    sha256_hash3 = Hashes(sha256_hash2)

 
    checksum = sha256_hash3[:4]

 
    extendedripehash = concatenated(extended_ripe_hash ,checksum)

 
    bitcoin_address = base58.b58encode(extendedripehash).decode()

    return bitcoin_address


# ----------------main function----------------------# 

def MAIN():
    
  
     # Generate ECDSA keys
    private_key, public_key = Bitcoin_KEYS()
    # Convert public key bytes to hexadecimal representation
    publicbytes = public_key.public_bytes(encoding=serialization.Encoding.X962
    ,format=serialization.PublicFormat.UncompressedPoint);
    

    
    # Generate Bitcoin wallet address
    bitcoin_address = generate_bitcoin_address(publicbytes)
    print( bitcoin_address)

    
    
print('THE bitcoin wallet generated is ')
MAIN()





