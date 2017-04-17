#!/usr/bin/python3
from socket import *
import asyncio
import argparse
import logging

class py3TCP:
	"""Implements a simple TCP server."""
	def __init__(self,port,logfile):
		"""Initialize event loop for TCP server.
		Initialize logfile.

		:param port: int, define the port to bind.
		:param logfile: string, define the log file name.
		"""
		def init_log(logfile):
			# create logger
			logger_name = "py3TCP"
			self.logger = logging.getLogger(logger_name)
			self.logger.setLevel(logging.INFO)

			# create formatter
			fmt = "%(asctime)-15s %(levelname)s %(message)s"
			datefmt = "%Y-%m-%d %H:%M:%S"
			formatter = logging.Formatter(fmt, datefmt)

			# create file handler
			fh = logging.FileHandler(logfile)
			fh.setLevel(logging.INFO)
			fh.setFormatter(formatter)

			# create stream handler
			sh = logging.StreamHandler(stream=None)
			sh.setLevel(logging.INFO)
			sh.setFormatter(formatter)

			# add handler and formatter to logger
			self.logger.addHandler(fh)
			self.logger.addHandler(sh)

		self.loop = asyncio.get_event_loop()
		self.core = asyncio.start_server(self.TCP_handler,'127.0.0.1',port, loop=self.loop)
		init_log(logfile)

	async def TCP_handler(self,reader,writer):
		"""Handle TCP Connection.
		Receives bytes from the clients and responds to the clients with the number of bytes received
		:param reader: It's used to read data from the client.
		:param writer: It's used to send data to the client.
		"""
		peername = writer.get_extra_info('peername')
		self.logger.info("Connection from {}.".format(peername))
		data = await reader.readline()
		datalen = len(data.strip(b'\n').strip(b'\r'))
		self.logger.info("Received {} bytes from {}.".format(datalen,peername))
		writer.write(str.encode(str(datalen)+'\n'))
		writer.close()
		self.logger.info("Connection from {} was terminated.".format(peername))

	def start(self):
		"""Start the py3TCP server."""
		try:
			self.server = self.loop.run_until_complete(self.core)
			self.logger.info("Serving on {}.".format(self.server.sockets[0].getsockname()))
			self.loop.run_forever()
		except Exception as e:
			self.logger.error("An error occured: {}".format(e))

	def close(self):
		"""Close the py3TCP server."""
		self.server.close()
		self.loop.run_until_complete(self.server.wait_closed())
		self.loop.close()

def main():
	parser = argparse.ArgumentParser(description="Python 3 TCP server.")
	parser.add_argument("-p", "--port", default=25000, help="Port to listen", type=int)
	parser.add_argument("-l", "--logfile", default="py3TCP.log", help="logfile name")
	args = parser.parse_args()

	TCPserver = py3TCP(args.port,args.logfile)
	try:
		TCPserver.start()
	except KeyboardInterrupt:
		pass
	finally:
		TCPserver.close()

if __name__ == '__main__':
	main()
