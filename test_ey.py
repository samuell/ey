import ey

def test_ey():
    fasta = ey.shell('wget -O [o:fasta:chry.fa] ftp://ftp.ensembl.org/pub/release-67/fasta/homo_sapiens/dna/Homo_sapiens.GRCh37.67.dna_rm.chromosome.Y.fa.gz')
    with open(fasta.out('fasta')) as fafile:
        for line in fafile:
            print(line)
