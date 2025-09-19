from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
        <h1 align="center">
            DEVICE SPECIFICATION-25016839
        </h1>
        <table border="2" align="center" cellspacing="20" cellpadding="20">
        <tr>
            <th>S.NO</th>
            <th>device specification</th>
            <th>description</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>storage</td>
            <td>954GB</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Graphics card</td>
            <td>128MB</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>RAM</td>
            <td>16GB</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Gen</td>
            <td>13</td>
        </tr>
        <tr>
            <td>5.</td>
            <td>processor</td>
            <td>i7-13620H</td>
        </tr>
        </table>

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()