operands=[]
operators=[]

priorities={
    "(":-1,
    ".":0,
    "^":1,
    "*":2,
    "/":2,
    "+":3,
    "-":3,
}

def calc_expression(expression):
    for a in expression:


