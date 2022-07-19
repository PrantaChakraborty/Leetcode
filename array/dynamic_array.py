"""
dynamic array
for example first take size 8, after array is full, it requests to its class to give an array of greater than 8,
after getting the new array initialized the values to the new array and the system reclaimed the old array
"""
import sys
import ctypes

data = []
for i in range(100):
    arr_len = len(data)
    arr_size = sys.getsizeof(data)
    print(f"Length is {arr_len} and array size is {arr_size}")
    data.append(None)


class DynamicArray:
    """
    custom dynamic array
    """

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)  # creating an array

    def _make_array(self, c):
        """
        Return a new array with capacity c
        :param c:
        :return: array
        """
        return c * ctypes.py_object

    def __len__(self):
        """
        :return: the number of elements stored in array
        """
        return self._n

    def __getitem__(self, item):
        """

        :param item:
        :return: return element at index k
        """
        if not 0 <= item < self._n:
            raise IndexError('invalid index')
        return self._array[item]

    def append(self, obj):
        """
        Add object to end of the array
        :param obj:
        :return:
        """
        if self._n == self._capacity:  # not enough space
            self._resize(2 * self._capacity)  # double the capacity
        self._array[self._n] = obj
        self._n += 1

    def _resize(self, capacity):
        """
        resize the internal array to capacity
        :param capacity:
        :return:
        """
        new_array = self._make_array(capacity)  # create a new array
        for item in range(self._n):
            new_array[item] = self._array[item]
        self._array = new_array  # use the bigger array
        self._capacity = capacity  # update the capacity



