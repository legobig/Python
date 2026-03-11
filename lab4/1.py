import operator
def make_calc(op, i=0):
    ops = {"+": operator.add,"-": operator.sub,
           "*": operator.mul,"/": operator.truediv}

    result = i

    def calc(value):
        nonlocal result
        result = ops[op](result, value)
        return result

    return calc
c = make_calc("*", i=1)
print(c(5))
print(c(2))
print(c(5))
