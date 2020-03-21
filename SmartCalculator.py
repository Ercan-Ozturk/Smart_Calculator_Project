class SmartCalculator:
    variables = {}
    stack = []

    def __hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    def __hasWords(self, inputString):
        for i in inputString:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
                return True
        return False

    def __equationSign(self, input):
        for i in input:
            if "=" in i:
                return True
        return False



    def __operands(self, ops):
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

    def __variables(self, op):
        for i in range(len(op)):
            if (self.__hasWords(self, op[i])):
                if (self.variables.get(op[i]) != None):
                    op[i] = str(self.variables.get(op[i]))
                else:
                    return -1

        return op

    def __paranthesis(op):
        return op.count("(") == op.count(")")

    def __postfix(self,  postfix, op):
        for i in op:

            if self.__hasNumbers(self, i):
                postfix += " " + i
            elif len(self.stack) > 0:
                if (self.stack[-1] == "("):
                    self.stack.append(i)
                    continue
            if i == "+" or i == "-":
                if len(self.stack) > 0:

                    if self.stack[-1] != "*" and self.stack[-1] != "/" and self.stack[-1] != "-" and self.stack[-1] != "+":
                        self.stack.append(i)
                    else:
                        while len(self.stack) > 0:

                            if self.stack[-1] != "(":
                                postfix += " " + self.stack.pop()



                            else:
                                break
                        self.stack.append(i)

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

    def __calculate(self, calc):
        for i in calc:

            if self.__hasNumbers(self, i):
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
            print("Please enter the calculation: ", end="")
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

            if self.__equationSign(self, numbers):

                numbers = numbers.replace(" ", "")
                numbers = numbers.split("=")
                if len(numbers) > 2:
                    print("Invalid assignment")
                    continue
                if (self.__hasNumbers(self, numbers[0])):
                    print("Invalid identifier")
                    continue
                if self.__hasWords(self, numbers[1]):
                    if (self.__hasNumbers(numbers[1])):
                        print("Invalid assignment")
                        continue
                    tmp = self.variables.get(numbers[1])
                    if tmp == None:
                        print("Unknown variable")
                        continue
                else:
                    tmp = int(numbers[1])
                self.variables[numbers[0]] = tmp
                continue

            else:

                postfix_ = ""
                numbers = numbers.replace("---", "-")
                numbers = numbers.replace("--", "+")

                if "**" in numbers or "//" in numbers:
                    print("Invalid expression")
                    continue
                op = self.__operands(self, numbers)
                op = self.__variables(self, op)

                if op == -1:
                    print("Unknown variable")
                    continue
                if (len(op)) == 0:
                    continue
                if (len(op) == 2):
                    if op[0] == "-":
                        print(op[0] + op[1])
                        continue

                if self.__paranthesis(op) == False:
                    print("Invalid expression")
                    continue

                post = self.__postfix(self, postfix_, op)
                self.__calculate(self, post)
                if (len(self.stack) != 1):
                    print("Invalid expression")
                    continue
                print("Answer is: " + str(self.stack[0]))

