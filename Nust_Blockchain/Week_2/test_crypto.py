from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15, MGF1
from cryptography.hazmat.primitives import padding as symmetric_padding

# Generate RSA key pair
def generateRSAkeyPair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# RSA Encrypt
def RSAencrypt(public_key, plain_text):
    cipher_text = public_key.encrypt(
        plain_text,
        padding.OAEP(
            MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text

# RSA Decrypt
def RSADecrypt(private_key, cipher_text):
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plain_text.decode('utf-8')

# Generate DSA key pair
def generateDSAKEYpair():
    private_key = dsa.generate_private_key(key_size=1024)
    public_key = private_key.public_key()
    return private_key, public_key

# Generate DSA signature
def generateDSASign(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        hashes.SHA256()
    )
    return signature

# Verify DSA signature
def DSAVerify(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Main function
def final():
    # Generate RSA key pair
    RSAprivatekey, RSApublickey = generateRSAkeyPair()

    # RSA Encryption and Decryption
    plain = 'Message for RSA algorithm'
    cipherText = RSAencrypt(RSApublickey, plain.encode('utf-8'))
    decryptedText = RSADecrypt(RSAprivatekey, cipherText)

    # Print RSA data
    RSA_data = [RSApublickey, RSAprivatekey, plain.encode('utf-8'), cipherText, decryptedText]
    for i in RSA_data:
        print(i)

    # Generate DSA key pair
    DSAPrivateKey, DSAPublicKey = generateDSAKEYpair()

    # Generate DSA signature
    message = 'MESSAGE FOR DSA algorithm'
    signature = generateDSASign(DSAPrivateKey, message)

    # Verify DSA signature
    verified = DSAVerify(DSAPublicKey, message, signature)

    # Print DSA data
    DSA_data = [DSAPublicKey, DSAPrivateKey, message, signature, verified]
    for i in DSA_data:
        print(i)

# Call the final function
print('The final code is:')
final()
