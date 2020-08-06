import subprocess as sp
import re
import os

def shell(cmd):
    task = ShellTask()
    task._init_from_command(cmd)
    task.execute()
    return task


class Task:
    pass


class ShellTask(Task):
    def __init__(self):
        self.outputs = {}
        self.inputs = {}
        self.command = ''

    # ------------------------------------------------
    # Public methods
    # ------------------------------------------------
    def out(self, portname):
        return 'untitled.txt'

    def execute(self):
        for name, path in self.outputs.items():
            if os.path.exists(path):
                print('File or folder already exists, so skipping: %s' % path)
                return

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
        # Out ports
        ms = re.findall(r'(\[o\:([a-z]*):([a-z\.]+)\])', cmd, flags=re.S)
        for m in ms:
            placeholder = m[0]
            portname = m[1]
            pathpattern = m[2]

            self.outputs[portname] = pathpattern
            cmd = cmd.replace(placeholder, pathpattern)

        return cmd
