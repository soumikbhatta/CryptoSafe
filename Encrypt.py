from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
def AES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","0.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Parts","0.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"/Parts","0.txt"),"wb")
    f.write(cont)
    f.close();

def BlowFish(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","1.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Parts","1.txt"),"w").close()
    f=open(os.path.join(os.getcwd()+"/Parts","1.txt"),"wb")
    f.write(cont);
    f.close();


def TrippleDES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","2.txt"),"r");
    content=f.read();
    f.close();
    content=content.encode()
    b=len(content);
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content);
    backend = default_backend();
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend);
    encryptor = cipher.encryptor();
    cont = encryptor.update(content) + encryptor.finalize();
    open(os.path.join(os.getcwd()+"/Parts","2.txt"),"w").close();
    f=open(os.path.join(os.getcwd()+"/Parts","2.txt"),"wb");
    f.write(cont);
    f.close();

def IDEA(key,iv):
	f=open(os.path.join(os.getcwd()+"/Parts","3.txt"),"r")
	content=f.read()
	f.close()
	content=content.encode()
	b=len(content)
	if(b%8!=0):
		while(b%8!=0):
			content+=" ".encode()
			b=len(content)
	backend = default_backend()
	cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv), backend=backend)
	encryptor = cipher.encryptor()
	cont = encryptor.update(content) + encryptor.finalize()
	open(os.path.join(os.getcwd()+"/Parts","3.txt"),"w").close()
	f=open(os.path.join(os.getcwd()+"/Parts","3.txt"),"wb")
	f.write(cont)
	f.close()

def EFernet(key):
    f=open(os.path.join(os.getcwd()+"/Parts","4.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    fer = Fernet(key)
    content=fer.encrypt(content)
    open(os.path.join(os.getcwd()+"/Parts","4.txt"),'w').close()
    f=open(os.path.join(os.getcwd()+"/Parts","4.txt"),"wb")
    f.write(content)
    f.close()

def CryptKeys():
    key = Fernet.generate_key()
    f=open('Secured.txt','wb')
    f.write(key)
    f.close()
    listDir=os.listdir(os.getcwd()+"/Keys_IV")
    fer = Fernet(key)
    for i in listDir:
        KI=open(os.getcwd()+'/Keys_IV//'+i,'rb')
        content=KI.read()
        KI.close()
        content=fer.encrypt(content)
        open(os.path.join(os.getcwd()+"/Keys_IV",i),'wb').close()
        f=open(os.path.join(os.getcwd()+"/Keys_IV",i),"wb")
        f.write(content)
        f.close()


