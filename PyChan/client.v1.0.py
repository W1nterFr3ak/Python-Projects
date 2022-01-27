import sockets
import sys

#check if sufficient parameters are met.
if len(sys.argv) <2:
    print("Usage: client.py ip port ")
    exit()
#banner.
print("\n\t########  ###  ###  ########  ###  ###  ########  ###    ###")
print("\t########  ###  ###  ########  ###  ###  ###  ###  ## #   ###")
print("\t########  ###  ###  ##        ########  ###  ###  ### #  ###    client v1.0")
print("\t########  ########  ##        ########  ########  ###  # ###    by P4rsz and W1nterFr3ak")
print("\t####           ###  ########  ###  ###  ###  ###  ###   # ##    email: parsz@protonmail.com WinterFreak@protonmail.com")
print("\t####      ########  ########  ###  ###  ###  ###  ###    ###\n")
#host and port.

host = sys.argv[1]
port = sys.argv[2]

#connect to host.
client = server.connect((host, port))
data = client.recv(1024)
print("\t",data)
print("\n\tExiting.\n")
exit()
