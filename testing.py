import doctest
import itertools
import unittest
def rle(iterable):
    """Applies run-length encoding to an iterable.
    # doctest: +NORMALIZE_WHITESPACE - это директивы
    >>> list(rle(""))
    []
    >>> list(rle("mississippi"))
    [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1), ('p', 2), ('i', 1)]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)

# if __name__ == "__main__":
#     doctest.testmod()

    # ___________________assert___
# def test_rle():
#     s = "mississippi"
#     tmp = set(ch for ch, _count in rle(s))
#     assert tmp == set (s[:-1]+s[1])
#     assert not list(rle(""))

class test(unittest.TestCase):
    def test_rle (self):
        self.assertEqual(rle("mississippi"), [...])

    def test_rle_empty(self):
        self.assertEqual(list(rle("")),[])

if __name__ == "__main__":
    unittest.main()



