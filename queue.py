"""Queue Module"""
class Queue():
    """"class"""
    def __init__(self):
        self.data = []
        self.max_size = 10

    def push(self, value):
        """"class"""
        if not self.is_full():
            self.data.append(value)
        else:
            print("queue full")

    def data_reverse(self):
        """"class"""
        self.data.reverse()
        print(self.data)

    def pop(self):
        """"class"""
        if self.is_empty() is False:
            return  self.data.pop(0)
        print("queue empty ")
        return None

    def is_empty(self):
        """"class"""
        if len(self.data) == 0:
            return True
        return False

    def is_full(self):
        """"class"""
        if len(self.data) == self.max_size:
            print(len(self.data))
            return True

        return False

    def display_queue(self):
        """"class"""
        print(self.data)
obj = Queue()
for i in range(10):
    obj.push(i)
obj.data_reverse()

obj.display_queue()

for i in range(5):
    obj.pop()

obj.display_queue()
obj.data_reverse()
