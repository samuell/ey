import ey

# ------------------------------------------------------------------------
# Download a gzipped fasta file and save it as chrmt.fa.gz
# ------------------------------------------------------------------------
url = 'ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz'
download_task = ey.shell('wget -O [o:gz:chrmt.fa.gz] '+url)

# ------------------------------------------------------------------------
# Un-GZip the file, into a file named chrmt.fa
# ------------------------------------------------------------------------
ungzip_task = ey.shell('zcat [i:gz] > [o:fa:[i:gz|%.gz]]',
        inputs={'gz': download_task.outputs['gz']})

# ------------------------------------------------------------------------
# Count the fraction of G+C, vs G+C+A+T
# ------------------------------------------------------------------------
# A function for Count GC fraction in DNA
def count_gcfrac_func(task):
    gc_count = 0
    at_count = 0

    with open(task.inputs['fa']) as infile:
        for line in infile:
            if line[0] == '>':
                continue
            for char in line:
                if char in ['A', 'T']:
                    at_count += 1
                elif char in ['G', 'C']:
                    gc_count += 1

    gc_fraction = gc_count/(gc_count+at_count)

    with open(task.outputs['gcfrac'], 'w') as outfile:
        outfile.write(str(gc_fraction) + '\n')

# Execute the function
count_task = ey.func(count_gcfrac_func,
        inputs={'fa': ungzip_task.outputs['fa']},
        outputs={'gcfrac': 'gcfrac.txt'})
