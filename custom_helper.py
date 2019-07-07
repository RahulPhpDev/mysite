from cryptography.fernet import Fernet
import db as database


key = "fhC576CfhiMUzgW62L619d4BWSS95fxSAzbSuQffmq0="
def encryptPassowrd(text): 
   cipher_suite = Fernet(key)
   byteText =  bytes(text, encoding="utf-8")
   # print(st)
   cipher_text = cipher_suite.encrypt(byteText)
# #    plain_text = cipher_suite.decrypt(cipher_text)
   return cipher_text 


def decryptPassowrd(password):
   cipher_suite = Fernet(key)
   # uncipher_text = (cipher_suite.decrypt('fsfs'))
   # txt = bytes(uncipher_text).decode("utf-8")
   # print(txt) 
   passw = password
   strr= b'gAAAAABdH02ohJ9TMm0WJD93rSh0PiYhXjadFGmimV3DSmtcJSNU8U4rOIXlYiBYSpDmvZ4E6RdhBsBd51IGgmQuLUWUb-qveQ=='
   print(type(strr))   
   print("Yorker")
   print(type(passw))
   uncipher_text = (cipher_suite.decrypt(passw))
   # plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
   print(uncipher_text)
   # return plain_text_encryptedpassword 


   # key = 'z7oCVMrxjjgx3n1HFI9oCkyxMnOrXekYKNMEBDKF704='
   # cipher_text = b'12345'
   # cipher_suite = Fernet(key)
   # decrypt_result = cipher_suite.encrypt(cipher_text)
   # print(decrypt_result)


def getSequenceNumber(field):
   seq = database.DB['counter'].find_one_and_update(
      {'_id':field},
      {'$inc':{'value':1}},
   )
   return int(seq['value'])