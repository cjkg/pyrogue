class Palette(object):
    def __init__(self):
        self.Colors = {'black': self.black(),
                        'blue': self.blue(),
                        'green': self.green(),
                        'cyan': self.cyan(),
                        'red': self.red(),
                        'magenta': self.magenta(),
                        'brown': self.brown(),
                        'dred': self.dred(),
                        'lgray': self.lgray(),
                        'dgray': self.dgray(),
                        'lblue': self.lblue(),
                        'lgreen': self.lgreen(),
                        'lcyan': self.lcyan(),
                        'orange': self.orange(),
                        'lred': self.lred(),
                        'lmagenta': self.lmagenta(),
                        'yellow': self.yellow(),
                        'white': self.white()
                        }
    def black(self):
        return (25, 25, 25)
    def blue(self):
        return (0, 99, 177)
    def green(self):
        return (85, 153, 85)
    def cyan(self):
        return (77, 158, 161)
    def red(self):
        return (187, 34, 34)
    def magenta(self):
        return (170, 51, 119)
    def brown(self):
        return (140, 117, 100)
    def dred(self):
        return (101, 1, 10)
    def lgray(self):
        return (157, 174, 178)
    def dgray(self):
        return (91, 112, 117)
    def lblue(self):
        return (48, 165, 255)
    def lgreen(self):
        return (153, 238, 119)
    def lcyan(self):
        return (128, 212, 215)
    def orange(self):
        return (248, 179, 74)
    def lred(self):
        return (246, 114, 128)
    def lmagenta(self):
        return (255, 136, 187)
    def yellow(self):
        return (255, 255, 102)
    def white(self):
        return (255, 250, 232)
