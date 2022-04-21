# ANSI stuff

# import ANSIescs
from pickle import REDUCE


class cOld:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # end color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BGBLUE = '\033[44m'

class c:
    # template is '\033[@m' with @ being the color code
    # colors from https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

    # normal foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # bright foreground colors
    BTBLACK = '\033[90m'
    BTMAGENTA = '\033[95m'
    BTBLUE = '\033[94m'
    BTCYAN = '\033[96m'
    BTGREEN = '\033[92m'
    BTYELLOW = '\033[93m'
    BTRED = '\033[91m'
    BTWHITE = '\033[97m'

    # normal background colors
    BLACKBG = '\033[40m'
    REDBG = '\033[41m'
    GREENBG = '\033[42m'
    YELLOWBG = '\033[43m'
    BLUEBG = '\033[44m'
    MAGENTABG = '\033[45m'
    CYANBG = '\033[46m'
    WHITEBG = '\033[47m'

    # bright background colors
    BTBLACKBG = '\033[100m'
    BTREDBG = '\033[101m'
    BTGREENBG = '\033[102m'
    BTYELLOWBG = '\033[103m'
    BTBLUEBG = '\033[104m'
    BTMAGENTABG = '\033[105m'
    BTCYANBG = '\033[106m'
    BTWHITEBG = '\033[107m'

    # control
    DEFAULTFG = '\033[39m'
    DEFAULTBT = '\033[49m'
    RESET = '\033[0m' # resets fg and bg
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # blender names
    WARNING = BTYELLOW 
    FAIL = BTRED
    OKBLUE = BTBLUE
    OKCYAN = BTCYAN
    OKGREEN = BTGREEN
    HEADER = BTMAGENTA
    ENDC = RESET

def testANSI(c):
    fgEscs = [
        # normal
        c.BLACK,
        c.RED,
        c.GREEN,
        c.YELLOW,
        c.BLUE,
        c.MAGENTA,
        c.CYAN,
        c.WHITE,

        # bright
        c.BTBLACK,
        c.BTRED,
        c.BTGREEN,
        c.BTYELLOW,
        c.BTBLUE,
        c.BTMAGENTA,
        c.BTCYAN,
        c.BTWHITE,
    ]

    total = ""
    for i, esc in enumerate(fgEscs):
        # add newline after 8 colors
        if i == 8:
            total = total + "\n"
        total = total + f"{esc}██{c.ENDC}"
    print(total)

def rgbANSI(r, g, b):
    # rgb foreground ansi esc
    return f"\033[38;2;{r};{g};{b}m"

def rgbgANSI(r, g, b):
    # rgb background ansi esc
    return f"\033[48;2;{r};{g};{b}m"

# 4 color gradient
def RGBtestANSI(c):
    block = "█"
    block30 = block*30
    block120 = block*120
    
    loopBlock = block30
    for i in range(255):
        bw = f"{rgbANSI(i,i,i)}{loopBlock}{c.ENDC}"
        r = f"{rgbANSI(i,0,0)}{loopBlock}{c.ENDC}"
        g = f"{rgbANSI(0,i,0)}{loopBlock}{c.ENDC}"
        b = f"{rgbANSI(0,0,i)}{loopBlock}{c.ENDC}"
        print(f"{bw}{r}{g}{b}")

# france flag gradient
def french(c):
    block = "█"
    block40 = block*40
    block120 = block*120
    
    loopBlock = block40
    for i in range(255):
        w = f"{rgbANSI(i,i,i)}{loopBlock}{c.ENDC}"
        r = f"{rgbANSI(i,0,0)}{loopBlock}{c.ENDC}"
        b = f"{rgbANSI(0,0,i)}{loopBlock}{c.ENDC}"
        print(f"{b}{w}{r}")





print(f"{c.BTBLUEBG}btblue background{c.ENDC}")

print(f"{rgbANSI(0,255,128)}rgb ansi{c.ENDC}")
print(f"{rgbgANSI(128,0,255)}rgb background{c.ENDC}")
print(f"{rgbgANSI(128,0,255)}{rgbANSI(255,255,0)}rgb background and foreground{c.ENDC}")

testANSI(c)
RGBtestANSI(c)
french(c)