import sys
from pathlib import Path
from colorama import Fore, Style, Back, init

# Ініціалізація Colorama
init(autoreset=True)


def folder_tree(folder_path: Path, indent: str = ""):
    try:
        for i in folder_path.iterdir():
            if i.is_dir():
                print(f"{indent}{Fore.GREEN + Style.BRIGHT + str(i.name)}/")
                # Додаємо відступ для вкладених папок
                folder_tree(i, indent + "  ")
            else:
                print(f"{indent}{Fore.YELLOW + str(i.name)}")  # Файли
    except Exception as mistake:
        print(f"{Fore.RED} Mistake: {mistake}")
        return


def main():
    if len(sys.argv) <= 1:
        print(
            f"{Style.BRIGHT}{Back.LIGHTRED_EX} Using: python colorama_3.py [way/to/dir]")
        sys.exit(1)

    folder_path = Path(sys.argv[1])

    # Перевірка існування шляху
    if not folder_path.exists():
        print(f"{Style.BRIGHT}{Back.LIGHTRED_EX} Direction {folder_path} not exist")
        sys.exit(1)

    # Перевірка, чи це директорія
    if not folder_path.is_dir():
        print(f"{Style.BRIGHT}{Back.LIGHTRED_EX}{folder_path} not a direction")
        sys.exit(1)

    # Виклик функції для друку дерева
    folder_tree(folder_path)


if __name__ == "__main__":
    main()
