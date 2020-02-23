# Forked from NanoFG
### https://github.com/SdeBlank/NanoFG.git

### NanoFG is a complete pipeline that process Nanopore/Pac-Bio Long-Reads to detect fusion genes.

To date, minor changes to the original NanoFG pipelines:
  - maf-convert.mod.py: utilities from LAST tool, update for python3 compatibility.
  - RegionSelection.py: regions provided as BED file format; reads isolated by pybedtools.
  - mv paths.ini > paths.config

## INSTALL

### clone repository from GitHub
```
git clone https://github.com/andreagrioni/NanoFG.git
cd NanoFG
```
### create anaconda environment
anaconda environment can be created from the environment.yml file.
Note that The first line of the yml file sets the new environment's name.
```
conda env create -f environment.yml
```
### config file
Update the path.config file with absolute paths for tools and reference genome.

## How to run
```
bash NanoFG.sh -f </path/to/fastqdir>  [-n SAMPLE_NAME ] [-r REGIONS] [-cf] [-cc] [-df] [-dc]
```
OR
```
bash NanoFG.sh -b </path/to/bam> [-v </path/to/vcf>] [-n SAMPLE_NAME ] [-r REGIONS] [-cf] [-cc] [-df] [-dc]
```

# Citation
*Original* NanoFG project at https://github.com/SdeBlank/NanoFG/wiki

*Original* citation: https://www.biorxiv.org/content/10.1101/807545v2

## Required Tools:

### Samtools (1.7) - http://samtools.sourceforge.net/
_Li, H. et al. The Sequence Alignment/Map format and SAMtools. Bioinformatics 25, 2078–2079 (2009)._
### Minimap2 (2.6) - https://github.com/lh3/minimap2
_Li, H. (2018). Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics, 34:3094-3100._

### LAST (921) - http://last.cbrc.jp/doc/last.html
_Kielbasa, S. M., Wan, R., Sato, K., Horton, P. & Frith, M. C. Adaptive seeds tame genomic sequence comparison. Genome Research 21, 487–493 (2011)._

### NanoSV (1.2.4) - https://github.com/mroosmalen/nanosv
_Cretu Stancu, M. et al. Mapping and phasing of structural variation in patient genomes using nanopore sequencing. Nat. Commun. 8, 1326 (2017)._

### Wtdbg2 (2.2) - https://github.com/ruanjue/wtdbg2 
_Ruan, J. and Li, H. (2019) Fast and accurate long-read assembly with wtdbg2. Nat Methods_

### pybedtools (0.8.0) - http://daler.github.io/pybedtools/index.html
