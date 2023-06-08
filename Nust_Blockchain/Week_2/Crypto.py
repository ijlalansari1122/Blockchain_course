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
     cipher_Text= public_key.encrypt(
       plain_Text,
       padding.OAEP(
        mgf=MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None  
       )
     )
     return cipher_Text;
 
     
     
 # function RSADecrypt(privateKey , cipherText);
 
 
def RSADecrypt(privateKey ,cipherText):
     plainText =privateKey.decrypt(
         cipherText,
         padding.OAEP(
             mgf=MGF1(algorithm=hashes.SHA256()),
             algorithm=hashes.SHA256(),
             label=None
         ) 
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
    
    signature =privateKEY.sign(
        message.encode('utf-8'),
        hashes.SHA256()),
    return signature;



# function DSAVerify(publicKEY , message ,signature)


def DSAVerify(publicKEY , message ,signature):
    
    try:
        publicKEY.verify(signature ,
              signature,
              message.encode('utf-8'),
              hashes.SHA256()               
                             
                             
        )    
        return True
    except:
        return False   
     
            


#---------------------------------main-function---------------------------------------------#


def final():
    # first call
    RSAprivatekey ,RSApublickey = generateRSAkeyPair()
    
    # second call
    
    plain = 'Message for RSA algorithm'
    
 
    cipherText = RSAencrypt(RSApublickey,plain.encode('utf-8')) 
     
     
    # third call
    
    decryptedText =RSADecrypt(RSAprivatekey, cipherText )
    
    
    # part_1 printing
    
    RSA_data= [RSApublickey, RSAprivatekey  ,cipherText,decryptedText]
    
    for i in RSA_data:
         print(i);
         
         
         
        #-----------------------------------------dsa part fn calls--------------------------------------#  
        #  part -1
         DSAPrivateKey ,DSAPublicKey=generateDSAKEYpair()
         
        #  part-2
        
         message = 'MESSAGE FOR DSA algorithm'
         
         
         signature= generateDSASign(DSAPrivateKey,message)
         
         
         verified = DSAVerify(signature ,message ,DSAPublicKey)
         
         
    RSA_data= [DSAPublicKey, DSAPrivateKey , message ,signature,verified]
         
    for i in RSA_data:
            print(i) 
             
         
         
         
         
         
         
print('the MESSAGE RSA AND DSA IS ' )
final() 


