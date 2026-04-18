"""
1. Ask for sentences in corpus
    - strip spaces
    - append with <s> and </s> --> process_input_sentence()
    - add to corpus --> create_corpus()
2. Create unigram counts
2. Create bigram counts
"""

from utils import create_corpus, create_unigram_counts, create_bigram_counts, compute_unsmoothed_unigram, compute_unsmoothed_bigram, print_type_token_counts, print_corpus

def main():
    corpus_length = int(input("Enter the length of corpus (no. of sentences): "))

    corpus = create_corpus(number_of_sentences=corpus_length)
    print_corpus(corpus=corpus)

    unigram_counts = create_unigram_counts(corpus=corpus)
    print_type_token_counts(n_gram_counts=unigram_counts, name="unigram")

    bigram_counts = create_bigram_counts(corpus=corpus)
    print_type_token_counts(n_gram_counts=bigram_counts, name="bigram")

    is_compute_unigram = input("Do you want to compute unsmoothed unigram? [y/n]: ").strip() == "y"
    if is_compute_unigram:
        token = input("Please provide the token (should be there in corpus): ")
        p = compute_unsmoothed_unigram(unigram_counts=unigram_counts, token=token)

        print(f"P({token}) = {p:.2f}")
    

    is_compute_bigram = input("Do you want to compute unsmoothed bigram? [y/n]: ").strip() == "y"
    if is_compute_bigram:
        bi_token_raw = input("Please provide the bigram token (ex. Sam|ham): ").strip()
        bi_token_lst = bi_token_raw.split("|")
        bi_token_lst.reverse()

        if len(bi_token_lst) != 2:
            bi_token_lst.insert(0, "<s>")
        
        p = compute_unsmoothed_bigram(unigram_counts=unigram_counts, bigram_counts=bigram_counts, token_lst=bi_token_lst)

        print(f"P({bi_token_raw}) = {p}")



if __name__ == "__main__":
    main()