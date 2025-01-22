from textnode import TextNode
from textnode import TextType

def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textnode)

main()