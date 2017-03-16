import zmq
import time

listen = "tcp://127.0.0.1:9988"
context = zmq.Context()
sock = context.socket(zmq.PUB)
sock.bind(listen)

while True:
    now = time.ctime()

    print "sending for worker1 : %r" % now
    sock.send("worker1:" + now)

    print "sending for worker2 : %r" % now
    sock.send("worker2:" + now)

    time.sleep(3)
