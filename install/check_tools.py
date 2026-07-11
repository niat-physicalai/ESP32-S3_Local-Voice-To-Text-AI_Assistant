from utils import command_exists


TOOLS = {
    "Python": "python",
    "Git": "git",
    "Arduino CLI": "arduino-cli",
    "Ollama": "ollama"
}


def check():

    print("=" * 60)
    print("CHECKING TOOLS")
    print("=" * 60)

    for name, cmd in TOOLS.items():

        if command_exists(cmd):
            print(f"[OK]   {name}")

        else:
            print(f"[MISS] {name}")

    print()