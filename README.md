# Simple-Web-Server
Using Python to create an HTTP server. The program can serve a single html file on a specified port. It can be run on the command line or imported into another program. 

<h1>What is HTTP?</h1>
HTTP is a stateless request/response protocol. To display a web page, the client sends a request to the server, which in turn sends the page back to the client. The client then displays the page.

<h1>What is a web server?</h1>

* A web server is a program that runs on a computer and responds to requests from web browsers of the client. 
* The web server is responsible for receiving the request from the client, processing the request, and sending the response back to the client. 
* The web server is also responsible for maintaining the state of the server. For example, the web server can store the state of the server, such as the current date and time. 
* The web server can also store the state of the client, such as the cookies that the client sends to the server.

<h1>What is a port?</h1>
Web servers use ports to listen for incoming requests. The port number is a number that the server uses to identify itself. The two standard ports used by web servers to connect with web clients are 80 and 443. 

<h1>Requirements</h1>

* Python 3.6 or later

<h1>Usage</h1>

* To start the server, run the following command:

```
python3 server.py
```

* To specify html file, use the following command:

```
python3 server.py path/to/file.html
```

* To specify both port and html file, use the following command:

```
python3 server.py path/to/file.html port_number
```

* To stop the server, use the following key combination: <code>Ctrl + C</code>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
