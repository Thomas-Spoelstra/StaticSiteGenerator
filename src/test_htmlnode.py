import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        tag = "h1"
        children = "children"
        self.assertEqual
        (
            f"Tag: {tag}\nValue: None\nChildren: {children}\nProps: None", 
            "Tag: h1\nValue: None\nChildren: children\nProps: None"
            )

    def test_repr_all_none(self):
        self.assertEqual
        (
            "Tag: None\nValue: None\nChildren: None\nProps: None", 
            "Tag: None\nValue: None\nChildren: None\nProps: None"
            )
        
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        props = node.props_to_html()

        self.assertEqual(props, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_more_nodes(self):
        node1 = HTMLNode(props=None)
        node2 = HTMLNode(props={"href": "https://google.com"})
        node3 = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        node4 = HTMLNode(props={"href": "https://google.com", "target": "_blank", "visited": "true"})

        (
            self.assertTrue(node1, "") 
            and self.assertTrue(node2, "href=\"https://google.com\"") 
            and self.assertTrue(node3, "href=\"https://google.com\" target=\"_blank\"")
            and self.assertTrue(node4, "href=\"https://google.com\" target=\"_blank\" visited=\true\"")
            )

if __name__ == "__main__":
    unittest.main()