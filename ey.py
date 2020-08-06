import subprocess as sp
import re

def shell(cmd):
    cmd = __replace_ports(cmd)
    out = sp.run(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, check=True, shell=True)
    return TaskInfo(out)

def __replace_ports(cmd):
    ms = re.findall(r'(\[o\:([a-z]*):([a-z\.]*)\])', cmd, flags=re.S)
    for m in ms:
        cmd = cmd.replace(m[0], m[2])
    return cmd

class TaskInfo:
    def __init__(self, cmdout):
        self.args = cmdout.args
        self.returncode = cmdout.returncode
        self.stdout = cmdout.stdout
        self.stderr = cmdout.stderr

    def out(self, portname):
        return 'untitled.txt'
