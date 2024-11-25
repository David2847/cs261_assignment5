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
        Removes and returns the object with the minimum key while performing necessary
        shuffling operations to maintain heap property.
        """
        if self.is_empty():
            raise MinHeapException
        # store value of root node
        min_node = self._heap[0]
        # store value of last element at index zero
        last_node_index = self._heap.length() - 1
        self._heap[0] = self._heap[last_node_index]
        # remove last element
        self._heap.remove_at_index(last_node_index)
        # percolate new root down
        self.percolate_down(0, self.size() - 1)
        # return value of root node
        return min_node

    def percolate_down(self, node_index, max_index) -> None:
        """
        Percolates the root index down to maintain heap property.
        """
        spot_found = False
        while not spot_found:
            # find both children of current node
            left_child_index = node_index * 2 + 1
            right_child_index = node_index * 2 + 2
            try:
                left_child = self._heap.get_at_index(left_child_index)
            except DynamicArrayException:
                left_child = None
            try:
                right_child = self._heap.get_at_index(right_child_index)
            except DynamicArrayException:
                right_child = None

            # this chunk is for HeapSort... ensures we don't stray out of the heap
            #       section of the array while sorting in place.
            if left_child_index > max_index:
                left_child = None
            if right_child_index > max_index:
                right_child = None

            # keep the smaller child
            # or if right and left are equal keep the left child
            # or if one doesn't exist, keep the one that does
            # or if neither exists, kick out of the while loop
            if left_child is None and right_child is None:
                return
            elif right_child is None or left_child <= right_child:
                favorite_child = left_child
                fav_child_index = left_child_index
            else:
                favorite_child = right_child
                fav_child_index = right_child_index

            # swap if child is less than parent
            node = self._heap.get_at_index(node_index)
            if favorite_child < node:
                self._heap[node_index] = favorite_child
                self._heap[fav_child_index] = node
                node_index = fav_child_index  # update node index for next run through while loop
            else:
                spot_found = True

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a heap out of an unsorted array, overwriting current contents
        of the heap.
        """
        # Handle empty array edge case
        if da.is_empty():
            self._heap = DynamicArray()
            return

        self._heap = da.slice(0, da.length())  # copy over data
        # start at first non-leaf node, percolate down
        last_node_index = self._heap.length() - 1
        node_index = (last_node_index - 1) // 2

        # node_index could be -1 immediately, but while loop handles this
        while node_index >= 0:
            self.percolate_down(node_index, self.size() - 1)
            node_index -= 1

    def size(self) -> int:
        """
        Returns the number of items currently stored on the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap.
        """
        self._heap = DynamicArray()

    def swap(self, index1, index2) -> None:
        """
        Swaps two objects in the heap
        """
        obj1 = self._heap[index1]
        obj2 = self._heap[index2]
        self._heap[index1] = obj2
        self._heap[index2] = obj1


def percolate_down(da: DynamicArray, node_index: int, max_index: int) -> None:
    """
    Perform percolate down operation in place on dynamic array. Node at node_index
    is percolated down, not past max_index.
    """
    spot_found = False
    while not spot_found:
        # find both children of current node
        left_child_index = node_index * 2 + 1
        right_child_index = node_index * 2 + 2
        try:
            left_child = self._heap.get_at_index(left_child_index)
        except DynamicArrayException:
            left_child = None
        try:
            right_child = self._heap.get_at_index(right_child_index)
        except DynamicArrayException:
            right_child = None

        # this chunk is for HeapSort... ensures we don't stray out of the heap
        #       section of the array while sorting in place.
        if left_child_index > max_index:
            left_child = None
        if right_child_index > max_index:
            right_child = None

        # keep the smaller child
        # or if right and left are equal keep the left child
        # or if one doesn't exist, keep the one that does
        # or if neither exists, kick out of the while loop
        if left_child is None and right_child is None:
            return
        elif right_child is None or left_child <= right_child:
            favorite_child = left_child
            fav_child_index = left_child_index
        else:
            favorite_child = right_child
            fav_child_index = right_child_index

        # swap if child is less than parent
        node = self._heap.get_at_index(node_index)
        if favorite_child < node:
            self._heap[node_index] = favorite_child
            self._heap[fav_child_index] = node
            node_index = fav_child_index  # update node index for next run through while loop
        else:
            spot_found = True

def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts it using the heap sort algorithm
    """
    # Handle empty array edge case
    if da.is_empty():
        return

    # start at first non-leaf node, percolate down
    last_node_index = da.length() - 1
    node_index = (last_node_index - 1) // 2

    # node_index could be -1 immediately, but while loop handles this
    while node_index >= 0:
        percolate_down(da, node_index, da.length() - 1)
        node_index -= 1







    # build a heap out of the array
    min_heap = MinHeap()
    min_heap.build_heap(da)

    # counter k initialized to point to last element
    counter = min_heap.size() - 1

    while counter > 0:
        min_heap.swap(0, counter)  # swap kth element and first (smallest) element
        # decrement k and percolate replacement value down. don't percolate past heap portion of the array!
        counter -= 1
        min_heap.percolate_down(0, counter)




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

    print("\nPDF - build_heap example 2")
    print("--------------------------")
    da = DynamicArray([])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

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
