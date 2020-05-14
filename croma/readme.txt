// Start Development Server (2 options)
1. Create "Run" Configuration
2. "python3 app.py"


Flask Server File Layout:
--|croma.wsgi           **main WSGI file (for apache2 server)
--|app.py               **main file
--|socket_server.py     **Socket Server, run separately
--|*.py                 **Server files
--|templates            **HTML files
------|layout           **Files for main HTML structure
----------|head.html    **(bootstrap, meta, favicon, etc.)
----------|navbar.html
----------|footer.html  **main footer and javascript
------|*.html
--|static               **CSS, Javascript, Images, etc.
------|css
----------|bootstrap    **Bootstrap 4.4.1 CSS Files
------|javascript
----------|bootstrap    **Bootstrap 4.4.1 JS Files
------|images
------|favicon.ico


// Start WeBots Stream
"webots --stream=port=2222;"

// Use of socket_client.py example
// Import socket_client states that socket_client.py
// should be in the same folder as the file accessing it
import json
import time
import socket_client
# set origin
socket_client.origin = 'webots'
# start listening to specified address
socket = socket_client.SocketClient("ws://localhost:4444")
# allow time for handshake before sending data
time.sleep(0.025)
# example send data
msg = json.dumps(
    {'origin': 'webots',
      'data':
      {
          'example1': 'value1',
          'example2': 'value2'
      }
    }, separators=(',', ':')
)
if socket.isConnected():
    socket.send(msg)


// Start Socket Server
"python3 socket_server.py"

/* Socket Server JSON Criteria */
// Prone to change in future updates
{
    origin: 'origin'                    **Origin of message (server, webots, client, etc.)
    data: 
    {
        property1: 'property1_value',   **Property Name and Value
        property2: 'property2_value'
        **etc.
    }
}
