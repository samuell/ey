import ey

# Download a gzipped fasta file and save it as chrmt.fa.gz
url = 'ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz'
gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] '+url)

# Un-GZip the file, into a file named chrmt.fa
fa = ey.shell('zcat [i:gz] > [o:fa:[i:gz|%.gz]]',
        inputs={'gz': gz.outputs['gz']})
