# Description:
# This script is used to decode url.
# Usage: python urlCoder.py <url> <e/d>
# we try to do it without use library like urllib

# Author: Milad Shaker
# Lindin: https://www.linkedin.com/in/milad-shaker-ba7ab6141/
# Github: https://github.com/miladshakerdn/simple-tools

import re

# decode url without use library
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

# url encode without use library
def url_encode(url):
    ''' Encode a URL string.
    >>> url_encode('abc def')
    '''
    res = ''
    protocol = ''
    pattern = r"(?::\/\/((?:[^\/]*\/)*(?:[^\/]*)))"
    match = re.search(pattern, url)
    if match:
        protocol = url.split(match.group(1))[0]
        url = match.group(1)
    for c in url:
        if c.isalnum():
            res += c
        else:
            res += '%%%02X' % ord(c)
    return protocol + res

###############################################
## clone urllib algoritm
###############################################
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


url = 'https://www.google.com/fdfb fsv https://'
if  __name__ == '__main__':
    print(url_encode(url))
    # now we have bad output
    # https://www%2Egoogle%2Ecom%2Ffdfb%20fsv%20https%3A%2F%2F
    # good output is:
    # https://www.google.com/fdfb%20fsv%20https%3A%2F%2F
    # fix it after