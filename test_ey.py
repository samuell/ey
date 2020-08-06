import ey
import os.path
from pytest import fail

def test_replace_ports():
    task = ey.Task()
    for input, expected in [
            (
                'wget -O [o:fasta:chrmt.fa]',
                'wget -O chrmt.fa'
            )
        ]:
        output = task._replace_ports(input)
        if output != expected:
            fail('output not as expected')

def test_ey():
    gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz')
    if not os.path.isfile('chrmt.fa.gz'):
        fail('download did not succeed')


