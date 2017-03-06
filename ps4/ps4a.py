# Problem Set 4A
# Name: Arti
# Collaborators:
# Time Spent: 1:00
# Created date: 6 Mar 2017
# Lst updted: 

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
    permutations = []
    
    # if it is single character
    if len(sequence) <= 1:
        permutations.append(sequence)
    else:
        # get the permutations for sunstring excluding first char
        sub_permutations = get_permutations(sequence[1:])
        
        # loop for every position in the string
        for i in range(len(sequence)):
            
            # loop for every permutations of substring
            for sub_sequence in sub_permutations:
                # form a word by placing first character in sub_sequence
                word = sub_sequence[: i] + sequence[0] + sub_sequence[i:]
                
                # append newly formed word if already not present in list
                if word not in permutations:
                    permutations.append(word)
                    
#    print('sequence: {}\npermutations: {}'.format(sequence, permutations))
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # check for single character word
#    example_input = 'i'
#    print('Input:', example_input)
#    print('Expected Output:', ['i'])
#    print('Actual Output:', get_permutations(example_input))

    # check for two characters word
#    example_input = 'it'
#    print('Input:', example_input)
#    print('Expected Output:', ['it', 'ti'])
#    print('Actual Output:', get_permutations(example_input))
    
    # check for three characters word
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
    # check for three characters word
#    example_input = 'pot'
#    print('Input:', example_input)
#    print('Expected Output:', ['pot', 'pto', 'opt', 'otp', 'tpo', 'top'])
#    print('Actual Output:', get_permutations(example_input))

    # check for empty string
#    example_input = ''
#    print('Input:', example_input)
#    print('Expected Output:', [''])
#    print('Actual Output:', get_permutations(example_input))

    # check for three characters word
#    example_input = 'ust'
#    print('Input:', example_input)
#    print('Expected Output:', ['ust', 'sut', 'stu', 'uts', 'tus', 'tsu'])
#    print('Actual Output:', get_permutations(example_input))
    
    # check for four characters word
    example_input = 'bust'
    print('Input:', example_input)
    print('Expected Output:',  ['bust', 'buts', 'bsut', 'btus', 'bstu', 'btsu', 'ubst', 'ubts', 'sbut', 'tbus', 'sbtu', 'tbsu', 'usbt', 'utbs', 'subt', 'tubs', 'stbu', 'tsbu', 'ustb', 'utsb', 'sutb', 'tusb', 'stub', 'tsub'])
    print('Actual Output:', get_permutations(example_input))
    
