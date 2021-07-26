from Bio import SeqIO
dna = list(SeqIO.parse('/share/SARS-class/SARS-2020.fasta', 'fasta'))

for frame in range(3):

  p = dna[0][frame:].translate().seq

  prots = p.split('*')

  for i in prots:
    if(len(i) > 100):
      b = p.find(i)
      e = b + len(i)
      print(frame, i, b, e)

