
paragraph = "Python is useful and Python is powerful"


def count_words(paragraph):
    space_count = 0
    for char in paragraph:
        if char == " ":
            space_count += 1
    return space_count + 1


def count_characters_without_spaces(paragraph):
    count = 0
    for char in paragraph:
        if char != " ":
            count += 1
    return count


def count_vowels_and_consonants(paragraph):
    vowel_letters = ["a", "e", "i", "o", "u"]
    vowels = 0
    consonants = 0

    for char in paragraph:
        if char.isalpha():
            if char.lower() in vowel_letters:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


def longest_word(paragraph):
    list_of_words = paragraph.split()
    longest = ""

    for word in list_of_words:
        if len(word) > len(longest):
            longest = word

    return longest


def repeated_words(paragraph):
    repeated = []
    list_of_words = paragraph.split()

    for word in list_of_words:
        count = 0

        for other_word in list_of_words:
            if word.lower() == other_word.lower():
                count += 1

        lowercase_words = []

        for w in repeated:
            lowercase_words.append(w.lower())

        if count > 1 and word.lower() not in lowercase_words:
            repeated.append(word)

    return repeated


if __name__ == "__main__":
    print(f"Total words in this paragraph are {count_words(paragraph)}")

    print(
        f"Total characters without spaces in this paragraph "
        f"is {count_characters_without_spaces(paragraph)}"
    )

    vowels, consonants = count_vowels_and_consonants(paragraph)
    print(
        f"There are {vowels} vowels and {consonants} consonants "
        f"in this paragraph"
    )

    print(f"The longest word in this paragraph is {longest_word(paragraph)}")

    print(f"Repeated words in this paragraph are {repeated_words(paragraph)}")
    print(f"All the words are listed only once except {repeated_words(paragraph)[0]} and {repeated_words(paragraph)[1]}")