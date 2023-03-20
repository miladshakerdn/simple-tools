# Description:
# This script is used to decode/enconde url.
# Usage: python urlCoder.py <url> <e/d>
# we try to do it without use library like urllib

# Author: Milad Shaker
# Lindin: https://www.linkedin.com/in/milad-shaker-ba7ab6141/
# Github: https://github.com/miladshakerdn/simple-tools


import re

# decode url without use urllib
def url_decode(s):
    ''' Decode a URL encoded string.
    >>> url_decode('abc%20def')
    this algoritm reformated from https://rosettacode.org/wiki/URL_decoding to python
    '''
    r = ''
    i = 0
    while i < len(s):
        if s[i] == '%':
            b = []
            while i < len(s) and s[i] == '%':
                i += 1
                b.append(int(s[i:i+2], 16))
                i += 2
            r += bytes(b).decode('utf-8')
        else:
            r += s[i]
            i += 1
    return r

# clone unquote to bytes with urllib algoritm
def unquote_to_bytes(string):
    _hexdig = '0123456789ABCDEFabcdef'
    _hextobyte = None
    """unquote_to_bytes('abc%20def') -> b'abc def'."""
    # Note: strings are encoded as UTF-8. This is only an issue if it contains
    # unescaped non-ASCII characters, which URIs should not.
    if not string:
        # Is it a string-like object?
        string.split
        return b''
    if isinstance(string, str):
        string = string.encode('utf-8')
    bits = string.split(b'%')
    if len(bits) == 1:
        return string
    res = [bits[0]]
    append = res.append
    # Delay the initialization of the table to not waste memory
    # if the function is never called
    if _hextobyte is None:
        _hextobyte = {(a + b).encode(): bytes.fromhex(a + b)
                      for a in _hexdig for b in _hexdig}
    for item in bits[1:]:
        try:
            append(_hextobyte[item[:2]])
            append(item[2:])
        except KeyError:
            append(b'%')
            append(item)
    return b''.join(res)

# clone decode url with urllib algoritm
def url_decode_urllib_algoritm(url, encoding='utf-8', errors='replace'):
    _asciire = re.compile('([\x00-\x7f]+)')
    bits = _asciire.split(url)
    res = [bits[0]]
    append = res.append
    for i in range(1, len(bits), 2):
        append(unquote_to_bytes(bits[i]).decode(encoding, errors))
        append(bits[i + 1])
    return ''.join(res)


url = 'https://www.google.com/search?client=firefox-b-d&q=%D8%AA%D8%B3%D8%AA+%D9%85%D8%B1%D9%88%D8%B1%DA%AF%D8%B1+firefox'
if  __name__ == '__main__':
    print(url_decode(url))