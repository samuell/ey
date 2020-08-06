import ey

# Download a gzipped fasta file and save it as chrmt.fa.gz
url = 'ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz'
gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] '+url)

# Un-GZip the file, into a file named chrmt.fa
fa = ey.shell('zcat [i:gz] > [o:fa:[i:gz|%.gz]]', inputs={'gz': gz.outputs['gz']})

# Count GC fraction in DNA
def count_gcfrac(task):
    gc = 0
    at = 0
    with open(task.inputs['fa']) as fa:
        for l in fa:
            if l[0] == '>':
                continue
            for c in l:
                if c in ['A', 'T']:
                    at += 1
                elif c in ['G', 'C']:
                    gc += 1
    with open(task.outputs['gcfrac'], 'w') as countfile:
        countfile.write(str(gc/(gc+at)) + '\n')

ct = ey.func(count_gcfrac,
        inputs={'fa': fa.outputs['fa']},
        outputs={'gcfrac': 'gcfrac.txt'})
