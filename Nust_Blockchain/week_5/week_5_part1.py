import hashlib

# this code snippet is for part_1
# Function for hash calcualtion

def hashed(value):
    return hashlib.sha256(value.encode()).hexdigest();


# function for concatenation

def concatenate(a,b,c,d,e):
    return a+b+c+d+str(e)
    

# Main Function

def assesment(Senders_email_address ,recipient_email_address,email_subject,message_body,Nonce):
    
    
   Attempts=0;

   while True:
       Attempts=Attempts+1
       concatenated=concatenate(Senders_email_address,recipient_email_address,email_subject,message_body,str(Nonce));
       
       hashed_Str=hashed(concatenated)
    
    #  checking difficulty
       
       if hashed_Str[:2]=='ff':
           return Attempts ,Nonce ,hashed_Str
       else: 
           Nonce=Nonce+1
           
 
 
# getting input from user

sender =input('please provide sender email: \b') 
recipient =input('please provide recipient email : \b') 
subject =input('please provide subject : \b') 
message =input('please provide message :  \b') 
nonce =int(input('please provide nonce :   \b'))
 
           
           
  
  
# calling  Main function

num_attempts,  nonce_found ,hashresult =assesment(sender,recipient,subject,message,nonce);


# outputting result

print('the hash result is:       ' ,hashresult)
print('the number of attempts are :     ' ,num_attempts)
print('the nonce found is:       ' ,nonce_found)





    
    



    
    








