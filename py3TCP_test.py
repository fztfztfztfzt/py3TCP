#!/usr/bin/python3
import unittest
from py3TCP import py3TCP
import socket
import multiprocessing as mp

class Test_py3TCP(unittest.TestCase):
    def test_respond(self):
        def server():
            TCPserver = py3TCP(25000,"py3TCP.log")
            TCPserver.start()
        def client(q):
            TCPclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCPclient.connect(('127.0.0.1', 25000))
            TCPclient.send("Hello Word\n".encode())
            q.put(TCPclient.recv(1024))
            TCPclient.close()
        q = mp.Queue()
        s = mp.Process(target=server)
        c = mp.Process(target=client, args=(q,))
        s.start()
        c.start()
        c.join()
        s.terminate()
        self.assertEqual(q.get(),b'10\n')

    def test_asyncio(self):
        def server():
            TCPserver = py3TCP(25000,"py3TCP.log")
            TCPserver.start()
        def client(q1,q2):
            TCPclient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCPclient1.connect(('127.0.0.1', 25000))
            TCPclient2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCPclient2.connect(('127.0.0.1', 25000))
            TCPclient2.send("Hello Word\n".encode())
            q2.put(TCPclient2.recv(1024))
            TCPclient2.close()
            TCPclient1.send("Hello\n".encode())
            q1.put(TCPclient1.recv(1024))
            TCPclient1.close()

        q1 = mp.Queue()
        q2 = mp.Queue()
        s = mp.Process(target=server)
        c = mp.Process(target=client, args=(q1,q2,))
        s.start()
        c.start()
        c.join()
        s.terminate()
        self.assertEqual(q1.get(),b'5\n')
        self.assertEqual(q2.get(),b'10\n')

if __name__ == '__main__':
    unittest.main()
