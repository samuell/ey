# Ey

[![CircleCI](https://circleci.com/gh/samuell/ey.svg?style=shield)](https://app.circleci.com/pipelines/github/samuell/ey)
[![PyPI](https://img.shields.io/pypi/v/ey.svg?style=flat)](https://pypi.org/project/ey)

A super-simple library for performing stepwise batch tasks that saves things to
files, such that outputs from already finished tasks are not needlessly
re-computed. See the [below](#example) for an example.

Ey does not have a scheduler or central worker pool or anything like that. Instead
you simply execute your tasks manually in a procedural way. This way task executions
can easily be mixed with other procedural python code.

Ey can work as an alternative to full-blown workflow frameworks like Luigi or
Airflow for cases when you just have a single python script, where you want to
do a few batch steps before starting your interactive analysis, such as
downloading datasets, unpacking them, preprocessing et cetera.

Ey is small (not much more than 100 lines of code), and has no external
dependencies, meaning that you can even copy the implementation into your own
code repos if you want to ensure maximum future reproducibility.

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
