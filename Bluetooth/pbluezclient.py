import bluetooth

serveraddr = 'DC:A6:32:F7:3B:04'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serveraddr, port))

while 1:
	text = input()
	if text == 'quit':
		break
	s.send(text)

sock.close()

