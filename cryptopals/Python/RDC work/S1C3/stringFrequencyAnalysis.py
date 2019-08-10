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
