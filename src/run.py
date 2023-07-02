from web._init_ import app
from gevent import pywsgi


app.run(host = "0.0.0.0", debug=False,port=5002) #debug mode, port is 5002

# if __name__ == '__main__':
#     server = pywsgi.WSGIServer(('0.0.0.0',5002),app)
#     server.serve_forever()