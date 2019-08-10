import binascii as ba


def xor_hex(str1, str2):
    try:
        if len(str2) != len(str1):
            raise ValueError('Length of strings is not equal')
        bstr1 = ba.a2b_hex(str1)
        bstr2 = ba.a2b_hex(str2)
        tmp = [chr(bstr1[x] ^ bstr2[x]) for x in range(len(bstr1))]
        outstr = ba.a2b_qp("".join(tmp))
    except Exception as e:
        raise e

    return ba.b2a_hex(outstr)
