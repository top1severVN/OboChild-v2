

green = "\033[32m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
res = "\033[0m"

class Press():
    """đây là một class chứa các lệnh liên quan đến việc kiểm tra xem người dùng có nhấn phím cụ thể hay không. Nó có hai phương thức: pressed và wait."""
    def wait():
        """đây là một hàm để chờ người dùng nhấn một phím bất kỳ trước khi tiếp tục thực thi chương trình."""
        try:
            import msvcrt
            print("Press any key to continue...")
            msvcrt.getch()
        except ImportError:
            import sys, tty, termios
            print("Press any key to continue...")
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    def pressed(key, cmd, notcmd):
        """đây là một hàm để kiểm tra xem người dùng có nhấn phím cụ thể hay không. Nếu người dùng nhấn phím đó, hàm sẽ thực thi lệnh cmd, ngược lại sẽ thực thi lệnh notcmd."""
        import msvcrt
        print(f"Press {key} to continue...")
        char = msvcrt.getch().decode('utf-8')
        if char.lower() == key.lower():
            cmd()
        else:
            notcmd()
