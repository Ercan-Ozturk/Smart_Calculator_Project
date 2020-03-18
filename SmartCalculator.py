class Smart_Calculator:
    dict = {}
    stack = []
    """
    def __init__(self):
        self.dict = {}
        self.stack = []
    """
    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    def haswords(self, inputString):
        for i in inputString:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
                return True
        return False

    def eq(self, input):
        for i in input:
            if "=" in i:
                return True
        return False

    def multipleOP(self, op):
        i = 0
        l = len(op) - 1
        while i < l:

            if self.hasNumbers(op[i]):
                if op[i + 1] not in "-*+/":
                    return -1
            else:
                if op[i + 1] in "-*+/":
                    if op[i] in "*/":
                        return -1
                    else:
                        if op[i] == "-" and op[i + 1] == "-":
                            op.pop(i)
                            op.pop(i)
                            op.insert("+", i - 1)
                            l -= 1
        return 1

    def operands(self, ops):
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
                        if (op[-1] == "-"):
                            op.pop()
                            op.append("+")
                    else:
                        tmp += "-"
            elif i == "+":
                if tmp != "":
                    op.append(tmp)
                    tmp = ""
                if (op[-1] != "+"):
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

    def variables(self, op):
        for i in range(len(op)):
            if (self.haswords(self, op[i])):
                if (self.dict.get(op[i]) != None):
                    op[i] = str(self.dict.get(op[i]))
                else:
                    return -1

        return op

    def paran(op):
        return op.count("(") == op.count(")")

    def postfix(self,  postfix, op):#stack i sildim
        # stack = []
        # postfix = ""
        for i in op:

            if self.hasNumbers(self, i):
                postfix += " " + i
            elif len(self.stack) > 0:
                if (self.stack[-1] == "("):
                    self.stack.append(i)
                    continue
            if i == "+" or i == "-":
                if len(self.stack) > 0:

                    if self.stack[-1] != "*" and self.stack[-1] != "/" and self.stack[-1] != "-" and stack[-1] != "+":
                        self.stack.append(i)
                    else:
                        while len(self.stack) > 0:

                            if self.stack[-1] != "(":
                                postfix += " " + self.stack.pop()



                            else:
                                break
                        self.stack.append(i)

                        # postfix += " " + stack.pop()

                else:
                    self.stack.append(i)
            elif i == "*" or i == "(" or i == "/":
                self.stack.append(i)

            elif i == ")":

                while len(self.stack) > 0:

                    if (self.stack[-1] != "("):
                        postfix += " " + self.stack.pop()

                    else:

                        self.stack.pop()
                        break

        while (len(self.stack) > 0):
            postfix += " " + self.stack.pop()

        calc = postfix.split(" ")
        calc.pop(0)
        return calc

    def calculate(self, calc):
        for i in calc:

            if self.hasNumbers(self, i):
                self.stack.append(i)
            elif i == "+":
                one = self.stack.pop()
                two = self.stack.pop()
                self.stack.append(int(one) + int(two))
            elif i == "*":
                one = self.stack.pop()
                two = self.stack.pop()
                self.stack.append(int(one) * int(two))
            elif i == "/":
                one = self.stack.pop()
                two = self.stack.pop()
                self.stack.append(int(two) // int(one))
            elif i == "-":
                one = self.stack.pop()
                two = self.stack.pop()
                self.stack.append(int(two) - int(one))
    def menu(self):
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

            if self.eq(self, numbers):

                numbers = numbers.replace(" ", "")
                numbers = numbers.split("=")
                if len(numbers) > 2:
                    print("Invalid assignment")
                    continue
                if (self.hasNumbers(self, numbers[0])):
                    print("Invalid identifier")
                    continue
                if self.haswords(self, numbers[1]):
                    if (self.hasNumbers(numbers[1])):
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
                #stack = []
                postfix_ = ""
                numbers = numbers.replace("---", "-")
                numbers = numbers.replace("--", "+")

                if "**" in numbers or "//" in numbers:
                    print("Invalid expression")
                    continue
                op = self.operands(self, numbers)
                op = self.variables(self, op)
                print(op)
                if op == -1:
                    print("Unknown variable")
                    continue
                if (len(op)) == 0:
                    continue
                if (len(op) == 2):
                    if op[0] == "-":
                        print(op[0] + op[1])
                        continue

                if self.paran(op) == False:
                    print("Invalid expression")
                    continue

                post = self.postfix(self, postfix_, op)
                self.calculate(self, post)
                if (len(self.stack) != 1):
                    print("Invalid expression")
                    continue
                print(self.stack[0])

