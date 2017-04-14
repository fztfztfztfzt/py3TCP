from setuptools import setup

setup(
      name="py3TCP",
      version="1.1",
      description="A simple python3 TCP server application",
      author="Polaris Feng",
	  author_email='fztfztfztfzt@gmail.com',
      url="https://github.com/fztfztfztfzt/py3TCP",
	  scripts=["py3TCP.py"],
	  entry_points={
        'console_scripts':[
            'py3TCP=py3TCP:main' 
        ]
		},
      )