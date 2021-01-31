
import socket


class simulatorAPI:
    def __init__(self):
        bind_ip = '127.0.0.1'
        bind_port = 65432
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((bind_ip, bind_port))
        self.server.listen(5)  # max backlog of connections
        print('Listening on {}:{}'.format(bind_ip, bind_port))
        self.run()



    def run(self):
        self.client_sock, self.address = self.server.accept()
        print('Accepted connection from {}:{}'.format(self.address[0], self.address[1]))
        request = self.client_sock.recv(1024)
        print('Received {}'.format(request.decode('utf-8')))
        self.client_sock.send(b'ACK!')

        data = input("message: ")
        while data != "exit":
            self.client_sock.send(data.encode('utf-8'))
            data = input("message: ")

        self.client_sock.close()

        # client_handler = threading.Thread(
        #     target=self.handle_client_connection,
        #     args=(self.client_sock,)
        #     # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        # )
        # client_handler.start()


if __name__ == '__main__':
    simulatorAPI()