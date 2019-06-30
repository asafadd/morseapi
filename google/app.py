import os

from flask import Flask
from flask import request
from index import translate_morse

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def translate_request():    
    result = translate_morse(request.args)
    return result

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))