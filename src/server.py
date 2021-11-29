"""
A quick demonstration of a simple HTTP server 
using the built-in Python libraries.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path
from pathlib import Path
import sys

DEFAULT_PORT = 8110
DEFAULT_HTML_PATH = "index.html"


class SimpleWebServer(BaseHTTPRequestHandler):
    """
    A simple web server that serves html pages.
    """

    html_file_path = Path(__file__).parent.absolute() / DEFAULT_HTML_PATH

    def do_GET(self) -> None:
        """
        Override the do_GET method to handle the GET requests
        and send the file to the client if it exists. If the
        file does not exist, send a 404 error.
        """
        try:
            html_file_content = open(__class__.html_file_path).read()
            self.send_response(200)
        except:
            html_file_content = "File not found"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(html_file_content, "utf-8"))


if __name__ == "__main__":

    port = DEFAULT_PORT
    html_file_path = DEFAULT_HTML_PATH
    
    if len(sys.argv) == 1:
        print(
            f"Using default html file path: {DEFAULT_HTML_PATH} and a default port: {DEFAULT_PORT}"
        )

    elif len(sys.argv) == 2 or len(sys.argv) == 3:
        html_file_path = sys.argv[1]
        if not path.exists(html_file_path):
            print(f"File {html_file_path} does not exist")
            exit()

        if len(sys.argv) == 3:
            port = int(sys.argv[2])
            if port < 0 or port > 65535:
                print(f"Port {port} is not valid")
                exit()

    else:
        print("Usage: python server.py [html_file_path] [port]")
        exit()

    httpd = HTTPServer(("localhost", port), SimpleWebServer)
    httpd.RequestHandlerClass.html_file_path = html_file_path
    httpd.serve_forever()
    print(f"Serving HTTP on port {port}...")
