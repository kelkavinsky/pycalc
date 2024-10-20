from enum import Enum
import math
from my_sort import MyEval
j = MyEval()
#from mainwindow import MainWindow
ops = ["+", "-", "*", "/"]
acts = ["AC", "C", "=","sqrt"]
digits = list("0123456789.")
brackets = ["(",")"]
#1233321123123132132
#from mainwindow import MainWindow
class State(Enum):
    CLEAR = 0
    DIGITS = 1
    OPS = 2
    BRACKETS = 3

class EventType(Enum):
    NUMBER = 0
    ACTS = 1
    OP = 2
    BRACKETS = 3


class MyCalc():
    def __init__(self):
        self.event_type = EventType.NUMBER
        self.current_line = ""
        self.input = []
        self.state = State.CLEAR
        self.stack = []
        self.history = None
        self.brcts = 0
        print (self.state)

    def clear(self):
        return
    def number(self):
        return
    def op(self):
        return






    digitsTable = ['acts','number','op']


    def do_event(self, event, value):
        print("history", self.history)
        self.history = None
        #MainWindow.history_update(self,"123")
        print (self.state, value, event)
        match self.state:

            case State.CLEAR:

                self.stack.clear()
                match event:
                    case EventType.NUMBER:

                        self.current_line = ""
                        print(self.current_line, "kavo")
                        print(self.current_line)
                        self.state = State.DIGITS
                        self.current_line += value
                        print(self.current_line)
                        return self.current_line

                    case EventType.OP:
                        None

                    case EventType.ACTS:
                        None
                    case EventType.BRACKETS:
                        if value == "(":
                            self.current_line = ""
                            self.brcts = 0
                            self.current_line += value
                            self.state = State.BRACKETS
                            self.brcts += 1
                            return self.current_line
            case State.DIGITS:
                match event:
                    case EventType.NUMBER:
                        if value == "." and "." in self.current_line:
                            return self.current_line
                        else:
                            self.current_line += value
                            print(self.current_line)
                            return self.current_line


                    case EventType.OP:
                        self.state = State.OPS
                        self.history = self.current_line
                        self.stack.append(self.current_line)
                        #
                        #self.ui.history.setText(self.stack[0])                                                                          #self.ui.digits.setText(dtext)

                        self.current_line = ""
                        self.current_line += value
                        print(self.stack)
                        return self.current_line

                    case EventType.ACTS:
                        print(value, "najal")
                        match value:
                            case "sqrt":
                                sqrt = math.sqrt(float(self.current_line))
                                if sqrt.is_integer() == True:
                                    self.current_line = str(int(sqrt))
                                else:
                                    self.current_line = (str('%.2f' % sqrt))
                                self.state = State.CLEAR
                                return self.current_line
                            case 'C':

                                self.current_line = ""
                            case 'AC':
                                self.state = State.CLEAR
                                print(self.state)
                                return
                            case '=':
                                self.history = self.current_line
                                if len(self.stack) >= 0:
                                        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                                        result = j.Evaluate(j.post_fix(j.tokens(''.join(self.stack) + self.current_line)))
                                        print(result)
                                        result = float('%.2f' % float(result[0]))
                                        print('hehe')
                                        if result.is_integer() == True:
                                            self.current_line = str(int(result))
                                        else:
                                            self.current_line = str(result)
                                        self.history += '\n'+"="+ str(result)
                                        self.state = State.CLEAR


                                        print(self.state)
                                return self.current_line


                        return

            case State.OPS:
                match event:
                    case EventType.NUMBER:
                        self.state = State.DIGITS
                        self.history = self.current_line
                        self.stack.append(self.current_line)
                        print(self.stack)

                        self.current_line = ""
                        self.current_line += value
                        print(self.current_line)
                        return self.current_line

                    case EventType.OP:
                        self.current_line = value
                        return self.current_line

                        if value == "(":
                            self.brcts = 0
                            self.current_line += value
                            self.state = State.BRACKETS
                            self.brcts += 1
                            return self.current_line

                    case EventType.ACTS:
                        print(value)
                        match value:
                            case "C":
                                self.state = State.CLEAR
                                                                                                           #acts = ["AC", "C", "="]
                            case "=":
                                print(value)
                                if self.current_line in ops:
                                    result = j.Evaluate(j.post_fix(j.tokens(''.join(self.stack))))
                                    result = float('%.2f' % float(result[0]))
                                    # result = float('%.2f' % eval(''.join(self.stack)))
                                else:
                                    result = j.Evaluate(j.post_fix(j.tokens(''.join(self.stack) + self.current_line)))
                                    result = float('%.2f' % float(result[0]))
                                    # result = float('%.2f' % eval(''.join(self.stack) + self.current_line))
                                print(result)
                                if result.is_integer() == True:
                                    self.current_line = str(int(result))
                                else:
                                    self.current_line = str(result)


                                self.state = State.CLEAR
                                print(self.state)
                                return self.current_line

                    case EventType.BRACKETS:
                        if value == "(":
                            self.history = self.current_line
                            self.stack.append(self.current_line)
                            self.current_line = ""
                            self.brcts = 0
                            self.current_line += value
                            self.state = State.BRACKETS
                            self.brcts += 1
                            return self.current_line



            case State.BRACKETS:
                print(self.brcts)


                if self.brcts > 0:

                    match event:
                        case EventType.NUMBER:
                            self.current_line += value
                            return self.current_line
                        case EventType.OP:
                            self.current_line += value
                            return self.current_line
                        case EventType.ACTS:
                            match value:
                                case "C":
                                    self.state = State.CLEAR
                                case "=":
                                    return

                        case EventType.BRACKETS:
                            match value:
                                case ")":
                                    self.brcts -= 1
                                    self.current_line += value
                                    return self.current_line
                                case "(":
                                    self.brcts += 1
                                    self.current_line += value
                                    return self.current_line



                elif self.brcts == 0 and EventType.OP:
                    if value == "=":
                        self.state = State.DIGITS
                        return self.do_event(EventType.ACTS, "=")

                        print("hhhhhhhhhhhhhhhh")
                    self.state = State.OPS
                    self.history = self.current_line
                    self.stack.append(self.current_line)
                        #
                        #self.ui.history.setText(self.stack[0])                                                                          #self.ui.digits.setText(dtext)

                    self.current_line = ""
                    self.current_line += value
                    print(self.stack)
                    return self.current_line






                else:
                    match event:
                        case EventType.NUMBER:
                            return
                        case EventType.OP:
                            self.state = State.OPS
                            self.history = self.current_line
                            self.stack.append(self.current_line)
                            #
                            #self.ui.history.setText(self.stack[0])                                                                          #self.ui.digits.setText(dtext)

                            self.current_line = ""
                            self.current_line += value
                            print(self.stack)
                            return self.current_line






    def send(self,s):
        if s in digits:
            self.event_type = EventType.NUMBER
        elif s in ops:
            self.event_type = EventType.OP
        elif s in acts:
            self.event_type = EventType.ACTS
        elif s in brackets:
            self.event_type = EventType.BRACKETS
        return self.do_event(self.event_type, s)





        print(self.state)
        print('typed ', s)
        self.current_line += s
        return self.current_line
