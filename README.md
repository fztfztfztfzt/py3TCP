py3TCP
=====
[![Build Status](https://travis-ci.org/fztfztfztfzt/py3TCP.svg?branch=master)](https://travis-ci.org/fztfztfztfzt/py3TCP)

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
2017-04-17 09:51:06 INFO Serving on ('127.0.0.1', 25000).
2017-04-17 09:51:19 INFO Connection from ('127.0.0.1', 52731).
2017-04-17 09:51:26 INFO Connection from ('127.0.0.1', 52732).
2017-04-17 09:51:32 INFO Received 11 bytes from ('127.0.0.1', 52731).
2017-04-17 09:51:32 INFO Connection from ('127.0.0.1', 52731) was terminated.
2017-04-17 09:51:37 INFO Received 5 bytes from ('127.0.0.1', 52732).
2017-04-17 09:51:37 INFO Connection from ('127.0.0.1', 52732) was terminated.
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
