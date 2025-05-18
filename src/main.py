from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from tkinter import Tk, filedialog
import random
import os
import time
import subprocess
import platform
import textwrap

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

bloody_colors = ["#7e0000", "#8a0000", "#990000", "#a60000", "#b30000", "#c00000", "#cc0000", "#d90000", "#e60000"]

ascii_art = """
▒███████▒▓█████  ██▀███   ▒█████    ██████  ██ ▄█▀ ██▓▓█████▄ ▒███████▒
▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒  ██▄█▒ ▓██▒▒██▀ ██▌▒ ▒ ▒ ▄▀░
░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▓███▄░ ▒██▒░██   █▌░ ▒ ▄▀▒░ 
  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░  ▒   ██▒▓██ █▄ ░██░░▓█▄   ▌  ▄▀▒   ░
▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒▒██▒ █▄░██░░▒████▓ ▒███████▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓   ▒▒▓  ▒ ░▒▒ ▓░▒░▒
░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░░ ░▒ ▒░ ▒ ░ ░ ▒  ▒ ░░▒ ▒ ░ ▒
░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░  ░ ░░ ░  ▒ ░ ░ ░  ░ ░ ░ ░ ░ ░
  ░ ░       ░  ░   ░         ░ ░        ░  ░  ░    ░     ░      ░ ░    
░                                                      ░      ░        
"""

def print_ascii():
    ascii_lines = ascii_art.strip("\n").split("\n")
    gradient_text = Text()
    for line in ascii_lines:
        color = random.choice(bloody_colors)
        gradient_text.append(line + "\n", style=color)
    console.print(gradient_text)

def show_menu():
    panel = Panel.fit(
        "[bold cyan][1][/bold cyan] Obfuscate\n"
        "[bold cyan][2][/bold cyan] Credits and info\n"
        "[bold cyan][3][/bold cyan] Exit\n\n"
        "[bold white]Select option:[/bold white]",
        title="[red]ZeroSkids Menu", border_style="red"
    )
    console.print(panel)

def open_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select file to obfuscate")
    root.destroy()
    return file_path

def save_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".py", title="Save obfuscated file as")
    root.destroy()
    return file_path

def open_folder(path):
    if platform.system() == "Windows":
        subprocess.run(['explorer', '/select,', os.path.normpath(path)])
    elif platform.system() == "Darwin":
        subprocess.run(['open', '-R', path])
    else:
        subprocess.run(['xdg-open', os.path.dirname(path)])

def ultra_skid_obfuscator(code: str) -> str:
    func_chunks = []
    func_defs = []
    idx = 0

    for char in code:
        hex_code = f"0x{ord(char):02x}"
        func_name = f"_x{idx}"
        func_defs.append(f"def {func_name}(): return chr({hex_code})")
        func_chunks.append(f"{func_name}()")
        idx += 1

    final_code_call = "+".join(func_chunks)
    code_block = "\n".join(func_defs + [f"exec(" + final_code_call + ")"])
    hexified = code_block.encode("utf-8").hex()

    loader = textwrap.dedent(f"""\
    import binascii
    exec(binascii.unhexlify("{hexified}").decode("utf-8"))
    """)
    return loader

def obfuscate_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        original_code = f.read()
    console.print("[cyan]Obfuscating...[/cyan]")
    time.sleep(1)
    obfuscated = ultra_skid_obfuscator(original_code)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Obfuscated by ZeroSkids\n" + obfuscated)
    console.print(f"[green]✅ Obfuscated and saved to:[/green] {output_path}")
    open_folder(output_path)

# main loop
while True:
    clear_terminal()
    print_ascii()
    show_menu()
    choice = Prompt.ask("Your choice", choices=["1", "2", "3"], default="1")

    if choice == "1":
        clear_terminal()
        console.print("[yellow bold]>> Select a file to obfuscate[/yellow bold]")
        file_path = open_file_dialog()
        if not file_path:
            console.print("[red]No file selected.[/red]")
            Prompt.ask("\n[bold cyan]Press Enter to return to menu[/bold cyan]")
            continue

        clear_terminal()
        console.print(f"[yellow bold]>> Save your obfuscated file[/yellow bold]")
        save_path = save_file_dialog()
        if not save_path:
            console.print("[red]No save location provided.[/red]")
            Prompt.ask("\n[bold cyan]Press Enter to return to menu[/bold cyan]")
            continue

        clear_terminal()
        obfuscate_file(file_path, save_path)
        Prompt.ask("\n[bold cyan]Press Enter to return to menu[/bold cyan]")

    elif choice == "2":
        clear_terminal()
        console.print(Panel(
            "[magenta]Made by:[/magenta]\n"
            "🧠 Skidzz – chaos queen\n"
            "😈 Skit – backend menace\n"
            "🤖 Ryn – totally real person\n",
            title="Credits", border_style="magenta"
        ))
        Prompt.ask("\n[bold cyan]Press Enter to return to menu[/bold cyan]")

    else:
        clear_terminal()
        console.print("[red bold]Peace out skiddy 🥀[/red bold]")
        break
