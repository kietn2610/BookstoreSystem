import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def print_expression(self, s: str) -> str:
        t = ''
        num = ''
        if not self.matched_expression(s):
            raise Exception()
        else:
            t += s
            for character in t:
                if character.isalpha():
                    if self.dict.find(character) is None:
                        pass
                    else:
                        num = str(self.dict.find(character))
                        t = t.replace(character, num)
            return t

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.push(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if stack.n == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str: #edit
        t = BinaryTree.BinaryTree()
        t.r = t.Node('')
        u = t.r
        for token in exp:
            if token == '(':
                u = u.insert_left()
            elif token in ['+', '-', '*', '/', '*']:
                u.x = token
                u = u.insert_right()
            elif token == ')':
                u = u.parent
            elif token.isalpha():
                u.x = token
                u = u.parent
        return t

    def _evaluate(self, u): #edit
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left is not None and u.right is not None:
            fn = op[u.x]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        else:
            t = self.dict.find(u.x)
            if t is not None:
                return t
            return u.x

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            return 0

'''
s = Calculator()
print(s.print_expression("((a*b)+(c*d))"))
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
print(s.print_expression("((a*b)+(c*d))"))
'''