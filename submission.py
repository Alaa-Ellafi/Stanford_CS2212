import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in
the sparse vector, while the values represent the elements at those positions.
Any key which is absent from the dict means that that element in the sparse
vector is absent (is zero).
Note that the type of the key used should not affect the algorithm. You can
imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors,
but it should work the same way with arbitrary keys (e.g., "red", "blue", 
"green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 4a

def find_alphabetically_first_word(text: str) -> str:
    """
    Given a string |text|, return the word in |text| that comes first
    lexicographically (i.e., the word that would come first after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find min() handy here. If the input text is an empty string,
    it is acceptable to either return an empty string or throw an error.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    words = text.split()
    return min(words)
    # END_YOUR_CODE


############################################################
# Problem 4b

def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    distance = math.sqrt((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)
    return distance
    # END_YOUR_CODE


############################################################
# Problem 4c

def mutate_sentences(sentence: str) -> List[str]:

    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
# BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    out =[sentence]
    words= sentence.split()
    n = len(words)
    words = words[:-1]
    for i in range(n-1):
        nbr=sentence.count(words[i])
        if nbr > 1:
            indices = [k for k, word in enumerate(words) if word == words[i]]
            for j in range(len(indices)-1):
                similars= words[indices[j]+1:indices[j+1]] + words[indices[j]:indices[j+1]+1] +words[indices[j]+1:-1]
                s =0
                while s + n < len(similars):
                        similar = ' '.join(similars[s:s+n])
                        out.append(similar)
                        s+= 1
    out = list(set(out))
    return out
out = mutate_sentences('the cat and the mouse')
out = list(set(out))
print(out)

# END_YOUR_CODE


############################################################
# Problem 4d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros)
    |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    result = 0
    for key in v1:
        result += v1[key]*v2[key]
    return result
    # END_YOUR_CODE


############################################################
# Problem 4e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector,
) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for key in v2:
        v1[key]= v1[key]+scale* v2[key]
    return v1


    
    # END_YOUR_CODE


############################################################
# Problem 4f

def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of words that
    occur more than once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    word_count = collections.defaultdict(int)
    for word in text.split():
        word_count[word] += 1
    return {word for word, count in word_count.items() if count > 1}

    # END_YOUR_CODE
