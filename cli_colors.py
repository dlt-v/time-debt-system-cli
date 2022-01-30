class cli_colors():
    HDR = '\033[95m'  # header color
    OKB = '\033[94m'  # okay blue
    OKC = '\033[96m'  # okay cyan
    OKG = '\033[92m'  # okay green
    WRN = '\033[31m'  # warning red
    CMT = '\033[93m'  # comment orange
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLR = '\033[0m'  # clear color

    def clear(self):
        print(self.CLR)
