import subprocess as sp
import re

def shell(cmd):
    task = Task()
    task._init_from_command(cmd)

    out = sp.run(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, check=True, shell=True)
    task._add_cmd_results(out)

    return task


class Task:
    def __init__(self):
        pass

    # ------------------------------------------------
    # Public methods
    # ------------------------------------------------
    def out(self, portname):
        return 'untitled.txt'

    # ------------------------------------------------
    # Internal methods
    # ------------------------------------------------
    def _add_cmd_results(self, cmdout):
        self.args = cmdout.args
        self.returncode = cmdout.returncode
        self.stdout = cmdout.stdout
        self.stderr = cmdout.stderr

    def _init_from_command(self, cmd):
        cmd = self._replace_ports(cmd)

    def _replace_ports(self, cmd):
        ms = re.findall(r'(\[o\:([a-z]*):([a-z\.]*)\])', cmd, flags=re.S)
        for m in ms:
            cmd = cmd.replace(m[0], m[2])
        return cmd
