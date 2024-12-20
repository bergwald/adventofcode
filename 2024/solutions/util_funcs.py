from typing import List

def file_to_list(filename, sep="\n", maxsplit=-1) -> List[str]:
    """
    Read an input file and split it using sep as the delimiter.
    """
    with open(filename) as f:
        return f.read().rstrip().split(sep, maxsplit=maxsplit)