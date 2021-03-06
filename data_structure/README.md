# Data Structures

## Hash Table
Hash table use hash function to map keys to values to achieve efficient lookup, O(1).
Collisions happen when two keys have the same hash code.
There are severak ways to avoid collision,
- Chaining with Linked List or Binary Search Tree.
- Open Addressing with Linear Probing.

## Array List
Array list have dynamic size to overcome fixed array size in Java.

## String Builder
Concatenating strings in the syntax of

        s = ""
        for word in words:
            s1 = s1+word

requires O(xn<sup>2</sup>) with x being characters and n as the number of words.
String Builder act as an resizeble array to store all strings and join them when needed.

## LinkedList
Compared to array, LinkedList offers O(1) add and remove.

## Stack and Queues
Stack follows Last-In-First-Out.
Queue follows First-In-First-Out, suitable for Bredth First Search.

## Binary Tree
Binary trees hold value and reference to left and right child.
There are three common ways to traverse binary trees:
- Preorder: Root, Lt, Rt
- Inorder: Lt, Root, Rt
- Postorder: Lt, Rt, Root

## Trie (prefix Tree)
Tries are n-ary trees that is optimal for looking up prefixes.

## Heap
Heaps are binary trees with min/max at root.

## Graph
Graphs are vertices connected by edges (directed, indirected).
Graphs are commonly represented using Adjacency List, and Adjacency Matrix.
Common ways to search a graph includes,
- Depth First Search (Recursive)
- Bredth First Search (Iterative with Queue)
