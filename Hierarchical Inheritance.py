class shape:

    def massage(self):
        print("shape class")

class rectangle(shape):
    pass

class circle(shape):
    pass

r = rectangle()
c = circle()

r.massage()
c.massage()