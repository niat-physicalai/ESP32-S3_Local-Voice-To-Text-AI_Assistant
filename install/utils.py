import shutil
import subprocess

from logger import log


def command_exists(command):
    return shutil.which(command) is not None


def run(command):

    log(f"> {command}")

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.stdout:
        log(result.stdout.strip())

    if result.stderr:
        log(result.stderr.strip())

    return result

# import shutil
# import subprocess


# def command_exists(command):
#     return shutil.which(command) is not None


# def run(command):
#     print(f"> {command}")

#     result = subprocess.run(
#         command,
#         shell=True,
#         text=True,
#         capture_output=True
#     )

#     return result