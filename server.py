import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer
from search import *

hostName = "localhost"
serverPort = 5000

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get_content_type())

        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        reqBody = json.loads(self.rfile.read(length))
        
        # # add a property to the object, just to mess with data
        # message['received'] = 'ok'
        # print(message)
        # end the message back
        message = {}
        message['courses'] = searchCourse(reqBody["result"],reqBody["type"])
        message["count"] = len(message["courses"])
        self._set_headers()
        self.wfile.write(bytes(json.dumps(message),"utf-8"))
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")