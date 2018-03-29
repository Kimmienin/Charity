from ftplib import FTP
import sys

ftp = FTP('jeangourd.com')
ftp.login("anonymous","");
data = []
 
ftp.dir()
 
ftp.quit()
