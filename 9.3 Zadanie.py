def all_variants(text):
    for i in text:
        yield i
    b = len(text)
    for first in range(b):
        for last in range(first + 1, b+1):
            if last - first > 1:
                yield text[first:last]


a = all_variants("abc")
for i in a:
    print(i)
