import os
from cryptography.fernet import Fernet

def generateIV():
	iv1 = os.urandom(16)
	iv2 = os.urandom(8)
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'IV.txt'),'wb')
	f.write(iv1)
	f.write(b"::::")
	f.write(iv2)
	f.close()
	return iv1,iv2

def generateKey():
	k1 = os.urandom(16)
	k2 = Fernet.generate_key()
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'k1.txt'),'wb')
	f.write(k1)
	f.close()
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'k2.txt'),'wb')
	f.write(k2)
	f.close()
	return k1,k2

def FetchIV():
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'IV.txt'),'rb')
	cont=f.read()
	f.close()
	iv=cont.split(b"::::")
	return iv

def FetchKey():
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'k1.txt'),'rb')
	k1=f.read()
	f.close()
	f=open(os.path.join(os.getcwd()+"/Keys_IV",'k2.txt'),'rb')
	k2=f.read()
	f.close()
	return k1,k2
