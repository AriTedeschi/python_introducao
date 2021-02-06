class BinaryTree:
    def __init__(self):
        self.datum = None
        self.left  = None
        self.right = None
    
    def getBound(self):
        return self.datum

    def newBound(self, e):
        self.datum = e
        self.left = BinaryTree()
        self.right = BinaryTree()
        return self

    def insert(self, e):
        if self.datum is None:
            self.newBound(e)
        elif e > self.datum:
            self.right.insert(e)
        else:
            self.left.insert(e)
    
    def IsPresent(self, e):
        if self.datum is None:
            return False
        elif self.datum == e:
            return True
        elif self.datum > e:
            return self.right.IsPresent(e)
        else:
            return self.left.IsPresent(e)
    
    def height(self):
        if self.datum is None:
            return -1
        else:
            leftHeight  = 1+self.left.height()
            rightHeight = 1+self.right.height()
            return leftHeight if leftHeight > rightHeight else rightHeight
    
    def countBounds(self):
        if self.datum is None:
            return 0
        elif self.left.datum is None and self.right.datum is None:
            return 1
        else:
            return (self.left.countBounds() + self.right.countBounds())

    def countNodes(self):
        if self.datum is None:
            return 0
        else:
            return (1 + self.left.countNodes() + self.right.countNodes())


    
    def preordem(self):
        if self.datum != None:
            print(self.datum)
            self.left.preordem()
            self.right.preordem()

    def inordem(self):
        if self.datum != None:
            self.left.inordem()
            print(self.datum)
            self.right.inordem()
            
    def posordem(self):
        if self.datum != None:
            self.left.posordem()
            self.right.posordem()
            print(self.datum)

if __name__ == '__main__':
    entry = [50, 17, 12, 9, 14, 23, 19, 72, 54, 67, 76]
    t = BinaryTree()

    for e in entry:
        t.insert(e)
    print("Percurso em ordem: ")
    # t.inordem()
    print("Percurso em preordem: ")
    # t.preordem()
    print("Percurso em posordem: ")
    # t.posordem()
    print("\nAltura da Arvore: {}".format(t.height()))
    print("Qtde Nos Folha: {}".format(t.countBounds()))
    print("Qtde Nos Total: {}".format(t.countNodes()))
    print("\nElemento 6 está presente? {}".format(t.IsPresent(6)))
    print("Elemento 6 está presente? {}".format(t.IsPresent(11)))
    