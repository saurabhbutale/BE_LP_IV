from mrjob.job import MRJob
import re

class MRCharCount(MRJob):
    
    # Regular expression to match alphabetic characters
    WORD_RE = re.compile(r'[a-zA-Z]')
    
    # Mapper function
    def mapper(self, _, line):
        # For each character in the line, check if it is alphabetic
        for char in line:
            if char.isalpha():
                # Emit the lowercase of the alphabetic character and count 1
                yield char.lower(), 1
    
    # Reducer function
    def reducer(self, char, counts):
        # Sum all the counts for a particular character
        yield char, sum(counts)

if __name__ == '__main__':
    MRCharCount.run()
