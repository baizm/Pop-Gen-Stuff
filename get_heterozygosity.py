import sys
import re

in_file = sys.argv[1]
out_file = sys.argv[2]

f = open(in_file, 'r')
o = open(out_file, 'w')

for i in f:
        if re.search('^PSC', i):
                split=re.split('\t',i.strip())
                id=split[2]
                nRefHom=float(split[3])
                nNonRefHom=float(split[4])
                nHets=float(split[5])
                nSites=int(nRefHom+nNonRefHom+nHets)
                H=nHets/nSites
                o.write(id+'\t'+str(H)+'\t'+str(nSites)+'\n')

f.close()
o.close()

#usage: python get_heterozygosity.py fixed_sites_only_stats.txt heterozygosity.txt
#where fixed_sites_only_stats.txt takes the form of output from: bcftools stats -s -
