import os
import ctypes
import sys
import subprocess
import time
from pystyle import Colors, Colorate, Center, Box, Write

# Проверка прав администратора
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print(Colorate.Error("[!] Запустите программу от имени администратора!"))
    input("Нажмите Enter для выхода...")
    sys.exit(1)

# ASCII-арт
def print_banner():
    banner = r"""
  ██████╗ ███████╗███████╗██████╗  ██████╗ ██████╗ ████████╗██╗███╗   ███╗██╗███████╗███████╗
  ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║████╗ ████║██║╚════██║╚════██║
  ██║  ██║█████╗  █████╗  ██████╔╝██║   ██║██████╔╝   ██║   ██║██╔████╔██║██║    ██╔╝    ██╔╝
  ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝ ██║   ██║██╔═══╝    ██║   ██║██║╚██╔╝██║██║   ██╔╝     ██╔╝ 
  ██████╔╝███████╗███████╗██║     ╚██████╔╝██║        ██║   ██║██║ ╚═╝ ██║██║   ██║      ██║  
  ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝      ╚═╝  
    """
    colored_banner = Colorate.Horizontal(Colors.blue_to_purple, banner, 1)
    print(Center.XCenter(colored_banner))
    print("\n")
    print(Center.XCenter(Colorate.Horizontal(Colors.blue_to_purple, ">>> DeepOptimize - Максимальная оптимизация Windows <<<", 1)))
    print("\n")

# Оптимизация Windows
def optimize_windows():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    optimizations = [
        ("Отключение индексирования поиска", 'sc config "WSearch" start= disabled'),
        ("Отключение гибернации", 'powercfg -h off'),
        ("Очистка кэша DNS", 'ipconfig /flushdns'),
        ("Очистка временных файлов", 'del /s /q %temp%\\*'),
        ("Оптимизация диска", 'defrag /C /H /V'),
        ("Отключение телеметрии", 'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f'),
        ("Отключение игрового режима", 'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\GameDVR" /v "AllowGameDVR" /t REG_DWORD /d 0 /f'),
        ("Оптимизация питания для максимальной производительности", 'powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'),
        ("Отключение ненужных служб", 'sc stop "DiagTrack" & sc config "DiagTrack" start= disabled'),
        ("Оптимизация параметров сети", 'netsh int tcp set global autotuninglevel=restricted')
    ]
    
    for desc, cmd in optimizations:
        Write.Print(f"[*] {desc}...\n", Colors.blue_to_purple, interval=0.02)
        try:
            if cmd.startswith('reg'):
                subprocess.run(cmd, shell=True, check=True)
            else:
                subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            Write.Print(f"[+] Успешно: {desc}\n\n", Colors.green_to_cyan, interval=0.02)
        except subprocess.CalledProcessError as e:
            Write.Print(f"[-] Ошибка при {desc}: {e}\n\n", Colors.red_to_yellow, interval=0.02)
        time.sleep(0.5)
    
    Write.Print("\n[!] Дополнительные рекомендации:\n", Colors.purple_to_blue, interval=0.02)
    tips = [
        "1. Отключите визуальные эффекты в 'Система > Дополнительные параметры системы > Быстродействие'",
        "2. Удалите ненужные программы из автозагрузки (Task Manager > Startup)",
        "3. Обновите драйверы оборудования",
        "4. Проверьте систему на вирусы с помощью антивируса"
    ]
    
    for tip in tips:
        Write.Print(f"{tip}\n", Colors.blue_to_purple, interval=0.02)
    
    Write.Print("\n[+] Оптимизация завершена! Рекомендуется перезагрузить компьютер.\n", Colors.green_to_cyan, interval=0.02)
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    optimize_windows()