import subprocess
import getpass

# shcmder by Manny Berrueta

def nix_sudo_sh(pwd: str, cmd: str):
    if pwd == "" or cmd == "":
        print("Need to pass in password and command for sudo shell")
        return "need pwd"

    try:
        print(cmd.split())
        nix_shell = subprocess.Popen(["sudo"] + cmd.split(),
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True,
                                     bufsize=0).communicate(pwd)
        stdout, err = nix_shell
        if err:
            print(err)
            return err
        else:
            print(stdout)
            return stdout
        
    except Exception as e:
        print(e)


def nix_sh(cmd: str):
    if cmd == "":
        print("Need to pass in a valid command for shell")
        return "need pwd"

    try:
        nix_shell = subprocess.Popen(cmd.split(),
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True,
                                     bufsize=0)
        stdout, err = nix_shell.communicate()
        
        if nix_shell.returncode != 0:
            print(err)
            return err
        else:
            print(stdout)
            return stdout
        
    except Exception as e:
        print(e)
