from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import session
import random
import string

app = Flask(__name__)
api = Api(app)


#store variables global, so the data isn't lost between reqeust
url2code = {}
code2url = {}

#this class It produces short URLs like http://short.com/KtLa2U, using a random code of six digits or letters. 
# If a long URL is already known, the existing short URL is used and no new entry is generated.
class Url():
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in url2code:
            code = ''.join(random.choice(Url.alphabet) for _ in range(6))
            if code not in code2url:
                code2url[code] = longUrl
                url2code[longUrl] = code
        return 'http://short.com/' + url2code[longUrl]

    def decode(self, shortUrl):
            return code2url[shortUrl[-6:]]

#Web service to encode url
class EncodeUrl(Resource):
    def post(self):
        url = Url()  
        parser = reqparse.RequestParser()
        parser.add_argument('url')
        args = parser.parse_args()
        return url.encode(args.url)

#Web service to decode url
class DecodeUrl(Resource):
    def post(self):
        url = Url()  
        parser = reqparse.RequestParser()
        parser.add_argument('url')
        args = parser.parse_args()  
        return url.decode(args.url)


#The Service endpoints
api.add_resource(EncodeUrl, '/encode')    

api.add_resource(DecodeUrl, '/decode')    

if __name__ == '__main__':
    app.run(debug=True)  

    