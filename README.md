# Ey

A super-simple library for performing stepwise batch tasks that saves things to
files, such that outputs from already finished tasks are not needlessly
re-computed.

## Prerequisites

- Ey is so far only tested on unix-like environments.

## Installation

Install from the Python Package Index using pip:

```
pip install ey
```

## Example:

Below is a small example that downloads a gzipped text file (in the so called
FASTA format), and un-gzips it:

```python
import ey

# Download a gzipped fasta file and save it as chrmt.fa.gz
url = 'ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.MT.fa.gz'
gz = ey.shell('wget -O [o:gz:chrmt.fa.gz] '+url)

# Un-GZip the file, into a file named chrmt.fa
fa = ey.shell('zcat [i:gz] > [o:fa:[i:gz|%.gz]]',
        inputs={'gz': gz.outputs['gz']})
```

Add this code to a file named `download_fasta.py` and run it with:

```bash
python download_fasta.py
```
