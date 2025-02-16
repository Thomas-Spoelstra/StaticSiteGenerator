from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    node1 = HTMLNode(props=None)
    node2 = HTMLNode(props={"href": "https://google.com"})
    node3 = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
    node4 = HTMLNode(props={"href": "https://google.com", "target": "_blank", "visited": "true"})

    node5 = LeafNode("p", "This is a paragraph of text.")
    node6 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(node1.props_to_html())
    print(node2.props_to_html())
    print(node3.props_to_html())
    print(node4.props_to_html())
    print(node5.to_html())
    print(node6.to_html())

main()