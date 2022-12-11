import subprocess
import getpass

# shcmder by Manny Berrueta

def nix_sudo_sh(cmd: str):
    if cmd == "":
        need_valid_cmd = "Need to pass in a valid command or program"
        print(need_valid_cmd)
        return need_valid_cmd

    try:
        print(cmd.split())
        nix_shell_proc = subprocess.Popen(["sudo"] + cmd.split(),
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True,
                                     bufsize=0)
        stdout, err = nix_shell_proc.communicate(getpass.getpass())
        
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
        need_valid_cmd = "Need to pass in a valid command or program"
        print(need_valid_cmd)
        return need_valid_cmd

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
