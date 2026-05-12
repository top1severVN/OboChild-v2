import re 
import sys

green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"

class stdout():
    @staticmethod
    def output(data):
        if isinstance(data, str):
            if data.startswith('"') and data.endswith('"') or data.startswith("'") and data.endswith("'"):
                data = data.strip('"').strip("'")
                sys.stdout.write(str(data) + '\n')
                sys.stdout.flush()
            elif data in globals():
                value = globals()[data]
                sys.stdout.write(str(data) + '\n')
                sys.stdout.flush()
            else:
                sys.stdout.write(str(data) + '\n')
                sys.stdout.flush()
        else:
            sys.stdout.write(str(data) + '\n')
            sys.stdout.flush()
    class out():
        def ring_red(data):
            if isinstance(data, str):
                if data.startswith('"') and data.endswith('"') or data.startswith("'") and data.endswith("'"):
                    data = data.strip('"').strip("'")
                    sys.stdout.write(red + str(data) + '\n' + res)
                    sys.stdout.flush()
                elif data in globals():
                    value = globals()[data]
                    sys.stdout.write(red + str(data) + '\n' + res)
                    sys.stdout.flush()
                else:
                    sys.stdout.write(red + str(data) + '\n' + res)
                    sys.stdout.flush()
            else:
                sys.stdout.write(red + str(data) + '\n' + res)
                sys.stdout.flush()
        def ring_green(data):
            if isinstance(data, str):
                if data.startswith('"') and data.endswith('"') or data.startswith("'") and data.endswith("'"):
                    data = data.strip('"').strip("'")
                    sys.stdout.write(green + str(data) + '\n' + res)
                    sys.stdout.flush()
                elif data in globals():
                    value = globals()[data]
                    sys.stdout.write(green + str(data) + '\n' + res)
                    sys.stdout.flush()
                else:
                    sys.stdout.write(green + str(data) + '\n' + res)
                    sys.stdout.flush()
            else:
                sys.stdout.write(green + str(data) + '\n' + res)
                sys.stdout.flush()
        def ring_yellow(data):
            if isinstance(data, str):
                if data.startswith('"') and data.endswith('"') or data.startswith("'") and data.endswith("'"):
                    data = data.strip('"').strip("'")
                    sys.stdout.write(yellow + str(data) + '\n' + res)
                    sys.stdout.flush()
                elif data in globals():
                    value = globals()[data]
                    sys.stdout.write(yellow + str(data) + '\n' + res)
                    sys.stdout.flush()
                else:
                    sys.stdout.write(yellow + str(data) + '\n' + res)
                    sys.stdout.flush()
            else:
                sys.stdout.write(yellow + str(data) + '\n' + res)
                sys.stdout.flush()
        def ring_blue(data):
            if isinstance(data, str):
                if data.startswith('"') and data.endswith('"') or data.startswith("'") and data.endswith("'"):
                    data = data.strip('"').strip("'")
                    sys.stdout.write(blue + str(data) + '\n' + res)
                    sys.stdout.flush()
                elif data in globals():
                    value = globals()[data]
                    sys.stdout.write(blue + str(data) + '\n' + res)
                    sys.stdout.flush()
                else:
                    sys.stdout.write(blue + str(data) + '\n' + res)
                    sys.stdout.flush()
            else:
                sys.stdout.write(blue + str(data) + '\n' + res)
                sys.stdout.flush()
        
class stdin():
    def input(data, typ):
        try:
            if typ == "int":
                tp = int
            elif typ == "flt":
                tp = float
            elif typ == "str":
                tp = str
            elif typ == "cmx":
                tp = complex
            else:
                tp = str
            if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
                data = data.strip('"')
                return tp(input(data))
            else:
                return tp(input(data))
        except Exception as e:
            print(f"loi roi: {red}{e}{res}")