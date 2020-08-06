import ey
from pytest import fail

def test_replace_ports():
    for input, expected in [
            (
                'wget -O [o:fasta:chry.fa]',
                'wget -O chry.fa'
            )
        ]:
        output = ey.__replace_ports(input)
        if output != expected:
            fail('output not as expected')

#def test_ey():
#    fasta = ey.shell(cmd)
#    with open(fasta.out('fasta')) as fafile:
#        for line in fafile:
#            print(line)
