import zmq

server = "tcp://127.0.0.1:9988"

context = zmq.Context()
sock = context.socket(zmq.SUB)

prefix = "worker1"
sock.setsockopt(zmq.SUBSCRIBE, prefix)
sock.connect(server)

print "subcribed to %s and listening for %s" % (server, prefix)

while True:
    message = sock.recv()
    print message
