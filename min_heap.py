# Name: David Jantz
# OSU Email: jantzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 5: Min Heap Implementation
# Due Date: 11/25/2024
# Description: This program implements a classic min heap using a dynamic array as
#               the underlying data structure. All typical min heap operations are
#               implemented, such as add(), get_min(), remove_min(), build_heap(),
#               heapsort(), etc.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds an element to the heap while maintaining heap properties.
        """
        # add to the last spot in the array
        self._heap.append(node)
        # percolate up until it's priority value is greater its parent
        self._percolate_up(self._heap.length() - 1)

    def _percolate_up(self, node_index: int) -> None:
        """
        Percolates up the specified node to maintain heap property
        """
        # while loop --
        #       find the parent of the node with that formula
        #       compare parent and node
        #       swap if node PV is less than its parent
        #       kick out of the while loop if it's reached the right spot
        spot_found = False
        while not spot_found:
            if node_index == 0:
                return  # terminate while loop if the OG node is now the root
            parent_index = (node_index - 1) // 2  # floor division to find parent index
            parent = self._heap[parent_index]
            node = self._heap[node_index]
            if node < parent:
                self._heap[node_index] = parent
                self._heap[parent_index] = node
                node_index = parent_index  # update node index for next run through while loop
            else:
                spot_found = True

    def is_empty(self) -> bool:
        """
        Returns True if heap is empty, otherwise returns False
        """
        return self._heap.is_empty()  # implement with preexisting DynamicArray method

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        pass

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
"""
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
"""