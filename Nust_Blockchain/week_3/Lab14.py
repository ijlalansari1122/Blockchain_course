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

# generate Bitcoin address

def generate_bitcoin_address(public_key):
    
    sha256_hash = hashlib.sha256(public_key).digest()
    
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    
    version_byte = b'\x00'
    
    extended_ripe_hash = version_byte + ripemd160_hash
    
    sha256_hash2 = hashlib.sha256(extended_ripe_hash).digest()
    
    sha256_hash3 = hashlib.sha256(sha256_hash2).digest()
    
    checksum = sha256_hash3[:4]
    
    extendedripehash = extended_ripe_hash + checksum
    
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

print('THE bitcoin wallet generated is ')
MAIN()
