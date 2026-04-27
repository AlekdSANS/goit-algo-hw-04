import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

PIPE = "|   "
TEE = "|-- "
LAST = "--- "
BLANK = "    "

def visualize(path: Path, prefix: str = "") -> None:
    entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

    for index, entry in enumerate(entries):
        connector = LAST if index == len(entries) - 1 else TEE

        if entry.is_dir():
            print(
                f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT}{entry.name}/"
            )
            extension = BLANK if index == len(entries) - 1 else PIPE
            visualize(entry, prefix + extension)
        else:
            print(
                f"{prefix}{connector}{Fore.GREEN}{entry.name}"
            )

def main() -> None:
    if len(sys.argv) != 2:
        print(
            f"{Fore.RED}Використання: python script3.py <шлях до директорії> (ex. python Dz_matsafei/goit-algo-hw-04/ad3/script3.py Dz_matsafei/goit-algo-hw-04/ad3)"
        )
        sys.exit(1)

    target = Path(sys.argv[1])

    if not target.exists():
        print(
            f"{Fore.RED}Помилка: шлях '{target}' не існує."
        )
        sys.exit(1)

    if not target.is_dir():
        print(
            f"{Fore.RED}Помилка: '{target}' не є директорією."
        )
        sys.exit(1)

    print(
        f"{Fore.BLUE}{Style.BRIGHT}{target.name}/"
    )
    visualize(target)

if __name__ == "__main__":
    main()