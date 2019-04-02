from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import image_processing


class ProcessingHandler(FTPHandler):
    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        print("%s Disconnected" % self.username)

    def on_login(self, username):
        print("%s has logged in" % username)

    def on_logout(self, username):
        print("%s has logged out" % username)

    def on_file_sent(self, file):
        print("%s has sent %s " % (self.username, file))

    def on_file_received(self, file):
        print("Received %s from %s" % (file, self.username))
        image_processing.process_image(file)

    def on_incomplete_file_received(self, file):
        print("Received incomplete file from %s" % self.username)

    def on_incomplete_file_sent(self, file):
        print("%s Sent incomplete file" % self.username)


if __name__ == "__main__":
    authorizer = DummyAuthorizer()
    authorizer.add_user("webcam", "1234", "./ToProcess", perm="lw")
    handler = ProcessingHandler
    handler.authorizer = authorizer
    server = FTPServer(('0.0.0.0', 21), handler)
    logging.basicConfig(filename='./log/pyftpd.log', level=logging.INFO)  # Store FTP server log
    server.serve_forever()




