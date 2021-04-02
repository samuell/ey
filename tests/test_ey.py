import os
from pytest import fail
import sys
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ey

def test_replace_ports():
    task = ey.ShellTask('', inputs={'gz': 'data/chrmt.fa.gz'})
    for cmdpattern, expected_cmd, expected_temp_cmd in [
            (
                'wget -O [o:fasta:chrmt.fa]',
                'wget -O chrmt.fa',
                'wget -O chrmt.fa.tmp'
            ),
            (
                'wget -O [o:fasta:[i:gz]]',
                'wget -O data/chrmt.fa.gz',
                'wget -O data/chrmt.fa.gz.tmp'
            ),
            (
                'zcat [i:gz] > [o:fasta:[i:gz|%.gz]]',
                'zcat data/chrmt.fa.gz > data/chrmt.fa',
                'zcat data/chrmt.fa.gz > data/chrmt.fa.tmp'
            ),
            (
                'zcat [i:gz] > [o:fasta:[i:gz|basename|%.gz]]',
                'zcat data/chrmt.fa.gz > chrmt.fa',
                'zcat data/chrmt.fa.gz > chrmt.fa.tmp'
            ),
            (
                'zcat [i:gz] > [o:fasta:[i:gz|%.gz|basename]]',
                'zcat data/chrmt.fa.gz > chrmt.fa',
                'zcat data/chrmt.fa.gz > chrmt.fa.tmp'
            )
        ]:
        cmd, temp_cmd = task._replace_ports(cmdpattern)
        if cmd != expected_cmd:
            fail('Expected command: "{expected}", but got "{actual}"'.format(
                expected=expected_cmd,
                actual=cmd
            ))
        if temp_cmd != expected_temp_cmd:
            fail('Expected temp command: "{expected}", but got "{actual}"'.format(
                expected=expected_temp_cmd,
                actual=temp_cmd
            ))


def test_ey_shell():
    ey.shell('wget -O [o:gz:/tmp/chrmt.fa.gz] ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz')
    if not os.path.isfile('/tmp/chrmt.fa.gz'):
        fail('download did not succeed')

    os.remove('/tmp/chrmt.fa.gz')


def test_ey_func():
    def write_file(task):
        with open(task.outputs['out'], 'w') as outfile:
            outfile.write('test-output\n')

    ey.func(write_file, outputs={'out': '/tmp/output.txt'})

    if not os.path.isfile('/tmp/output.txt'):
        fail('writing of file in ey.func() did not succeed')

    os.remove('/tmp/output.txt')
