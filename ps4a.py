# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

from itertools import permutations

# code from https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

#    perms = [''.join(p) for p in permutations(sequence)]
#    return perms
#    print(perms)
    
    # If lst is empty then there are no permutations 
    if len(sequence) == 0: 
	    return [] 

	# If there is only one element in lst then, only 
	# one permuatation is possible 
    if len(sequence) == 1: 
	    return [sequence] 

	# Find the permutations for lst if there are 
	# more than 1 characters 

    l = [] # empty list that will store current permutation 

	# Iterate the input(sequence) and calculate the permutation 
    for i in range(len(sequence)): 
        m = sequence[i] 

	# Extract sequence[i] or m from the sequence. remLst is 
	# remaining list 
        remLst = sequence[:i] + sequence[i+1:] 

	# Generating all permutations where m is first 
	# element 
        for p in get_permutations(remLst): 
            l.append(m + p) 
    return l 


        

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

