import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, input_path):
        """Given a single file, return text."""

        words = open(input_path).read()
        
        return words



    def make_chains(self, words):
        """Takes input text as string; stores chains."""

        chains = {}
        list_keys = words.split(" ")
        #looks at our long string and assigns key to bigrams from it, and assings value to the
        #next word after the bigram
        for i in range(len(list_keys) - 2):
            key = (list_keys[i], list_keys[i + 1])
            value = list_keys[i + 2]

            #puts the bigram and value into the dictionary
            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        # or we could say "chains.setdefault(key, []).append(value)"

        return chains

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys()) #makes a random choice from chains' keys, calls it keys
        words = [key[0], key[1]]#takes the ranndom choice and places it in a list by index
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)
  

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    input_path = sys.argv[1]
    # we should make an instance of the class
    markov = SimpleMarkovGenerator()
    # we should call the read_files method with the list of filenames
    words = markov.read_files(input_path)
    chains = markov.make_chains(words)
    # we should call the make_text method 5x
    for i in range(4):
        print markov.make_text(chains)
   

