#-*- coding:utf-8 -*-
'''
Created on 2017年5月8日

@author: huangjiaxin
'''
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num = 0
    for i in dna:
        if i == nucleotide:
            num += 1
    return num


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return (dna2 in dna1)


def is_valid_sequence(dna):
    """(str) -> bool
    The parameter is a potential DNA sequence. Return True if and only if the DNA sequence 
    is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). 
    """
    FC = "ATCG"
    for i in dna:
        if i not in FC:
            return False
    return True
    
    
def insert_sequence(dna1, dna2, ind):
    """(str, str, int) -> str
    The first two parameters are DNA sequences and the third parameter is an index. Return the 
    DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. 
    """
    if ind > len(dna1):
        return dna1 + dna2
    if ind < 1:
        return dna2 + dna1
    return dna1[:ind] + dna2 + dna1[ind:]


def get_complement(nu):
    """(str) -> str
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement.
    """
    if nu == 'A':
        return 'T'
    elif nu == 'T':
        return 'A'
    elif nu == 'C':
        return 'G'
    elif nu == 'G':
        return 'C'
    

def get_complementary_sequence(dna):
    """(str) -> str
    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.
    """
    CS = ''
    for i in dna:
        CS += get_complement(i)
    return CS

