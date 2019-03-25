from ftplib import FTP

ftp = FTP('')

def connectToServer(host, port):
    ftp.connect(host, port)
    ftp.login(user="name", passwd="123")


def getFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

connectToServer('ip_addr',21)
getFile("file.txt")