import sys
import time

green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"
under = "\033[4m"
inc = "\033[3m"
smoke = "\033[2m"
strong = "\033[1m"
theme = "\033[7m"
invisible = "\033[8m"


class ring():
    """Basic loop printing command class. / class này là class lệnh in vòng lặp cơ bản"""
    def star(start, end, string, step=1):
        """start: start of the loop, end: end of the loop, string: data to print, step: loop increment. / start: số bắt đầu của vòng lặp, end: số kết thúc của vòng lặp, string: dữ liệu sẽ được in ra màn hình, step: bước nhảy của vòng lặp"""
        if isinstance(string, str) and string.startswith('"') and string.endswith('"'):
            string = string.split('"')
            for i in range(start, end, step):
                sys.stdout.write(str(string) + '\n')
                sys.stdout.flush()
        elif string in globals():
            value = globals()[string]
            for i in range(start, end, step):
                sys.stdout.write(str(string) + '\n')
                sys.stdout.flush()
        else:
            for i in range(start, end, step):
                sys.stdout.write(str(string) + '\n')
                sys.stdout.flush()

colors = {
    "green": "\033[32m",
    "red": "\033[31m",
    "blue": "\033[34m",
    "yellow": "\033[33m"
}

fonts = {
    "strong": "\033[1m",
    "invi": "\033[8m",
    "under": "\033[4m",
    "reverse": "\033[7m",
    "smoke": "\033[2m",
    "inc": "\033[3m"
}

speeds = {
    "slow": 1,
    "fast": 0.05,
    "fast than": 0,
    "medium": 0.5,
    "slow than": 1.5,
    "none": 0.2
}
class cust():
    """Advanced loop printing class with color, font, and speed control. / class này là class lệnh in vòng lặp nâng cao, nó có thể in ra dữ liệu với màu sắc và kiểu chữ khác nhau, cũng như có thể điều chỉnh tốc độ in dữ liệu"""
    def star(start, end, data, speed="none", font=res, color=res, step=1):
        """start: start of the loop, end: end of the loop, data: data to print, speed: printing speed, font: text style, color: text color, step: loop increment. / start: số bắt đầu của vòng lặp, end: số kết thúc của vòng lặp, data: dữ liệu sẽ được in ra màn hình, speed: tốc độ in dữ liệu, font: kiểu chữ của dữ liệu sẽ được in ra, color: màu sắc của dữ liệu sẽ được in ra, step: bước nhảy của vòng lặp"""   
        if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
            data = data.split('"')
            sp = speeds.get(speed, 0,2)
            ft = fonts.get(font, res)
            cl = colors.get(color, res)
            for i in range(start, end, step):
                sys.stdout.write(f"{cl}{ft}{data}{res}\n")
                sys.stdout.flush()
                time.sleep(sp)
        else:
            sp = speeds.get(speed, 0.2)
            ft = fonts.get(font, res)
            cl = colors.get(color, res)
            for i in range(start, end, step):
                sys.stdout.write(f"{cl}{ft}{data}{res}\n")
                sys.stdout.flush()
                time.sleep(sp)

class command():
    """Helper loop commands class. / class này là class chứa các lệnh hỗ trợ vòng lặp"""
    def out_now(self, data):
        """data: data to print. / data: dữ liệu sẽ được in ra màn hình"""
        if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
            data = data.split('"')
            print(data)
        elif data in globals():
            value = globals()[data]
            print(data)
        else:
            print(data)
    def out_color(self, data, color):
        """data: data to print, color: text color. / data: dữ liệu sẽ được in ra màn hình, color: màu sắc của dữ liệu sẽ được in ra"""
        cl = colors.get(color, res)
        if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
            data = data.split('"')
            print(f"{cl}{data}{res}")
        elif data in globals():
            value = globals()[data]
            print(f"{cl}{data}{res}")
        else:
            print(f"{cl}{data}{res}")
    def out_font(self, data, font):
        """data: data to print, font: text style. / data: dữ liệu sẽ được in ra màn hình, font: kiểu chữ của dữ liệu sẽ được in ra""" 
        ft = fonts.get(font, res)
        if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
            data = data.split('"')
            print(f"{ft}{data}{res}")
        elif data in globals():
            value = globals()[data]
            print(f"{ft}{data}{res}")
        else:
            print(f"{ft}{data}{res}")
    def out_color_font(self, data, color, font):
        """data: data to print, color: text color, font: text style. / data: dữ liệu sẽ được in ra màn hình, color: màu sắc của dữ liệu sẽ được in ra, font: kiểu chữ của dữ liệu sẽ được in ra"""  
        cl = colors.get(color, res)
        ft = fonts.get(font, res)
        if isinstance(data, str) and data.startswith('"') and data.endswith('"'):
            data = data.split('"')
            print(f"{cl}{ft}{data}{res}")
        elif data in globals():
            value = globals()[data]
            print(f"{cl}{ft}{data}{res}")
        else:
            print(f"{cl}{ft}{data}{res}")
    def in_now(self, prompt):
        """prompt: prompt shown when asking for user input. / prompt: lời nhắc sẽ được hiển thị khi người dùng nhập dữ liệu"""
        if isinstance(prompt, str) and prompt.startswith('"') and prompt.endswith('"'):
            prompt = prompt.split('"')
            return input(prompt)
        elif prompt in globals():
            value = globals()[prompt]
            return input(value)
        else:
            return input(prompt)
    def in_color(self, prompt, color):
        """prompt: prompt shown when asking for user input, color: prompt text color. / prompt: lời nhắc sẽ được hiển thị khi người dùng nhập dữ liệu, color: màu sắc của lời nhắc sẽ được hiển thị"""
        cl = colors.get(color, res)
        if isinstance(prompt, str) and prompt.startswith('"') and prompt.endswith('"'):
            prompt = prompt.split('"')
            return input(f"{cl}{prompt}{res}")
        elif prompt in globals():
            value = globals()[prompt]
            return input(f"{cl}{prompt}{res}")
        else:
            return input(f"{cl}{prompt}{res}")
    def in_font(self, prompt, font):
        """prompt: prompt shown when asking for user input, font: prompt text style. / prompt: lời nhắc sẽ được hiển thị khi người dùng nhập dữ liệu, font: kiểu chữ của lời nhắc sẽ được hiển ra"""
        ft = fonts.get(font, res)
        if isinstance(prompt, str) and prompt.startswith('"') and prompt.endswith('"'):
            prompt = prompt.split('"')
            return input(f"{ft}{prompt}{res}")
        elif prompt in globals():
            value = globals()[prompt]
            return input(f"{ft}{prompt}{res}")
        else:
            return input(f"{ft}{prompt}{res}")
    def in_color_font(self, prompt, color, font):
        """prompt: prompt shown when asking for user input, color: prompt text color, font: prompt text style. / prompt: lời nhắc sẽ được hiển thị khi người dùng nhập dữ liệu, color: màu sắc của lời nhắc sẽ được hiển thị, font: kiểu chữ của lời nhắc sẽ được hiển thị"""
        cl = colors.get(color, res)
        ft = fonts.get(font, res)
        if isinstance(prompt, str) and prompt.startswith('"') and prompt.endswith('"'):
            prompt = prompt.split('"')
            return input(f"{cl}{ft}{prompt}{res}")
        elif prompt in globals():
            value = globals()[prompt]
            return input(f"{cl}{ft}{prompt}{res}")
        else:
            return input(f"{cl}{ft}{prompt}{res}")
    def tempo(t):
        """t: time to pause before continuing the loop. / t: thời gian để vòng lặp tiếp tục thực thi sau khi dừng"""
        time.sleep(t)
    def stop(bool):
        """bool: if True, stop the loop immediately; if False, continue after waiting. / bool: nếu bool là True thì vòng lặp sẽ dừng ngay lập tức, nếu bool là False thì vòng lặp sẽ tiếp tục thực thi sau khi thời gian đã được đặt"""
        if bool == True:
            sys.exit()
        elif bool == False:
            def next_time(t):
                """t: thời gian để vòng lặp tiếp tục thực thi sau khi dừng"""
                time.sleep(t)
            def stop_time(t):
                """t: thời gian để vòng lặp tiếp tục thực thi sau khi dừng"""
                time.sleep(t)
                sys.exit()


class forever():
    """Loop class that executes commands repeatedly until stopped. / class này là 1 class vòng lặp , nó sẽ thực thi các lệnh trong vòng lặp mãi mãi cho đến khi có lệnh dừng vòng lặp"""
    def condition(condition, rections):
        """condition: loop condition, rections: commands to execute inside the loop. / condition: điều kiện để vòng lặp và rections: các lệnh sẽ được thực thi trong vòng lặp"""
        while condition:
            for rection in rections:
                rection()
                time.sleep(0.1)