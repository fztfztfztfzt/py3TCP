py3TCP
=====
About
-----
* It is a simple Python 3 TCP server.
* It can receive bytes from clients and after this it can respond to the clients with the number of bytes received and terminate the connection to the client.
* The server can handle multiple concurrent TCP connections.

Environment
----------
Python >= 3.5

Install
-------
```bash
$ git clone https://github.com/fztfztfztfzt/py3TCP
$ cd py3TCP
$ sudo python3 setup.py install
```

Usage
-----
Server:
```
$ sudo py3TCP -p 25000 -l py3TCP.log
Thu 13 Apr 2017 17:56:38 INFO Serving on ('127.0.0.1', 25000).
Thu 13 Apr 2017 17:56:41 INFO Connection from ('127.0.0.1', 53720).
Thu 13 Apr 2017 17:56:44 INFO Connection from ('127.0.0.1', 53721).
Thu 13 Apr 2017 17:56:56 INFO Received 11 bytes from ('127.0.0.1', 53720).
Thu 13 Apr 2017 17:57:02 INFO Received 5 bytes from ('127.0.0.1', 53721).
```

Client1:
```
$ netcat 127.0.0.1 25000
Hello Wrold
11
```

Client2:
```
$ netcat 127.0.0.1 25000
Hello
5
```

Running tests
-------------
```python3
python3 -m unittest py3TCP_test
```

TODO
-----
Add test cases, and use travis.io for continuous testing.
