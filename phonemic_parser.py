from collections import defaultdict #import dictionaries capable of implementing default values
import cmudict #import the CMU arpabet dictionary

#load CMUdict into a standard python dictionary and convert value list into space-separated strings
modifiedCMU = {key:' '.join(value_list) for key, value_list in cmudict.entries()}


#Further preprocess the dictionary by setting keys to phoneme sequences and values to homophones
def key_value_inverter(pronunciation_dict):
    inverted_dict = defaultdict(list) #initialize dictionary with default values as empty lists
    for word, phonemes in pronunciation_dict.items(): #iterate through all key/value pairs
        inverted_dict[phonemes].append(word) #set phonemic sequence as key and append associated words as values
    return inverted_dict
                                         
                                       
def phonemic_sequence_parser(pronunciation_dict, phonemes):
    result=[]
    def backtrack(start, path): #define brute force backtracking function
        if start == len(phonemes):  #base case - identify end of string
            result.append(path[:])  # Append a copy of the path to the result
            return
        for end in range(start + 1, len(phonemes) + 1): #iterate through input phonemes  
            phoneme_sequence = " ".join(phonemes[start:end])  # Convert list of phonemes to space-separated string
            if phoneme_sequence in pronunciation_dict:
                for word in pronunciation_dict[phoneme_sequence]:
                    path.append(word)
                    backtrack(end, path) #apply function recursively
                    path.pop() #remove current value from array
    backtrack(0, [])
    return result


invertedCMU = key_value_inverter(modifiedCMU)
input_phonemes1 = ["DH", "EH1", "R", "DH", "EH1", "R"]
parses = phonemic_sequence_parser(invertedCMU, input_phonemes2)
sorted(parses, key=len)

##Example output:  [["THEIR", "THEIR"], ["THEIR", "THERE"], ["THERE", "THEIR"], ["THERE", "THERE"]]).
