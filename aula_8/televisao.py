class televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

if __name__ == '__main__':
    tv = televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    
#from aula_7 import televisao