from dll import DoublyLinkedList as dll


def parens(string):
    """Test the parenthics of a unicode string."""
    dlink = dll()
    for letter in string:
        if letter == "(" or letter == ")":
            dlink.append(letter)
    while dlink.head is not None:
        if dlink.head.data == ")":
            return -1
        elif dlink.tail.data == "(":
            return 1
        else:
            dlink.pop()
            dlink.shift()
    return 0
