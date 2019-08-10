def frequency(message: str) -> dict:
    """
    :param message:
    :return:
    :rtype: dict
    """
    ret = {}
    for key in message:
        if key in ret:
            ret[key] += 1
        else:
            ret[key] = 1
    return ret
# TODO: Create functions that run through the top (6) most frequent chars, xors and check to see if the xor'd string
#  is all chars and whitespace
# Remember, the most common character in a line of text is the space: ascii 32. if you have a char with a frequency
#  higher than 12%, it's probably a chr(32)
