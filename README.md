URL shortening

project dependencies
**********************************
python3
pip3
flask
flask-restful
*****************************

Installation
*************************************
https://www.python.org/downloads/release/python-387/
https://pip.pypa.io/en/stable/installing/

Setup environment
**************************
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip3 install flask-restful

To start project
*****************************
open a terminal
cd into the cloned directory:

Enter:
python main.py

From another terminal You can test the Url Web Service

Step 1) 

To encode a url, enter a url like the following format:
curl http://localhost:5000/encode -d "url=https://myanimelist.net/anime/40028/Shingeki_no_Kyojin__The_Final_Season"

Step 2)

To decode the url, Use the sample request below and replace http://short.com/UB4fH4 with the response give from Step 1


curl http://localhost:5000/decode -d "url=http://short.com/UB4fH4"


Time Spent:
20 mins to install python, pip, 

20 mins to plan project, framework, etc.

30 mins to create and test algorithm

20 mins to integrate into  a web service using flask and flask-restful

