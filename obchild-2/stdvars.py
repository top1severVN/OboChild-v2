green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"

class vars():
    def __init__(self):
        self.memory = {}
    def gift(self, key, value):
            if isinstance(key, str):
                self.memory[key] = value
    def get(self, key):
        if key in self.memory:
            return self.memory[key]
        else:
            print(f"khong tim thay{red}[KeyError]{res}")
            
class varsplus():
    def __init__(self):
        self.memory = {}
        self.current_name = ""
    def create(self, name):
        self.current_name = name 
        self.memory[name] = []
    def give(self, var, value, ram):
        if ram == self.current_name:
            self.memory[ram].append([var, value])
        else:
            print("KeyError")
    def take(self, var):
        for item in self.memory[self.current_name]:
            if item[0] == var:
                return item[1]
        return f"Error: not see -> {var}"
    