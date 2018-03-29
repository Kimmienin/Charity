from ftplib import FTP

ftp = FTP('jeangourd.com')
ftp.login("anonymous","");
data = []
 
ftp.dir(data.append)
 
ftp.quit()
 
for line in data:
    print ("-", line)
    
