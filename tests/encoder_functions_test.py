#! /usr/bin/env python3

import unittest
import sys
#https://csatlas.com/python-import-file-module/
sys.path.append('src/')

import encoder_functions as ef

# from hypothesis import given
# from hypothesis.strategies import text

# class TestEncoding(unittest.TestCase):
#     """Generates test invariant via Hypothesis

#     Args:
#         unittest (_type_): _description_
#     """
#     @given(text())
#     def test_decode_inverts_encode(self, s):
#         self.assertEqual(ef.decode(ef.encode(s)), s)


# if __name__ == "__main__":
#     unittest.main()

from hypothesis import example, given, strategies as st


@given(st.text())
@example("")
def test_decode_inverts_encode(s):
    assert ef.decode(ef.encode(s)) == s