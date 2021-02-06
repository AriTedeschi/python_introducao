class Stack:
    def __init__(self):
        self.data = list()

    def remo(self):
        try:
            re = self.data.pop(len(self.data)-1)
        except IndexError:
            print('Empty Stack!')
        else:
            return re

    def push(self, e):
        self.data.append(e)

    def stacktop(self):
        try:
            return self.data[len(self.data)-1]
        except IndexError:
            print('Empty Stack!')
    

if __name__ == '__main__':
    s = Stack()
    print(s.stacktop())
    s.push(1)
    print('\n\n Push {}'.format(s.stacktop()))
    s.push(2)
    print(s.stacktop())
    print('\n Pop: {}'.format(s.pop()))
    print('\n Pop: {}'.format(s.pop()))
    print(s.stacktop())
   

