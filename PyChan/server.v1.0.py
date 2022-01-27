import socket
import sys

#check if sufficient parameters are met.
if len(sys.argv) <2:
    print("Usage: server.py ip port ")
    exit()

#banner.
print("\n\t########  ###  ###  ########  ###  ###  ########  ###    ###")
print("\t########  ###  ###  ########  ###  ###  ###  ###  ## #   ###")
print("\t########  ###  ###  ##        ########  ###  ###  ### #  ###    server v1.0")
print("\t########  ########  ##        ########  ########  ###  # ###    by P4rsz and W1nterFr3ak")
print("\t####           ###  ########  ###  ###  ###  ###  ###   # ##    email:parsz@protonmail.com,WinterFreak@protonmail.com")
print("\t####      ########  ########  ###  ###  ###  ###  ###    ###\n")

#port and host
host = str(sys.argv[1])
port = int(sys.argv[2])

#server object, binding.
server = socket.socket(socket.AF_INET)
server.bind((host, port))

#accept connections
while True:
    try:
        #listen for connections
        print(f"[-] Listening on {host} : {port}")
        server.listen(10)
        #accept incoming connections, send a welcome message, notify us of the connection then close connection.
        conn, addr = server.accept()
        conn.send(b' Welcome to the server')
        print(f"[-] {addr} connected.")
        conn.close()
        exit()
    #handle interrupts.
    except KeyboardInterrupt:
        print("\n\tExiting")
        exit()
