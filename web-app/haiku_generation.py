import random
import nltk
from nltk.corpus import wordnet as wn
import re

nltk.download('wordnet')
nltk.download('omw-1.4')

def get_related_words(theme):
    """Fetch words related to the theme using WordNet."""
    related_words = set()
    for synset in wn.synsets(theme):
        # direct synonyms
        for lemma in synset.lemmas():
            word = lemma.name().replace('_', ' ')
            if word.isalpha():
                related_words.add(word)
                
            # synonyms of synonyms
            for related_syn in wn.synsets(lemma.name()):
                for related_lemma in related_syn.lemmas():
                    rword = related_lemma.name().replace('_', ' ')
                    if rword.isalpha():
                        related_words.add(rword)

        #hypernyms 
        for hypernym in synset.hypernyms():
            for lemma in hypernym.lemmas():
                hword = lemma.name().replace('_', ' ')
                if hword.isalpha():
                    related_words.add(hword)
                    
    return list(related_words)


def count_syllables(word):
    """check syllables by counting vowel groups."""
    word = word.lower()
    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))

def generate_line(words, target_syllables):
    """Generate a line with a target syllable count."""
    line = []
    syllable_count = 0
    tries = 0
    while syllable_count < target_syllables and tries < 100: # just to make sure it will produce a faulty sentence rather than infinite loop in edgecases, usually wont happen with 5 and 7
        word = random.choice(words)
        word_syllables = count_syllables(word)
        if syllable_count + word_syllables <= target_syllables:
            line.append(word)
            syllable_count += word_syllables
        tries += 1
    return ' '.join(line)

def generate_haiku(theme):
    """Generate a 5-7-5 haiku based on a theme."""
    words = get_related_words(theme)
    if not words:
        print(f"No related words found for '{theme}'. Using fallback words.")
        words = ["wind", "moon", "star", "dream", "sky", "light", "tree", "river"] #can add more

    common_words = [
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'with',
        'without', 'upon', 'for', 'to', 'of', 'is', 'was', 'be', 'are' 
    ]
    words = words + common_words
    
    line1 = generate_line(words, 5)
    line2 = generate_line(words, 7)
    line3 = generate_line(words, 5)
    return f"{line1}\n{line2}\n{line3}"

if __name__ == "__main__":
    theme = input("Enter a theme for the haiku: ").strip()
    haiku = generate_haiku(theme)
    print("\nHere is your haiku:\n")
    print(haiku)
