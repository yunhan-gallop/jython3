"""
	This is not an exhaustive pulldom test suite.
	Instead, it is a place to put jython-specific tests,
	relating to bugs like this one, for example.

	"xml.dom.Node.data returns bytestrings of decoded unicode"
	http://bugs.jython.org/issue1583

	amak.
"""

import io
import unittest
from xml.dom import pulldom
from test import support

class UnicodeTests(unittest.TestCase):

    testDoc = """\
<?xml version="1.0" encoding="ascii"?>
<document>
    <p>Some greek: &#x391;&#x392;&#x393;&#x394;&#x395;</p>
    <greek attrs="&#x396;&#x397;&#x398;&#x399;&#x39a;"/>
    <?greek &#x39b;&#x39c;&#x39d;&#x39e;&#x39f;?>
    <!--&#x39b;&#x39c;&#x39d;&#x39e;&#x39f;-->
</document>
"""

    def setUp(self):
        self.testFile = io.StringIO(self.testDoc)

    def testTextNodes(self):
        text = []
        for event, node in pulldom.parse(self.testFile):
            if event == pulldom.CHARACTERS:
                text.append(node.data)
        try:
            result = "".join(text)
            self.assertEqual(repr(result), r"u'\n    Some greek: \u0391\u0392\u0393\u0394\u0395\n    \n    \n    \n'")
        except Exception as x:
            self.fail("Unexpected exception joining text pieces: %s" % str(x))

    def testAttributes(self):
        attrText = []
        for event, node in pulldom.parse(self.testFile):
            if event == pulldom.START_ELEMENT:
                for attrIx in range(node.attributes.length):
                    attrText.append(node.attributes.item(attrIx).value)
        try:
            result = "".join(attrText)
            self.assertEqual(repr(result), r"u'\u0396\u0397\u0398\u0399\u039a'")
        except Exception as x:
            self.fail("Unexpected exception joining attribute text pieces: %s" % str(x))

    def testProcessingInstruction(self):
        piText = []
        for event, node in pulldom.parse(self.testFile):
            if event == pulldom.PROCESSING_INSTRUCTION:
                piText.append(node.data)
        try:
            result = "".join(piText)
            # Weird how the repr for PI data is different from text and char data.
            # Still, the whole xml.dom.* and xml.sax.* hierarchy is rather a 
            # labyrinthine mess under jython, mostly because it's so old, and
            # yet survived through major evolutionary changes in both jython and java.
            self.assertEqual(repr(result), r"u'&#x39b;&#x39c;&#x39d;&#x39e;&#x39f;'")
        except Exception as x:
            self.fail("Unexpected exception joining pi data pieces: %s" % str(x))

    def testComment(self):
        commentText = []
        for event, node in pulldom.parse(self.testFile):
            if event == pulldom.COMMENT:
                commentText.append(node.data)
        try:
            result = "".join(commentText)
            self.assertEqual(repr(result), r"u'&#x39b;&#x39c;&#x39d;&#x39e;&#x39f;'")
        except Exception as x:
            self.fail("Unexpected exception joining comment data pieces: %s" % str(x))

def test_main():
    support.run_unittest(__name__)

if __name__ == "__main__":
    test_main()
