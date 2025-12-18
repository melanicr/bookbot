def num_words(words):
    total = words.split()
    return len(total)


def counting(file_text):
    letter_count = {}

    for letter in file_text.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        elif letter in letter_count:
            letter_count[letter] += 1
    return letter_count

def helper(items):
    return items["count"]


def sorting(text):
    sorted_list = []

    for key, value in text.items():
        sorted_list.append({
            "word": key,
            "count": value
        })
    sorted_list.sort(key=lambda item: item["count"], reverse=True)
    return sorted_list