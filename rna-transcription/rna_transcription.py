def to_rna(dna_strand):
    if dna_strand == "":
        return ""

    conversion = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    rna_strand = ""

    for char in dna_strand:
        for key, value in conversion.items():
            if char == key:
                rna_strand += value

    return rna_strand
