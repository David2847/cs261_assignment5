# Name: David Jantz
# OSU Email: jantzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment2
# Due Date: Monday, October 28, 2024
# Description: This is an implementation of the dynamic array ADT in Python.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method resizes the array capacity by creating a new StaticArray of different size and copying over everything.
        """
        if new_capacity < self._size or new_capacity < 1:  # StaticArray requires array sizes of 1 or greater
            return
        new_static_array = StaticArray(new_capacity)

        # iterate through and copy data over to new StaticArray
        for i in range(self._size):
            new_static_array.set(i, self[i])

        self._data = new_static_array
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Adds new value onto the end of the array, resizing if necessary (doubling capacity)
        """
        # check capacity, double if necessary
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # increase self._size by one
        self._size += 1
        # just use bracket notation to set new value
        self[self._size - 1] = value

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Add new value at desired index, shifting values over and doubling capacity as necessary.
        """
        # Raise DynamicArrayException for invalid indices.
        if index > self._size or index < 0:
            raise DynamicArrayException

        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # increase self._size
        self._size += 1

        # shift over values to make an empty slot at desired index
        # have to iterate backwards so they don't overwrite each other
        for i in range(self._size - 1, index, -1):
            self._data[i] = self._data[i - 1]

        # insert value at desired index
        self._data[index] = value

    def remove_at_index(self, index: int) -> None:
        """
        Removes desired item from the array. Resize if it gets small enough.
        """
        # the only valid indices are ones that currently hold values.
        if index >= self._size or index < 0:
            raise DynamicArrayException

        # resize capacity if:
        # capacity is currently greater than 10, and
        if self._capacity > 10:
            # size is strictly less than 1/4 of capacity.
            if self._size * 4 < self._capacity:
                # if conditions are met, resize capacity to double current size or 10, which ever is larger.
                new_capacity = max(10, self._size * 2)
                self.resize(new_capacity)

        # shift over values to overwrite value at specified index
        for i in range(index, self._size - 1):
            self[i] = self[i + 1]

        # decrease self._size by one
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Return new dynamic array that is a subset of current dynamic array
        """
        stop_index = start_index + size  # EXclusive -- value at this index not included
        # Raise DynamicArrayException if start index or size is invalid
        # no valid start index for empty arrays
        if (start_index >= self._size or
                start_index < 0 or
                stop_index > self._size or
                stop_index < start_index):
            raise DynamicArrayException

        new_da = DynamicArray()
        # loop through old array, appending desired values onto new array
        for i in range(start_index, stop_index):
            new_da.append(self[i])
        return new_da

    def map(self, map_func) -> "DynamicArray":
        """
        create new dynamic array where the value of each element is generated by applying a given
        map function to the corresponding value from the original array.
        """
        new_da = DynamicArray()
        # loop through old array, apply map function and append to new dynamic array
        for val in self:
            new_da.append(map_func(val))
        return new_da

    def filter(self, filter_func) -> "DynamicArray":
        """
        Create new dynamic array populated only with those elements for which filter_func returns True.
        """
        new_da = DynamicArray()
        for val in self:
            if filter_func(val):
                new_da.append(val)
        return new_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially apply reduce_func to all elements of dynamic array and return resulting value.
        """
        # initialize answer as first value or as initializer
        answer = initializer
        start_index = 0  # zeroth item not initializer, so apply reduce_func starting there
        if initializer is None and self._size > 0:
            answer = self[0]
            start_index = 1  # zeroth item is the initializer, so apply reduce_func starting at index 1
        if answer is None:  # if initializer and zeroth array item were both none, call it quits
            return answer

        # loop through array, performing reduce_func as we go
        for i in range(start_index, self._size):
            answer = reduce_func(answer, self[i])
        return answer


def chunk(arr: DynamicArray) -> "DynamicArray":
    """
    "chunks" input array into an array of arrays, each consisting of a non-descending subsequence of values.
    """
    # create new dynamic array and initial subarray
    new_da = DynamicArray()
    new_da.append(DynamicArray())
    try:
        new_da[0].append(arr[0])  # add the first value of the array manually if it exists
    except DynamicArrayException:
        return DynamicArray()  # if arr is empty, we want to return a 1D empty array, so just make a new one here

        # iterate through input array:
    subarray_index = 0  # keep track of which subarray to add items to.
    for i in range(1, arr.length()):
        # check to see if we need to make a new subarray
        if arr[i] < arr[i - 1]:
            subarray_index += 1
            new_da.append(DynamicArray())
        # regardless of whether a new subarray was made, add current value onto current subarray
        new_da[subarray_index].append(arr[i])

    return new_da


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    takes a dynamic array in sorted order, returns tuple with first item being dynamic array of the mode(s)
    and the second item being their frequency
    """
    modes = DynamicArray()
    modes.append(arr[0])  # first item in modes array, for now
    freq = 1  # first item appears at least once

    # loop through arr, count freq of each item as we go
    count = 1
    for i in range(1, arr.length()):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1

        if count == freq:  # another mode! add to list
            modes.append(arr[i])
        elif count > freq:  # new mode, others obsolete. delete them. update freq
            modes = DynamicArray()
            modes.append(arr[i])
            freq = count
        # last case: if count < freq, do nothing

    return modes, freq


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray([0, 1, 2, 3])

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da)
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')


    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
