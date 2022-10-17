
import threading
import time
import random


setTimeout_thread = dict()
setInterval_thread = dict()


class setTimeout():

    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.id = random.random()
        self.start()

    def start(self):
        # print (self.id)

        def dosomething() -> None:

            # self.func()
            time.sleep(self.time/1000)
            # print(thread,"thread")
            if (str(self.id) in setTimeout_thread):

               self.func()

        setTimeout_thread[str(self.id)] = threading.Thread(
            target=lambda: dosomething())
        setTimeout_thread[str(self.id)].start()


def clearTimeout(value: setTimeout):

    del setTimeout_thread[str(value.id)]


class setInterval():

    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.id = random.random()
        self.start()

    def start(self):
        # print (self.id)

        def dosomething() -> None:

            self.func()
            time.sleep(self.time/1000)
            # print(thread,"thread")
            if (str(self.id) in setInterval_thread):

                dosomething()

        setInterval_thread[str(self.id)] = threading.Thread(
            target=lambda: dosomething())
        setInterval_thread[str(self.id)].start()


def clearInterval(value: setInterval):

    del setInterval_thread[str(value.id)]

# def
