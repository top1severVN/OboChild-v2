import sys
import time

green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"
                    
class cmp():
    """Comparison class that returns True or False depending on the result of comparisons. / class này là class so sánh, nó sẽ trả về True hoặc False tùy thuộc vào kết quả của phép so sánh"""
    def less(a, b):
        """Return True if a is less than b, otherwise False. / đây là hàm less, nó sẽ trả về True nếu a nhỏ hơn b, ngược lại sẽ trả về False"""
        if a < b:
            return True
        else:
            return False 
    def great(a, b):
        """Return True if a is greater than b, otherwise False. / đây là hàm great, nó sẽ trả về True nếu a lớn hơn b, ngược lại sẽ trả về False"""
        if a > b:
            return True
        else:
            return False
    def equal(a, b):
        """Return True if a equals b, otherwise False. / đây là hàm equal, nó sẽ trả về True nếu a bằng b, ngược lại sẽ trả về False"""
        if a == b:
            return True
        else:
            return False
    def EqGr(a, b):
        """Return True if a is greater than or equal to b, otherwise False. / đây là hàm EqGr, nó sẽ trả về True nếu a lớn hơn hoặc bằng b, ngược lại sẽ trả về False"""
        if a >= b:
            return True
        else:
            return False
    def EqLs(a, b):
        """Return True if a is less than or equal to b, otherwise False. / đây là hàm EqLs, nó sẽ trả về True nếu a nhỏ hơn hoặc bằng b, ngược lại sẽ trả về False"""
        if a <= b:
            return True
        else:
            return False
    def LsGr(a, b):
        """Return True if a is not equal to b, otherwise False. / đây là hàm LsGr, nó sẽ trả về True nếu a khác b, ngược lại sẽ trả về False"""
        if a < b or a > b:
            return True
        else:
            return False

class condition():
    """Condition class that executes conditional operations like >, <, =, <=, >=, !=. / đây là class điều kiện, nó sẽ thực thi các phép toán điều kiện như >, <, =, <=, >=, !="""
    def condi(a, symbol, b, pa, pb):
        """a: first value, symbol: condition operator, b: second value, pa: command when true, pb: command when false. / a: giá trị thứ nhất, symbol: ký hiệu của phép toán điều kiện, b: giá trị thứ hai, pa: lệnh sẽ được thực thi nếu điều kiện đúng, pb: lệnh sẽ được thực thi nếu điều kiện sai"""
        if symbol == '>':
            if a > b:
                print(pa)
            else:
                print(pb)
        elif symbol == '=':
            if a == b:
                print(pa)
            else:
                print(pb)
        elif symbol == '<':
            if a < b:
                print(pa)
            else:
                print(pb)
        elif symbol == '<=':
            if a <= b:
                print(pa)
            else:
                print(pb)
        elif symbol == '>=':
            if a >= b:
                print(pa)
            else:
                print(pb)
        elif symbol == '!=':
            if a != b:
                print(pa)
            else:
                print(pb)
        else:
            print(f"{red}Invalid symbol: {symbol}{res}")

class logic():
    """Logic class that executes logical operations like and, or, not, xor, nand, nor, xnor. / đây là class logic, nó sẽ thực thi các phép toán logic như and, or, not, xor, nand, nor, xnor"""
    def and_(a, b):
        """Return True if both a and b are True, otherwise False. / đây là hàm and, nó sẽ trả về True nếu cả a và b đều là True, ngược lại sẽ trả về False"""
        return a and b
    def or_(a, b):
        """Return True if either a or b is True, otherwise False. / đây là hàm or, nó sẽ trả về True nếu ít nhất một trong hai a hoặc b là True, ngược lại sẽ trả về False"""
        return a or b
    def not_(a):
        """Return True if a is False, otherwise False. / đây là hàm not, nó sẽ trả về True nếu a là False, ngược lại sẽ trả về False"""
        return not a
    def xor(a, b):
        """Return True if a and b are different, otherwise False. / đây là hàm xor, nó sẽ trả về True nếu a và b khác nhau, ngược lại sẽ trả về False"""
        return (a and not b) or (not a and b)
    def nand(a, b):
        """Return True if at least one of a or b is False, otherwise False. / đây là hàm nand, nó sẽ trả về True nếu ít nhất một trong hai a hoặc b là False, ngược lại sẽ trả về False"""
        return not (a and b)
    def nor(a, b):
        """Return True if both a and b are False, otherwise False. / đây là hàm nor, nó sẽ trả về True nếu cả a và b đều là False, ngược lại sẽ trả về False"""
        return not (a or b)
    def xnor(a, b):
        """Return True if a and b are equal, otherwise False. / đây là hàm xnor, nó sẽ trả về True nếu a và b giống nhau, ngược lại sẽ trả về False"""
        return not ((a and not b) or (not a and b))




            