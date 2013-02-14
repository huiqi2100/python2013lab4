# Filename: compress.py
# Author: Koh Hui Qi
# Date created: 14 Feb 2013
# Description: Compress large textual documents

# http://rosettacode.org/wiki/LZW_compression#Python

def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

try:
    infile = open("flintstones.txt", 'r')
    lines = infile.readlines()
    for line in lines:
        compressed = compress(line)
        print(compressed)

except IOError:
    print("ERROR! Unable to read file")

