def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def haswords(inputString):
    for i in inputString:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False
def eq(input):
    for i in input:
        if "=" in i:
            return True
    return False
"""
sadece operatör girilince çöküyor
"""
def multipleOP(op):
    i=0
    l = len(op) -1
    while i < l:

        if hasNumbers(op[i]):
            if op[i + 1] not in "-*+/":
                return -1
        else:
            if op[i + 1]  in "-*+/":
                if op[i] in "*/":
                    return -1
                else:
                    if op[i] == "-" and op[i+1] == "-":
                        op.pop(i)
                        op.pop(i)
                        op.insert("+", i-1)
                        l-=1
    return 1



def operands(ops):
    tmp = ""
    op = []
    for i in ops:

        if i == "(":
            if tmp != "":
                op.append(tmp)
                tmp = ""
            op.append(i)
        elif i == ")":
            if tmp != "":
                op.append(tmp)
                tmp = ""
            op.append(i)
        elif i in " ":
            if tmp != "":
                op.append(tmp)
                tmp = ""
        elif i == "-":
            if tmp != "":

                op.append(tmp)
                tmp = ""
                op.append(i)
            else:

                if tmp == "-":
                    if(op[-1] == "-"):
                        op.pop()
                        op.append("+")
                else:
                    tmp += "-"
        elif i == "+":
            if tmp != "":
                op.append(tmp)
                tmp = ""
            if(op[-1] != "+"):
                op.append(i)
        elif i in "*/+":
            if tmp != "":
                op.append(tmp)
                tmp = ""
            op.append(i)

        else:
            tmp += i
    if tmp != "":
        op.append(tmp)
    return op
def variables(op, dict):
    for i in range(len(op)):
        if(haswords(op[i])):
            if(dict.get(op[i]) != None):
                op[i] = str(dict.get(op[i]))
            else:
                return -1

    return op

def paran(op):
    return op.count("(") == op.count(")")

def postfix(stack, postfix, op):
    #stack = []
    #postfix = ""
    for i in op:

        if hasNumbers(i):
            postfix += " " + i
        elif len(stack) > 0:
            if (stack[-1] == "("):
                stack.append(i)
                continue
        if i == "+" or i == "-":
            if len(stack) > 0:

                if stack[-1] != "*" and stack[-1] != "/" and stack[-1] != "-" and stack[-1] != "+":
                    stack.append(i)
                else:
                    while len(stack) > 0:

                        if stack[-1] != "(":
                            postfix += " " + stack.pop()



                        else:
                            break
                    stack.append(i)

                    # postfix += " " + stack.pop()

            else:
                stack.append(i)
        elif i == "*" or i == "(" or i == "/":
            stack.append(i)

        elif i == ")":

            while len(stack) > 0:

                if (stack[-1] != "("):
                    postfix += " " + stack.pop()

                else:

                    stack.pop()
                    break

    while (len(stack) > 0):
        postfix += " " + stack.pop()


    calc = postfix.split(" ")
    calc.pop(0)
    return calc

def calculate(calc, stack_):
    for i in calc:

        if hasNumbers(i):
            stack_.append(i)
        elif i == "+":
            one = stack_.pop()
            two = stack.pop()
            stack_.append(int(one) + int(two))
        elif i == "*":
            one = stack_.pop()
            two = stack_.pop()
            stack_.append(int(one) * int(two))
        elif i == "/":
            one = stack_.pop()
            two = stack_.pop()
            stack_.append(int(two) // int(one))
        elif i == "-":
            one = stack_.pop()
            two = stack_.pop()
            stack_.append(int(two) - int(one))
    return stack_

dict = {}
while (True):

    numbers = input()
    if len(numbers) > 0:
        if numbers[0] == "/":
            if numbers == "/exit":
                print("Bye!")
                break
            if numbers == "/help":
                print("Calculator")
                continue
            else:
                print("Unknown command")
                continue

    if eq(numbers):

        numbers = numbers.replace(" ", "")
        numbers = numbers.split("=")
        if len(numbers) > 2:
            print("Invalid assignment")
            continue
        if(hasNumbers(numbers[0])):
            print("Invalid identifier")
            continue
        if haswords(numbers[1]):
            if(hasNumbers(numbers[1])):
                print("Invalid assignment")
                continue
            tmp = dict.get(numbers[1])
            if tmp == None:
                print("Unknown variable")
                continue
        else:
            tmp = int(numbers[1])
        dict[numbers[0]] = tmp
        continue

    else:
        stack = []
        postfix_ = ""
        numbers = numbers.replace("---", "-")
        numbers = numbers.replace("--", "+")

        if "**" in numbers or "//" in numbers:
            print("Invalid expression")
            continue
        op = operands(numbers)
        op = variables(op, dict)
        print(op)
        if op == -1:
            print("Unknown variable")
            continue
        if(len(op)) == 0:
            continue
        if(len(op) == 2):
            if op[0] == "-":
                print(op[0]+op[1])
                continue

        if paran(op) == False:
            print("Invalid expression")
            continue

        post = postfix(stack, postfix_, op)
        calc = calculate(post, stack)
        if(len(calc)!=1):
            print("Invalid expression")
            continue
        print(calc[0])



