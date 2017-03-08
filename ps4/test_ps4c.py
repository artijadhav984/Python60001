from ps4c import *
import string
#
# Test code
#Created by: Arti
#Updated by: 
# Date created: 7 Mar 2017
# Date Last updated: 
    
def test_subMessage_build_transpose_dict():
    """
    Unit test for build_transpose_dict
    """
    failure=False
    subMsg = SubMessage('')
    
    vowel_dict = {}
    consonants_dict = {}
    
    for char in CONSONANTS_LOWER + CONSONANTS_UPPER:
        consonants_dict[char] = char
                       
    permutations = {'eaiuo': {'a': 'e', 'A': 'E', 'e': 'a', 'E': 'A', 'i': 'i', 'I': 'I', 'o': 'u', 'O': 'U', 'u': 'o', 'U': 'O', 'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                    'eouai': {'a': 'e', 'A': 'E', 'e': 'o', 'E': 'O', 'i': 'u', 'I': 'U', 'o': 'a', 'O': 'A', 'u': 'i', 'U': 'I', 'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                    'eoai': {'a': 'e', 'A': 'E', 'e': 'o', 'E': 'O', 'i': 'a', 'I': 'A', 'o': 'i', 'O': 'I', 'u': 'u', 'U': 'U', 'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                    'uoiea': {'a': 'u', 'A': 'U', 'e': 'o', 'E': 'O', 'i': 'i', 'I': 'I', 'o': 'e', 'O': 'E', 'u': 'a', 'U': 'A', 'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                    'aeiou': {'a': 'a', 'A': 'A', 'e': 'e', 'E': 'E', 'i': 'i', 'I': 'I', 'o': 'o', 'O': 'O', 'u': 'u', 'U': 'U', 'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}}
    
    for key in permutations.keys():
        transpose_dict = subMsg.build_transpose_dict(key)
        
        if permutations[key] != transpose_dict:
            print("FAILURE: test_subMessage_build_transpose_dict()")
            print("Expected dictionary: " + permutations[key] + "but output is: " + transpose_dict)
            failure=True
        
    if not failure:
        print("SUCCESS: test_subMessage_build_transpose_dict()")

# end of test_subMessage_build_transpose_dict

def test_subMessage_apply_transpose():
    """
    Unit test for apply_transpose
    """
    failure=False
    
    messages = [("Hello, World!", 'eaiuo', "Hallu, Wurld!"),
                ("He has been registered for classes at MIT twice before, but has reportedly never passed aclass.", 'eouai', "Ho hes boon rogustorod far clessos et MUT twuco bofaro, bit hes ropartodly novor pessod ecless."),
                ("abcdef", 'eoai', "ebcdof"), ("!@#$ &(5", 'uoiea', "!@#$ &(5"),
                ("Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.", 'aeiou', "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.")]
    
    for (text, vowels_permutation, exp_msg) in messages:
        subMsg = SubMessage(text)
        transpose_dict = subMsg.build_transpose_dict(vowels_permutation)
        encoded_msg = subMsg.apply_transpose(transpose_dict)
        
        if(encoded_msg != exp_msg):
            print("FAILURE: test_subMessage_apply_transpose()")
            print("Expected message: " + exp_msg + " but output is: " + encoded_msg)
            failure=True
    
    if not failure:
        print("SUCCESS: test_subMessage_apply_transpose()")

# end of test_subMessage_apply_transpose
#
def test_encryptedSubMessage_decrypt_message():
    """
    Unit test for decrypt_message
    """
    failure=False
    
    messages = {"Hallu, Wurld!": "Hello, World!",
                "Ho hes boon rogustorod far clessos et MUT twuco bofaro, bit hes ropartodly novor pessod ecless." : "He has been registered for classes at MIT twice before, but has reportedly never passed aclass.", 
                "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack." : "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack."}
    
    for text in messages.keys():
        encryptedSubMsg = EncryptedSubMessage(text)
        decoded_msg = encryptedSubMsg.decrypt_message()
        
        if(decoded_msg != messages[text]):
            print("FAILURE: test_encryptedSubMessage_decrypt_message()")
            print("Expected message: '" + messages[text] + "' but output is: '" + decoded_msg + "'")
            failure=True
    
    if not failure:
        print("SUCCESS: test_encryptedSubMessage_decrypt_message()")

# end of test_ciphertextMessage_decrypt_message

print("----------------------------------------------------------------------")
print("Testing SubMessage-build_transpose_dict...")
test_subMessage_build_transpose_dict()
print("----------------------------------------------------------------------")
print("Testing SubMessage-apply_transpose...")
test_subMessage_apply_transpose()
print("----------------------------------------------------------------------")
print("Testing EncryptedSubMessage-decrypt_message...")
test_encryptedSubMessage_decrypt_message()