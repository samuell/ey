import ey
import os.path
from pytest import fail

def test_replace_ports():
    task = ey.ShellTask('', inputs={'gz': 'chrmt.fa.gz'})
    for input, expected in [
            (
                'wget -O [o:fasta:chrmt.fa]',
                'wget -O chrmt.fa'
            ),
            (
                'wget -O [o:fasta:[i:gz]]',
                'wget -O chrmt.fa.gz'
            ),
            (
                'zcat [i:gz] > [o:fasta:[i:gz|%.gz]]',
                'zcat chrmt.fa.gz > chrmt.fa'
            )
        ]:
        output = task._replace_ports(input)
        if output != expected:
            fail('Expected "{expected}", but got "{actual}"'.format(
                expected=expected,
                actual=output
            ))

def test_ey():
    gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz')
    if not os.path.isfile('chrmt.fa.gz'):
        fail('download did not succeed')
