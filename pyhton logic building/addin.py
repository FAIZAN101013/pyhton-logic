def basic_op(operator, value1, value2):
    while True:
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            return value1 / value2
        else :
            pass
def basic_opr(operator, value1, value2):
    operator = {
        "+": value1 + value2,
        "-": value1 - value2,
        "*": value1 * value2,
        "/": value1 / value2,
    }
    return operator.get(operator,"invalid")
        
operator , value1 , value2 ='+', 4, 7
result = basic_op(operator , value1 , value2)
result2 = basic_op(operator , value1 , value2)
print(result)
print(result2)