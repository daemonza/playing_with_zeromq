### Playing with zeromq

Sandbox repo used for using Go and Python to play with zeromq

#### Dependencies

On the Python2 side :

```
pip install -r requirements.txt
```

On the Go side :
```
go get github.com/zeromq/goczmq
```

#### sub / pub

Start the publisher with :
```
python Python/pub.py
```
This will bind to tcp://127.0.0.1:8899

The subscribers will connect to tcp://127.0.0.1:8899
Start the Python subscriber with :
```
python Python/sub.py
```
Start the Go subscriber with : 
```
go run Go/sub/main.go
```
