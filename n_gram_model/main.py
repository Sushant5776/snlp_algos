"""
1. Ask for sentences in corpus
    - strip spaces
    - append with <s> and </s> --> process_input_sentence()
    - add to corpus --> create_corpus()
2. Create unigram counts
2. Create bigram counts
"""

from utils import create_corpus, create_unigram_counts, create_bigram_counts, print_type_token_counts, print_corpus

def main():
    corpus_length = int(input("Enter the length of corpus (no. of sentences): "))

    corpus = create_corpus(number_of_sentences=corpus_length)
    print_corpus(corpus=corpus)

    unigram_counts = create_unigram_counts(corpus=corpus)
    print_type_token_counts(n_gram_counts=unigram_counts, name="unigram")

    bigram_counts = create_bigram_counts(corpus=corpus)
    print_type_token_counts(n_gram_counts=bigram_counts, name="bigram")

if __name__ == "__main__":
    main()