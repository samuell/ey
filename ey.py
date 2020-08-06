import subprocess as sp
import re

def shell(cmd):
    task = ShellTask()
    task._init_from_command(cmd)
    task.execute()
    return task


class Task:
    pass


class ShellTask(Task):
    # ------------------------------------------------
    # Public methods
    # ------------------------------------------------
    def out(self, portname):
        return 'untitled.txt'

    def execute(self):
        out = sp.run(self.command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, check=True, shell=True)
        self._add_cmd_results(out)

    # ------------------------------------------------
    # Internal methods
    # ------------------------------------------------
    def _init_from_command(self, cmd):
        self.command = self._replace_ports(cmd)

    def _add_cmd_results(self, cmdout):
        self.args = cmdout.args
        self.returncode = cmdout.returncode
        self.stdout = cmdout.stdout
        self.stderr = cmdout.stderr

    def _replace_ports(self, cmd):
        ms = re.findall(r'(\[o\:([a-z]*):([a-z\.]*)\])', cmd, flags=re.S)
        for m in ms:
            cmd = cmd.replace(m[0], m[2])
        return cmd
