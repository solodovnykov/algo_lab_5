def AlgorythmKMP(text, pattern):
    p = [0] * len(text)
    first_symbol = 0
    second_symbol = 1

    result = []

    while second_symbol < len(pattern):
        if pattern[first_symbol] == pattern[second_symbol]:
            p[second_symbol] = first_symbol + 1
            second_symbol += 1
            first_symbol += 1
        else:
            if first_symbol == 0:
                p[second_symbol] = 0
                second_symbol += 1
            else:
                first_symbol = p[first_symbol - 1]

    length_of_pattern = len(pattern)
    length_of_text = len(text)

    text_index = 0
    pattern_index = 0

    while text_index < length_of_text:
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
            if pattern_index == length_of_pattern:
                result = [(text_index - pattern_index), (text_index - 1)]

                return result
        else:
            if pattern_index > 0:
                pattern_index = p[pattern_index - 1]
            else:
                text_index += 1
    if text_index == length_of_text:
        return 'pattern not found'


pattern = 'lol'
text = 'olollllllll'

print(AlgorythmKMP(text, pattern))
