import threading


class BuckyMessenger(threading.Thread):
    def run(self):
       for _ in range(10):
           print(threading.currentThread().getName())

x=BuckyMessenger(name='Send out messages')
y=BuckyMessenger(name='Receive messages')
x.start()
y.start()

