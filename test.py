#!/bin/env python

# http://www.ccs.neu.edu/home/matthias/HtDP2e/
# How to design programs.
#
# http://muthukadan.net/docs/zca.html
# A Comprehensive Guide to Zope Component Architecture
#
# https://github.com/eugeneai/ZCA/raw/master/zca.pdf
# -- Перевод книги.
#
# http://python.org
# http://github.com
#
# http://umlet.org
#


print ("Ok")

def fact(x):
    if x<0:
        raise ValueError("negative argument")
    if x<2: return 1
    return x*fact(x-1)

class Figure(object):
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.shown=False

    def move(self, dx,dy):
        shown = self.shown
        if shown:
            self.hide()
        self.x += dx
        self.y += dy
        if shown:
            self.show()
        return self

    def hide(self):
        raise RuntimeError("should be implemented by subclass")

    def show(self):
        raise RuntimeError("should be implemented by subclass")

    def __str__(self):
        return self.__class__.__name__+"(x={},y={})".format(self.x, self.y)

    def __display__(self):
        return str(self)

class Circle(Figure):
    def __init__(self, x,y,r):
        super(Circle,self).__init__(x,y)
        #Figure.__init__(self, x,y)
        self.r=r

    def hide(self):
        print("{} now is hidden.".format(self))
        self.shown=False

    def show(self):
        print("{} now is shown.".format(self))
        self.shown=True

class Rectangle(Figure):
    def __init__(self, x,y, w,h):
        super(Rectangle,self).__init__(x,y)
        self.w=w
        self.h=h

    def show(self):
        print("{} rect has shown.".format(self))
        self.shown=True

    def hide(self):
        print("{} rect has hidden.".format(self))
        self.shown=False

if False:
    c=Circle(1,5,6)
    r=Rectangle(5,6,7,8)

    objs=[c,r]

    # 1-st way

    [o.show() for o in objs]
    [o.move(-10,0) for o in objs]

    # 2-nd way

    for o in objs:
        o.show()

    for o in objs:
        o.move(10,0)

    # 3-rd way

    def show_obj(o):
        o.show()

    map(show_obj, objs)

    map(lambda o: o.show(), objs)
    map(lambda o: o.move(10,0), objs)


if True:
    l=[1,2,3,4,5]

    nl=[]
    for n in l:
        nl.append(n*n)

    print(nl)

    nl=list(map(lambda x: x*x, l))
    print("Lambda:", nl)

    nl=[x*x for x in l if x < 3]

    print("List comprehension:", nl)

    print(l[2:7])

    # l[2:7]=[0]

    print(l)

    t=(1,2,3,4,5)

    l=[2,3,4,5]

    print(t[0])

    d = {"one":1, "two":2}

    print(d["two"])

    d["three"]=3

    print(d["three"])

    # d["four"]="46"

    a=d.setdefault("four", 4)
    print(a)


    import pprint

    S = "A quick brown fox jumped over the lazy dog."

    cnt={}

    for c in S:
        num = cnt.setdefault(c, 0)
        cnt[c]=num+1

    l=list(cnt.items())
    l.sort(key=lambda x:-x[1])

    for k, v in l:
        print("{}={}".format(repr(k),v))

    #pprint.pprint(l)

    # generators

    def l():
        i=0
        while True:
            yield i
            i+=1

    def lq():
        for x in l():
            if x<10:
                yield x*x
            else:
                break

    for o in lq():
        print(o)



    def gen():
        for i in range(10):
            yield(i)

    def ticket(n):
        if n==0:
            yield []
            return
        for i in gen():
            for t in ticket(n-1):
                yield t+[i]

    def tickets():
        yield from ticket(6)

    def lucky():
        for t in tickets():
            a,b,c, d,e,f=t
            if a+b+c == d+e+f:
                yield t

    print("Number of lucky tickets is")

    l = list(lucky())

    print(len(l))

    pprint.pprint(l[:10])
