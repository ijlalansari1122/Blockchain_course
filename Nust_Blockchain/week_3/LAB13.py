
import hashlib
import random
import random
import hashlib
import ecdsa
from ecdsa import SigningKey, SECP256k1

# generateTXid

def generateTXid():
   
   random_str=str(random.randint(1,1000000) )
   hexadata=hashlib.sha256(random_str.encode()).hexdigest()
   
   return hexadata
   

    
 


# generateinput


def generateInput():
    prevTxid = generateTXid();
    prevOutput =random.randint(0,5);
    
    return prevTxid ,prevOutput;



# generateOutput

def generateOutput():
    
    recipientAddress = 'ijlal ansari' + str(random.randint(1,100));
    amount = round(random.uniform(0.001, 1.0) ,8)


    return recipientAddress , amount;


# transactionFee

def generateTransactionFee():
   return round(random.uniform(0.001 ,1.0) ,8)
    



# RandomTransaction
def  RandomTransaction():
    txid=generateTXid()
    inputPrevTXid , inputPrevOutputIndex = generateInput();
    outputRecipientAddress ,OutputAmount = generateOutput()
    transactionFee =generateTransactionFee();
    return(txid ,inputPrevTXid,inputPrevOutputIndex , outputRecipientAddress ,OutputAmount ,transactionFee);





# Concatenation    #


def concatenateSTR(txid ,inputPrevTxid ,inputPrevOutputIndex ,outputRecipientAddress , outputAmount ,transactionFee):
    transactionData =str(txid) +str(inputPrevTxid)+str(inputPrevOutputIndex) +str(outputRecipientAddress)+str(outputAmount)+str(transactionFee);
    return transactionData;


    # GenerateECDSAKeyPair
    
    
def GenerateECDSAKeyPair():
       ECDSAprivate_key = SigningKey.generate(curve=SECP256k1) 
       ECDSApublic_key = ECDSAprivate_key.get_verifying_key()
       return ECDSAprivate_key, ECDSApublic_key;
   
   
#    ECDSASIGN


def  ECDSAsign(privateKey ,message):
     signature =privateKey.sign(message.encode('utf-8'))
                               
     return signature
 
 
 
#  ECDSAverify


def ECDSAverify(publicKey , message , signature):
    try:
        publicKey.verify(
            signature ,message.encode())
    
        return True
    except  ecdsa.BadSignatureError:
        return False
    
 
 
 
 
#  main 







def main_fn():
    
 inputPrevTxid,txid, inputPrevOutputIndex,outputRecipientAddress, outputAmount,transactionFee = RandomTransaction()
    
 transactionDataASmessage =concatenateSTR(txid,inputPrevTxid,inputPrevOutputIndex,outputRecipientAddress,outputAmount,transactionFee).encode()
 transactionDataAShashed =hashlib.sha256(transactionDataASmessage).hexdigest()  
 
 ECDSAprivatekey , ECDSAPublickey =GenerateECDSAKeyPair()
 signature =ECDSAsign(ECDSAprivatekey,transactionDataAShashed)
 
 verified =ECDSAverify(ECDSAPublickey ,transactionDataAShashed ,signature)

 print('ECDSA:' ,ECDSAPublickey)
 print('ECDSA:' , ECDSAprivatekey)
 print('transactionDataAsMessageSHA256Hashed:',transactionDataAShashed
)
 print('Signature',signature.hex())
 print('Verification:' ,verified)



print('The simulate signing of a bitcoin using Elliptic Curve Digital Signature Algorithm(ECDSA) IS')
main_fn()

    
    
   
  
    
   
  
  
  
   

        
    
     
    
    

    
    
    
    