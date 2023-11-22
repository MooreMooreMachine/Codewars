def generate_hashtag(s: str):
    list_of_words = s.split()
    list_of_words.insert(0, '#')
    output_string = ''
    for index in range(0, len(list_of_words)):
        list_of_words[index] = list_of_words[index].capitalize()
        output_string += list_of_words[index]
    if len(output_string) > 140 or len(s) == 0:
        return False
    else:
        return output_string

print(generate_hashtag(''))





