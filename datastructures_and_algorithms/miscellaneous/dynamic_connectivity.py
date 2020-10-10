"""PROBLEM STATEMENT:
Given a set of N objects.
・Union command: connect two objects.
・Find/connected query: is there a path connecting the two objects?
"""

__author__ = "Kanishk Varshney"
__data__ = "27-Sept-2020"

import inspect

class WeightedQuickUnion():
    """Weighted Quick Union Solution to dynamic connectivity problem
    
    Similar to QuickUnion solution, but keeps track of the size of the trees 
    to avoid generating large trees leading to worse case scenarios(full array parse/update)
    """
    def __init__(self, n: int):
        self.n = n
        self.id = list(range(n))
    

    def root(self, k: int):
        """Find root of element k"""
        
        while self.id[k] != k:
            k = self.id[k]
        return k

    def find(self, p: int, q: int) -> bool:
        """Find in the connected graph/ components if two elements are connected"""
        print(self.root(p) == self.root(q))
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        """Connect two nodes in the graph

        Args:
            p (int): connect node TO
            q (int): connect TO node
        """
        pid = self.root(p)
        qid = self.root(q)
        self.id[pid] = qid

class QuickUnion():
    """Quick Union Solution to dynamic connectivity problem"""
    def __init__(self, n: int):
        self.n = n
        self.id = list(range(n))
    

    def root(self, k: int):
        """Find root of element k"""
        
        while self.id[k] != k:
            k = self.id[k]
        return k

    def find(self, p: int, q: int) -> bool:
        """Find in the connected graph/ components if two elements are connected"""
        print(self.root(p) == self.root(q))
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        """Connect two nodes in the graph

        Args:
            p (int): connect node TO
            q (int): connect TO node
        """
        pid = self.root(p)
        qid = self.root(q)
        self.id[pid] = qid
        

class QuickFind():
    """Quick Find Solution to dynamic connectivity problem"""
    def __init__(self, n: int):
        self.n = n
        self.id = list(range(n))
    
    def find(self, p: int, q: int) -> bool:
        """Find in the connected graph/ components if two elements are connected"""
        print(self.id[p] == self.id[q])
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int):
        """Connect two nodes in the graph

        Args:
            p (int): connect node TO
            q (int): connect TO node
        """
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.n):
            if self.id[i] == pid:
                self.id[i] = qid
    
if __name__ == "__main__":
    (inspect.getdoc(QuickFind))
    algo = QuickUnion(10)
    result = []
    algo.union(4, 3)
    algo.union(3, 8)
    algo.union(6, 5)
    algo.union(9, 4)
    algo.union(2, 1)
    result.append(algo.find(0, 7))
    result.append(algo.find(8, 9))
    algo.union(5, 0)
    algo.union(7, 2)
    algo.union(6, 1)
    algo.union(1, 0)
    result.append(algo.find(0, 7))
    assert result == [False, True, True]