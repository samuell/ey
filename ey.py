import subprocess as sp
import re
import os
import shutil

def shell(command, inputs={}):
    task = ShellTask(command, inputs)
    task.execute()
    return task


class Task:
    pass


class ShellTask(Task):
    def __init__(self, command, inputs={}):
        self.inputs = {}
        self.outputs = {}
        for name, path in inputs.items():
            self.inputs[name] = path
        self.command, self.temp_command = self._replace_ports(command)

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

        print('Executing command: %s' % self.command)
        out = sp.run(self.temp_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, check=True, shell=True)

        # Move paths from temp to final paths
        for _, path in self.outputs.items():
            shutil.move('%s.tmp' % path, path)

        self._add_cmd_results(out)

    # ------------------------------------------------
    # Internal methods
    # ------------------------------------------------
    def _add_cmd_results(self, cmdout):
        self.args = cmdout.args
        self.returncode = cmdout.returncode
        self.stdout = cmdout.stdout
        self.stderr = cmdout.stderr

    def _replace_ports(self, command):
        # In-ports
        ms = re.findall(r'(\[i\:([^:\]\|]*)(\|%([^\]]+))?\])', command, flags=re.S)
        for m in ms:
            placeholder = m[0]
            portname = m[1]
            path = self.inputs[portname]

            if m[3] != '':
                end_to_trim = m[3]
                path = path.replace(end_to_trim, '')

            command = command.replace(placeholder, path)

        # Out-ports
        temp_command = command
        ms = re.findall(r'(\[o\:([^:\]]*):([^:\]]+)\])', command, flags=re.S)
        for m in ms:
            placeholder = m[0]
            portname = m[1]
            path = m[2]
            self.outputs[portname] = path

            temppath = '%s.tmp' % path

            command = command.replace(placeholder, path)
            temp_command = temp_command.replace(placeholder, temppath)

        return command, temp_command
