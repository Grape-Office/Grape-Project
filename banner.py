import random

import pyfiglet
from colorama import Fore, init


def banner(text="PodoCheong", width=120):
    init(autoreset=True)
    colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE]
    random_color = random.choice(colors)
    # available_fonts = pyfiglet.FigletFont.getFonts()
    # random_font = random.choice(available_fonts)
    ascii_art = pyfiglet.figlet_format(text, font='big', width=width)
    print(random_color + ascii_art)


if __name__ == "__main__":
    program_name = "PodoCheong"
    banner(program_name)
