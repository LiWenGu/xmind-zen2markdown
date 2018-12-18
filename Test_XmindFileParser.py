import unittest

import pprint

from XmindFileParser import XmindFileParser


class TestXmindFileParser(unittest.TestCase):

    def test_unzip(self):
        content = XmindFileParser.parse("/Users/liwenguang/Documents/个人学习.xmind")
        pprint.pprint(content[0]["rootTopic"]["title"])


if __name__ == '__main__':
    unittest.main()