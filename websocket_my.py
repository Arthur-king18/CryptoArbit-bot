from threading import Thread


class MyThread(Thread):
    def __init__(self, function, name, price_dict):
        super(MyThread, self).__init__()
        self.t = Thread(target=function, args=(name, price_dict, ))
        self.t.start()

