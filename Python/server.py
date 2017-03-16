import zmq

listen = "tcp://127.0.0.1:9988"

context = zmq.Context()
sock = context.socket(zmq.REP)
sock.bind(listen)

print("listening on %s " % listen)

while True:
    message = sock.recv()
    print message
    sock.send("hello %r " % message)
