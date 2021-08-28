from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import sys
import json
import urllib.parse
import threading


ruta = {}
messages = ['Hola', 'Pero hpta']
ruta['messages'] = messages


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content_type', 'application/json')
        self.end_headers()
        jsonFile = json.dumps(ruta)
        self.wfile.write(jsonFile.encode())

    def do_POST(self):
        try:
            content_len = int(self.headers.get('content-length'))
            post_body = self.rfile.read(content_len)
            data = json.loads(post_body)

            parsed_path = urllib.parse.urlparse(self.path)
            self.send_response(200)
            self.end_headers()
            print(data['text'])
            if not messages[len(messages)-1] == data['text']:
                messages.append(data['text'])
                ruta['messages'] = messages
            self.wfile.write(json.dumps({
                'method': self.command,
                'path': self.path,
                'real_path': parsed_path.query,
                'query': parsed_path.query,
                'request_version': self.request_version,
                'protocol_version': self.protocol_version,
                'body': data
            }).encode())
            return

        except:
            self.send_error(404, "{}".format(sys.exc_info()[0]))
            print(sys.exc_info())


def main():
    PORT = 8000
    server = HTTPServer(('localhost', PORT), helloHandler)
    print(f'server running on port {PORT}')
    threads = []
    tServer = threading.Thread(target=server.serve_forever)
    threads.append(tServer)
    tServer.start()


if __name__ == "__main__":
    main()
