from sys import platform
from model.OperatingSystem import OS 
from model.CommandErrors import CommandErrors
import subprocess

class CMD:

    def __init__(self):
        self.os = self.get_OS()

    def get_OS(self):
        operating_system = OS.OTHERS
        if platform == "linux" or platform == "linux2":
            operating_system = OS.LINUX 
        elif platform == "darwin":
            operating_system = OS.APPLE 
        elif platform == "wins32":
            operating_system = OS.WINDOWS
        return operating_system

    def run_cmd(self, command):
        cmd_output = ""
        try:
            output = subprocess.run(command.split(" "), capture_output = True, text = True, check = True)
            cmd_output = output.stdout 
        except subprocess.TimeoutExpired as e:
            print(f"Timeout: {e}")
            cmd_output = CommandErrors.TIMEOUT
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            cmd_output = CommandErrors.CALLEDPROCESSERROR
        except FileNotFoundError as e:
            print(f"Command not found: {e}")
            cmd_output = CommandErrors.COMMANDNOTFOUND
        return cmd_output
