import platform
import socket


def print_system():

    print("=" * 60)
    print("SYSTEM INFORMATION")
    print("=" * 60)

    print("OS        :", platform.system())
    print("Release   :", platform.release())
    print("Version   :", platform.version())
    print("Machine   :", platform.machine())
    print("Hostname  :", socket.gethostname())
    print("IP        :", socket.gethostbyname(socket.gethostname()))

    print()