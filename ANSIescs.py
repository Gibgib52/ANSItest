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

def rgbANSI(r, g, b):
    # rgb foreground ansi esc
    return f"\033[38;2;{r};{g};{b}m"

def rgbgANSI(r, g, b):
    # rgb background ansi esc
    return f"\033[48;2;{r};{g};{b}m"

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
