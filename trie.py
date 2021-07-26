import collections


class TrieNode:
    def __init__(self):
        self.child=collections.defaultdict(TrieNode)
        self.is_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for i in word:
            curr=curr.child[i]
        curr.is_word=True

    def search(self,word):
        curr=self.root
        for i in word:
            curr=curr.child.get(i)
            if not curr:
                return False
        return curr.is_word
    def startsWith(self,prefix):
        curr=self.root
        for i in prefix:
            curr=curr.child.get(i)
            if curr is None:
                return False
        return True




