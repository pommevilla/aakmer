valid_aas = "ARNDCQEGHILKMFPSTWVY"
valid_nucls = "ACGT"


def get_kmer_dict(s: str, k: int, mode: str = "aa") -> dict:
    """
    Returns a dictionary of count of k-mers found in s
    """
    correct_characters = valid_aas if mode == "aa" else valid_nucls

    kmer_dict = {}
    for i in range(len(s) - k + 1):
        kmer = s[i : i + k]
        kmer_dict[kmer] = kmer_dict.get(kmer, 0) + 1
    return kmer_dict
