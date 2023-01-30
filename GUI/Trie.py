class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        node = self.root
        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True
    
    global values
    values = []

    def suggestionsword(self, node, word):
        if node.last:
            values.append(word)
        for a, n in node.children.items():
            self.suggestionsword(n, word + a)
        return values
    def AutoSuggestions(self, key):
        node = self.root
        global values
        for a in key:
            if not node.children.get(a):
                values = []
                return 0
            node = node.children[a]
            values = []
        if not node.children:
            values = []
            return -1

        return self.suggestionsword(node, key)