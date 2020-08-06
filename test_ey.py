import ey
import os.path
from pytest import fail

def test_replace_ports():
    task = ey.ShellTask('', inputs={'gz': 'chrmt.fa.gz'})
    for cmdpattern, expected_cmd, expected_temp_cmd in [
            (
                'wget -O [o:fasta:chrmt.fa]',
                'wget -O chrmt.fa',
                'wget -O chrmt.fa.tmp'
            ),
            (
                'wget -O [o:fasta:[i:gz]]',
                'wget -O chrmt.fa.gz',
                'wget -O chrmt.fa.gz.tmp'
            ),
            (
                'zcat [i:gz] > [o:fasta:[i:gz|%.gz]]',
                'zcat chrmt.fa.gz > chrmt.fa',
                'zcat chrmt.fa.gz > chrmt.fa.tmp'
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

def test_ey():
    gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz')
    if not os.path.isfile('chrmt.fa.gz'):
        fail('download did not succeed')
