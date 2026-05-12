import pygame as py
import sys

class ogame:
    """Basic game helper for pygame initialization, screen setup, and event handling."""

    def __init__(obj, width=640, height=480, title='GS Window'):
        py.init()
        obj.screen = py.display.set_mode((width, height))
        py.display.set_caption(title)
        obj.clock = py.time.Clock()
        obj.running = True

    def screen(obj, x, y):
        """Set the game window size to (x, y)."""
        obj.screen = py.display.set_mode((x, y))
        return obj.screen

    def fill(obj, color=(0, 0, 0)):
        """Fill the screen with a color."""
        obj.screen.fill(color)
        py.display.flip()

    def gameloop(obj):
        """Process events and return the current running state."""
        for event in py.event.get():
            if event.type == py.QUIT:
                obj.running = False
        return obj.running

    @staticmethod
    def mapsize(x, y, a, b):
        """Return a pygame.Rect of the given position and size."""
        return py.Rect(x, y, a, b)

    def pressed(obj, but):
        """Return True if the specified key is currently pressed."""
        k = py.key.get_pressed()
        dickey = {
            "a": py.K_a,
            "s": py.K_s,
            "d": py.K_d,
            "w": py.K_w,
            "e": py.K_e,
            "q": py.K_q,
            "z": py.K_z,
            "x": py.K_x,
            "c": py.K_c,
            "r": py.K_r,
            "v": py.K_v,
            "f": py.K_f,
            "b": py.K_b,
            "n": py.K_n,
            "m": py.K_m,
            "k": py.K_k,
            "l": py.K_l,
            "j": py.K_j,
            "h": py.K_h,
            "g": py.K_g,
            "t": py.K_t,
            "y": py.K_y,
            "u": py.K_u,
            "i": py.K_i,
            "o": py.K_o,
            "p": py.K_p,
            "1": py.K_1,
            "2": py.K_2,
            "3": py.K_3,
            "4": py.K_4,
            "5": py.K_5,
            "6": py.K_6,
            "7": py.K_7,
            "8": py.K_8,
            "9": py.K_9,
            "0": py.K_0,
            "down": py.K_DOWN,
            "up": py.K_UP,
            "left": py.K_LEFT,
            "right": py.K_RIGHT
        }
        target = dickey.get(but.lower())
        if target:
            return k[target]
        return False

    def endgame(obj):
        """Quit pygame and exit the program."""
        py.quit()
        sys.exit()

    def close(obj):
        """Close the pygame window without exiting the interpreter."""
        py.quit()


class draw:
    """Drawing helper with basic shape functions."""

    @staticmethod
    def rect(obj, color, rect, width=0):
        """Draw a rectangle on the screen."""
        py.draw.rect(obj.screen, color, rect, width)
        py.display.flip()

    @staticmethod
    def circle(obj, color, center, radius, width=0):
        """Draw a circle on the screen."""
        py.draw.circle(obj.screen, color, center, radius, width)
        py.display.flip()

    @staticmethod
    def line(obj, color, start_pos, end_pos, width=1):
        """Draw a line on the screen."""
        py.draw.line(obj.screen, color, start_pos, end_pos, width)
        py.display.flip()

    @staticmethod
    def polygon(obj, color, pointlist, width=0):
        """Draw a polygon on the screen."""
        py.draw.polygon(obj.screen, color, pointlist, width)
        py.display.flip()

    @staticmethod
    def text(obj, text, position, size=24, color=(255, 255, 255), font_name=None):
        """Render text on the screen."""
        font = py.font.SysFont(font_name, size)
        surface = font.render(str(text), True, color)
        obj.screen.blit(surface, position)
        py.display.flip()
    
                