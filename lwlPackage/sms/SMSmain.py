from twilio.rest import Client 


account_sid = 'AC988415bd476b4abc248b4afaa8bc6717' 
auth_token = '3b62cb9653d077b61f0d1f50bc06e718' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                            from_='+13343423628',    
                            body='asdf',      
                            to='+8617742566640' 
                          ) 
 
print(message.sid)