from ps4b import *
import string
#
# Test code
#Created by: Arti
#Updated by: 
# Date created: 6, 7 Mar 2017
# Date Last updated: 
    
def test_message_build_shift_dict():
    """
    Unit test for build_shift_dict
    """
    failure=False
    msg = Message('')
    
    # test 1
    
    shift = 4
    expected_dict = {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i',\
                     'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n',\
                     'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's',\
                     'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x', \
                     'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c', 'z': 'd',\
                     'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I',\
                     'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N',\
                     'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S',\
                     'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X',\
                     'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C', 'Z': 'D'}
    actual_dict = msg.build_shift_dict(shift)
    
    if expected_dict != actual_dict:
        print("FAILURE: test_message_build_shift_dict()")
        print("Expected dictionary:", expected_dict)
        print("Returned dictionary:", actual_dict)
        failure=True
        
    # test 2
    
    shift = 0
    expected_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',\
                     'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',\
                     'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',\
                     'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',\
                     'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z',\
                     'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E',\
                     'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J',\
                     'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O',\
                     'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T',\
                     'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
    actual_dict = msg.build_shift_dict(shift)
    
    if expected_dict != actual_dict:
        print("FAILURE: test_message_build_shift_dict()")
        print("Expected dictionary:", expected_dict)
        print("Returned dictionary:", actual_dict)
        failure=True
        
    # test 3
    
    shift = 25
    expected_dict = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g',\
                     'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o',\
                     'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w',\
                     'y': 'x', 'z': 'y', 'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E',\
                     'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M',\
                     'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U',\
                     'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'}
    actual_dict = msg.build_shift_dict(shift)
    
    if expected_dict != actual_dict:
        print("FAILURE: test_message_build_shift_dict()")
        print("Expected dictionary:", expected_dict)
        print("Returned dictionary:", actual_dict)
        failure=True
        
    # test 4
    
    shift = 30
    expected_dict = {'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i',\
                     'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n',\
                     'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's',\
                     'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x', \
                     'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c', 'z': 'd',\
                     'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I',\
                     'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N',\
                     'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S',\
                     'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X',\
                     'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C', 'Z': 'D'}
    actual_dict = msg.build_shift_dict(shift)
    
    if expected_dict != actual_dict:
        print("FAILURE: test_message_build_shift_dict()")
        print("Expected dictionary:", expected_dict)
        print("Returned dictionary:", actual_dict)
        failure=True
        
    # test 5
    
    shift = -4
    expected_dict = {'a': 'w', 'b': 'x', 'c': 'y', 'd': 'z', 'e': 'a', 'f': 'b', 'g': 'c', 'h': 'd', 'i': 'e', 'j': 'f', 'k': 'g', 'l': 'h', 'm': 'i', 'n': 'j', 'o': 'k', 'p': 'l', 'q': 'm', 'r': 'n', 's': 'o', 't': 'p', 'u': 'q', 'v': 'r', 'w': 's', 'x': 't', 'y': 'u', 'z': 'v', 'A': 'W', 'B': 'X', 'C': 'Y', 'D': 'Z', 'E': 'A', 'F': 'B', 'G': 'C', 'H': 'D', 'I': 'E', 'J': 'F', 'K': 'G', 'L': 'H', 'M': 'I', 'N': 'J', 'O': 'K', 'P': 'L', 'Q': 'M', 'R': 'N', 'S': 'O', 'T': 'P', 'U': 'Q', 'V': 'R', 'W': 'S', 'X': 'T', 'Y': 'U', 'Z': 'V'}
    actual_dict = msg.build_shift_dict(shift)
    
    if expected_dict != actual_dict:
        print("FAILURE: test_message_build_shift_dict()")
        print("Expected dictionary:", expected_dict)
        print("Returned dictionary:", actual_dict)
        failure=True
        
    if not failure:
        print("SUCCESS: test_message_build_shift_dict()")

# end of test_message_build_shift_dict

def test_message_apply_shift():
    """
    Unit test for apply_shift
    """
    failure=False
    
    messages = [("Hello, World!", 4, "Lipps, Asvph!"),\
                ("abcdef", 2, "cdefgh"), ("!@#$ &(5", 12, "!@#$ &(5")]
    
    for (text, shift, exp_msg) in messages:
        msg = Message(text)
        shifted_msg = msg.apply_shift(shift)
        
        if(shifted_msg != exp_msg):
            print("FAILURE: test_message_apply_shift()")
            print("Expected message: " + exp_msg + "but output is: " + shifted_msg)
            failure=True
    
    if not failure:
        print("SUCCESS: test_message_apply_shift()")

# end of test_message_apply_shift

def test_ciphertextMessage_decrypt_message():
    """
    Unit test for decrypt_message
    """
    failure=False
    
    messages = [("Lipps, Asvph!", 22, "Hello, World!"),
                ("Jgnnq", 24, "Hello"),
                ("Mr xlmw pigxyvi,", 22, "In this lecture,"),
                ("He has been registered for classes at MIT twice before, but has reportedly never passed aclass.", 0, "He has been registered for classes at MIT twice before, but has reportedly never passed aclass."),
                ("Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy.", 12, "Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack.")]
    
    for (text, shift, exp_msg) in messages:
        ciphertext = CiphertextMessage(text)
        shifted_msg = ciphertext.decrypt_message()
        
        if(shifted_msg != (shift, exp_msg)):
            print("FAILURE: test_ciphertextMessage_decrypt_message()")
            print(shift)
            print("Expected message: '" + exp_msg + "' but output is: '" + shifted_msg[1] + "'")
            failure=True
    
    if not failure:
        print("SUCCESS: test_ciphertextMessage_decrypt_message()")

# end of test_ciphertextMessage_decrypt_message

print("----------------------------------------------------------------------")
print("Testing Message-build_shift_dict...")
test_message_build_shift_dict()
print("----------------------------------------------------------------------")
print("Testing Message-apply_shift...")
test_message_apply_shift()
print("----------------------------------------------------------------------")
print("Testing CiphertextMessage-decrypt_message...")
test_ciphertextMessage_decrypt_message()