from ftplib import FTP
import sys

ftp = FTP('jeangourd.com')
ftp.login("anonymous","");
data = []
perm = []
perm2 = []
binary = []
binaryMessage = "";
ftp.dir(data.append)


i = 0
j = 0
for line in data:
    perm.append(data[i][:10])   
    i += 1

for line in perm:
    print(line)             #### this is just to prints the permissions

for line in perm:
    binary.append("")
    for a in perm[j]:
        if a == '-':
            binary[j]+= "0"
        else:
            binary[j]+= "1"
    j += 1

for line in binary:         #### this is just to print the binary
    print(line)

for line in binary:             
    binaryMessage += line


if(len(binaryMessage) % 7 == 0): # If code is 7-bit
    for i in range(0, (len(binaryMessage)/7)):
        sys.stdout.write(chr(int(binaryMessage[i*7:i*7+7], base=2))), # convert to ASCII(int(String[position: position+7], in binary))
    print('')

elif(len(binaryMessage) % 8 == 0): #if code is 8-bit
    for i in range(0, (len(binaryMessage)/8)):
        sys.stdout.write(chr(int(binaryMessage[i*8:i*8+8], base=2))), # convert to ASCII(int(String[position: position+8], in binary))
    print('')

    
    
ftp.quit()
