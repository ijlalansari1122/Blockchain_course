import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from ecdsa import  SECP256k1

def Bitcoin_KEYS():
    
    private_key = ec.generate_private_key(ec.SECP256K1 ,default_backend)
    
    public_key = private_key.public_key();
    
    return private_key, public_key

# hashed 

def Hashed(value):
    return hashlib.sha256(value).digest();

# added
def HASHED_concatenate(x ,y):
    return x+y
        
# ripemd

def ripemd(value):
    return hashlib.new('ripemd160', value).digest()
    



# generate Bitcoin address

def generate_bitcoin_address(public_key):
    
    sha256_hash = Hashed(public_key)
    
    ripemd160_hash = ripemd(sha256_hash)
    
    version_byte = b'\x00'
    
    extended_ripe_hash = HASHED_concatenate(ripemd160_hash ,version_byte)
    
    sha256_hash2 = Hashed(extended_ripe_hash)
    
    sha256_hash3 = Hashed(sha256_hash2)
    
    checksum = sha256_hash3[:8]
    
    extendedripehash = HASHED_concatenate(extended_ripe_hash , checksum)
    
    bitcoinaddress = base58.b58encode(extendedripehash).decode()
    
    return bitcoinaddress

def MAIN():
    # Generate ECDSA keys
    private_key, public_key = Bitcoin_KEYS()

    # Convert public key bytes to hexadecimal representation
    publicbytes = public_key.public_bytes(encoding=serialization.Encoding.X962
    ,format=serialization.PublicFormat.UncompressedPoint);


    # Generate Bitcoin wallet address
    bitcoin_address = generate_bitcoin_address(publicbytes)
    print("Bitcoin Wallet Address is:", bitcoin_address)


MAIN()
