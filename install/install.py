from system_check import print_system
from check_tools import check


def banner():

    print("=" * 60)
    print("ESP32-S3 LOCAL VOICE AI INSTALLER")
    print("=" * 60)
    print()


def main():

    banner()

    print_system()

    check()

    print("Installer finished.")


if __name__ == "__main__":
    main()


# import platform
# import socket
# import sys


# def banner():
#     print("=" * 50)
#     print(" ESP32-S3 Local Voice AI Installer")
#     print("=" * 50)
#     print()


# def check_os():
#     print("[1] Operating System")

#     print(platform.system())
#     print(platform.release())
#     print(platform.version())

#     print()


# def check_python():
#     print("[2] Python")

#     print(sys.version)

#     print()


# def check_network():

#     print("[3] Network")

#     hostname = socket.gethostname()

#     ip = socket.gethostbyname(hostname)

#     print("Hostname :", hostname)
#     print("IP       :", ip)

#     print()


# def main():

#     banner()

#     check_os()

#     check_python()

#     check_network()

#     print("Installer started successfully.")


# if __name__ == "__main__":
#     main()