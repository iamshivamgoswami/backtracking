import collections


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for i in word:
            curr = curr.child[i]
        curr.is_word = True


class Solution:
    def findWords(self, board, words):
        res = []
        t = Trie()
        for i in words:
            t.insert(i)
        curr = t.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, curr, i, j, "", res)
        return res

    def dfs(self, board, curr, i, j, path, res):
        if curr.is_word:
            res.append(path)
            curr.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == ".":
            return
        tmp = board[i][j]
        curr = curr.child.get(tmp)
        if not curr:
            return
        board[i][j] = "."
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            self.dfs(board, curr, x, y, path + tmp, res)
        board[i][j] = tmp




