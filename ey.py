import subprocess as sp
import re

def shell(cmd):
    cmd = __replace_ports(cmd)
    out = sp.run(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, check=True, shell=True)
    return TaskInfo()

def __replace_ports(cmd):
    ms = re.findall(r'\[o\:([a-z]*):([a-z]*)\]', cmd, flags=re.S)
    import pdb; pdb.set_trace()
    return cmd

class TaskInfo:
    def out(self, portname):
        return 'untitled.txt'
