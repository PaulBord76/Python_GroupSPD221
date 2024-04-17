str = "The shortest word in the sentence"
def shortest_word_length(s: str) -> int:
    """
        Функция принимает на вход строку из слов и возвращает длину кратчайшего слова.

        :param s: Строка из слов
        :type s: str
        :return: Длина кратчайшего слова
        :rtype: int
        """
    words = s.split()
    shortest_length = min(len(word) for word in words)
    return shortest_length

print(shortest_word_length(str))