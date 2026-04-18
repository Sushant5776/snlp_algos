from typing import List
from helpers import print_two_new_lines_before_and_after


def process_input_sentence(sentence: str):
    sentence = sentence.strip().lower()
    sentence = f"<s> {sentence} </s>"
    return sentence


def create_corpus(number_of_sentences: int) -> List[str]:
    corpus = []

    for i in range(number_of_sentences):
        sentence = input(f"Type Sentence {i + 1}: ")
        sentence = process_input_sentence(sentence=sentence)
        corpus.append(sentence)

    return corpus


def create_unigram_counts(corpus: List[str]):
    unigram_counts: dict[str, int] = {}

    flattened_corpus = " ".join(corpus)
    tokens = flattened_corpus.split()
    types = set(tokens)

    for type_ in types:
        type_appearance_count = tokens.count(type_)
        unigram_counts[type_] = type_appearance_count

    return unigram_counts


def create_bigram_counts(corpus: List[str]):
    bigram_counts: dict[str, int] = {}

    flattened_corpus = " ".join(corpus)

    for sentence in corpus:
        sentence_tokens = sentence.split()

        for i in range(len(sentence_tokens) - 1):
            bi_token = f"{sentence_tokens[i]} {sentence_tokens[i + 1]}"

            if bi_token in bigram_counts:
                continue

            bi_token_count = flattened_corpus.count(bi_token)
            bigram_counts[bi_token] = bi_token_count

    return bigram_counts


def compute_unsmoothed_unigram(unigram_counts: dict[str, int], token: str) -> float:
    N = sum(unigram_counts.values())
    p = unigram_counts[token] / N

    return p


def compute_unsmoothed_bigram(
    unigram_counts: dict[str, int], bigram_counts: dict[str, int], token_lst: List[str]
) -> float:
    bi_token = " ".join(token_lst)

    bi_token_count = bigram_counts[bi_token]
    history_count = unigram_counts[bi_token[0]]
    p = bi_token_count / history_count

    return p


@print_two_new_lines_before_and_after
def print_corpus(corpus: List[str]):
    print("-----Printing Corpus-----")
    for index, sentence in enumerate(corpus, start=1):
        print(f"Sentence {index}: {sentence}")
    print("-----Printed Corpus-----")


@print_two_new_lines_before_and_after
def print_type_token_counts(n_gram_counts: dict[str, int], name="unigram"):
    name = name.capitalize()

    print(f"-----Printing {name} Counts-----")

    for type_, count in n_gram_counts.items():
        print(f"Type: {type_}, Count: {count}")

    print(f"-----Printed {name} Counts-----")
