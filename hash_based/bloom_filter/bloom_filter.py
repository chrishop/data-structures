"""


https://en.wikipedia.org/wiki/Bloom_filter
"""

import math
from typing import Sized
import mmh3


class BloomFilter:
    
    def __init__(self, size, keys):
        '''
        size : int
            The length of the bit array
        keys : int
            How many hash functions are being used
        '''
        self.size = size
        self.keys = keys
        self.bit_array = [0 for _ in range(size)]
        
    def add(self, elem):
        for key_no in range(self.keys):
            index = mmh3.hash(elem, key_no) % self.size
            self.bit_array[index] = 1
            
    def check(self, elem):
        for key_no in range(self.keys):
            index = mmh3.hash(elem, key_no) % self.size
            if self.bit_array[index] != 1:
                return False
        return True
    

def main():
    print("*** spell checker for words beginning with A ***")
    print("loading ...")
    
    # optimised for 11616 sized set
    bloom_filter = BloomFilter(55670, 5)
    with open("hash_based/bloom_filter/Aword.csv", "r") as word_file:
        for line in word_file:
            stripped = line.strip()
            bloom_filter.add(stripped)
            
    running = True
    while running:
        print("> ", end="")
        entry = input()
        if entry == "q":
            running = False
        else:
            if bloom_filter.check(entry):
                print("I think that's a word beginning with A in english")
            else:
                print("That's not a word beginning with A in english")
    
    
    
    
if __name__ == "__main__":
    main()