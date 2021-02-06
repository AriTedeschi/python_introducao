class Queue:
    def __init__(self):
        self.data = list()

    def remove(self):
        try:
            return self.data.pop(0)
        except IndexError:
            print('Empty Queue!')

    def insert(self, e):
        self.data.append(e)

    def whoIsNext(self):
        try:
            return self.data[0]
        except IndexError:
            print('Empty Queue!')

    def showQueue(self):
        try:
            for e in self.data:
                print(e)
        except IndexError:
            print('Empty Queue!')
    

if __name__ == '__main__':
    q = Queue()
    q.showQueue()
    print('\n\n')
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(1)
    q.showQueue()
    print('\n Remove: {}'.format(q.remove()))
    q.showQueue()
    print('\n Next: {}'.format(q.whoIsNext()))
    q.showQueue()