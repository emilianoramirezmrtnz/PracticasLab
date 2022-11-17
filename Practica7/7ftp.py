from ftplib import FTP
import re

ftp = FTP('ftp.us.debian.org')  
ftp.login()                    
ftp.cwd('debian')               

ftp.retrlines('LIST')
filelist = ftp.nlst()

for element in filelist:
    if re.findall('.txt', element) or re.findall('.msg', element) or re.findall('readme', element, re.IGNORECASE):
        print("Se está descargando" + str(element))
        with open('C:\\Users\\elias\\Documents\\chapo\\'+element, 'wb') as fp:
            ftp.retrbinary('RETR '+element, fp.write)
ftp.quit()