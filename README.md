py3TCP
=====
About
-----
It is simple asynchronous Python 3 TCP server. 


Environment
----------
Python >= 3.5


Usage
-----
Server:
```
$ sudo python3 py3TCP.py -p 25000 -l py3TCP.log
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

TODO
-----
1.Make this project an installable package.
2.Add test cases, and use travis.io for continuous testing.
