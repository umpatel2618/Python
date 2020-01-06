def to_rna(dna_strand):
    dic={'A':'U','C':'G','G':'C','T':'A'}
    rna=""
    for i in dna_strand:
        rna+=dic[i]
    return rna
to_rna("")
