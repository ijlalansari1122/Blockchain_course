# importing important modules for task
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15, MGF1
from cryptography.hazmat.primitives import padding as symmetric_padding


# function generateRSAkeyPair():


def generateRSAkeyPair():
    # private key
    private_key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    # public key
    public_key=private_key.public_key()
       
    return private_key ,public_key;



# function RSAEncrypt(publicKEY , plaintext)



def RSAencrypt(public_key,plain_Text ):
     publickey=serialization.load_pem_public_key(public_key)
    
     cipher_Text= publickey.encrypt(
       plain_Text.encode('utf-8'),
       padding.PKCS1v15()  

     )
     return cipher_Text;
 
     
     
 # function RSADecrypt(privateKey , cipherText);
 
 
def RSADecrypt(privateKey ,cipherText):
       
     private_key =serialization.load_pem_private_key(privateKey ,password=None)
     
     plainText =private_key.decrypt(
         cipherText,
         padding=PKCS1v15() 
     )     
     
     return plainText.decode('utf-8');
     
     
  
  
  
  
  
  
#   ----------------------------------------------part_2 starts from here --------------------------------------------------------------------
  
  #  function generateDSAKeypair

  
  
def  generateDSAKEYpair():
      
      privateKey=dsa.generate_private_key(key_size=1024)
      
      publicKey=privateKey.public_key()
      
      return privateKey , publicKey;
  
  
  
  #  function generateDSAsign
  
  
def generateDSASign(privateKEY ,message):
    
    private_KEY=serialization.load_pem_private_key(privateKEY ,password=None)
    
    signature =private_KEY.sign(
        message.encode('utf-8'),
        padding.PSS(
            js=padding.MGF1(hashes.SHA256()),
            signlenght =padding.MGF1.MAX_LENGTH
    
        ),
        hashes.SHA256
    )
    return signature;



# function DSAVerify(publicKEY , message ,signature)


def DSAVerify(publicKEY , message ,signature):
        public_KEY = serialization.load_pem_public_key(publicKEY)
        
        message_value=hashes.SHA256()
        encoded= message.encode('utf-8')
        message_value.update(encoded)
        final_message=message_value.finalize()
        
        if public_KEY.verify(signature ,final_message):
            return True
        else: False
            


#---------------------------------main-function---------------------------------------------#


def final():
    # first call
    RSAprivatekey ,RSApublickey = generateRSAkeyPair()
    
    # second call
    
    plain = 'Message for RSA algorithm'
    plainText =plain.encode('utf-8')
 
    cipherText = RSAencrypt(9211,plain) 
     
     
    # third call
    
    decryptedText =RSADecrypt(cipherText)
    
    
    # part_1 printing
    
    RSA_data= [RSApublickey, RSAprivatekey , plainText ,cipherText,decryptedText]
    
    for i in RSA_data:
         print(i);
         
         
         
        #-----------------------------------------dsa part fn calls--------------------------------------#  
        #  part -1
         DSAPrivateKey ,DSAPublicKey=generateDSAKEYpair()
         
        #  part-2
        
         message = 'MESSAGE FOR DSA algorithm'
         message.encode('utf-8');
         
         
         signature= generateDSASign(12412,message)
         
         
         verified = DSAVerify(signature)
         
         
    RSA_data= [DSAPublicKey, DSAPrivateKey , message ,signature,verified]
         
         
         
         
         
         
         
         
print('the final code is' + final()) 


