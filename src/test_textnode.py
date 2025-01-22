import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr_url_none(self):
        text = "test"
        text_type = "bold"
        self.assertEqual(f"TextNode({text}, {text_type}, {None})", "TextNode(test, bold, None)")

    def test_repr_default_case(self):
        text = "test"
        text_type = "bold"
        url = "https://www.github.com"
        self.assertEqual(f"TextNode({text}, {text_type}, {url})", "TextNode(test, bold, https://www.github.com)")

    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        faulty_node = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, faulty_node)


if __name__ == "__main__":
    unittest.main()