import ey

gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz')

fa = ey.shell('zcat [i:gz] > [o:fa:[i:gz|%.gz]]',
        inputs={'gz': gz.outputs['gz']})
