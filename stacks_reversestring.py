from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr + myStack.pop()
    return revstr    
    

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
