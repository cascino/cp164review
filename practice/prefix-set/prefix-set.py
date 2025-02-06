from copy import deepcopy

class PrefixSet():
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty PrefixSet.
        Use: set = PrefixSet()
        -------------------------------------------------------
        Returns:
            a new PrefixSet object (PrefixSet)
        -------------------------------------------------------
        """
        self._values = []
        self._size = 0
    
    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Private helper that searches for the key in the list of values.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the key in the list of values, -1 if not found (int)
        -------------------------------------------------------
        """
        pass

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the PrefixSet.
        Use: set.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        pass

    def remove(self, value):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the PrefixSet that matches value.
        Use: v = set.remove(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            v - the value in the PrefixSet that matches value, None if not found (?)
        -------------------------------------------------------
        """
        pass

    def contains(self, value):
        """
        -------------------------------------------------------
        Determines if the PrefixSet contains value.
        Use: b = set.contains(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            b - True if the PrefixSet contains value, False otherwise (boolean)
        -------------------------------------------------------
        """
        pass

    def count(self, value):
        """
        -------------------------------------------------------
        Determines the number of elements less than value in the PrefixSet.
        Use: n = set.count(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            n - the number of times value appears in the PrefixSet (int)
        -------------------------------------------------------
        """
        pass

    def prefix_sum(self, value):
        """
        -------------------------------------------------------
        Determines the number of values in the PrefixSet that have a prefix less than value.
        Use: n = set.prefix_sum(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            n - the number of values in the PrefixSet that have a prefix less than value (int)
        -------------------------------------------------------
        """
        pass

    def prefix(self, value):
        """
        -------------------------------------------------------
        Return the prefix of the value. 
        Use: n = set.prefix(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            n - the prefix of the value (int)
        -------------------------------------------------------
        """
        pass

    def difference(self, other):
        '''
        -------------------------------------------------------
        Determines the difference of two PrefixSets.
        Use: diff = set.difference(other)
        -------------------------------------------------------
        Parameters:
            other - another PrefixSet (PrefixSet)
        Returns:
            diff - a new PrefixSet containing the difference of the two PrefixSets (PrefixSet)
        -------------------------------------------------------
        '''
        pass

    def union(self, other):
        '''
        -------------------------------------------------------
        Determines the union of two PrefixSets.
        Use: union = set.union(other)
        -------------------------------------------------------
        Parameters:
            other - another PrefixSet (PrefixSet)
        Returns:
            union - a new PrefixSet containing the union of the two PrefixSets (PrefixSet)
        -------------------------------------------------------
        '''
        pass

    def intersection(self, other):
        '''
        -------------------------------------------------------
        Determines the intersection of two PrefixSets.
        Use: inter = set.intersection(other)
        -------------------------------------------------------
        Parameters:
            other - another PrefixSet (PrefixSet)
        Returns:
            inter - a new PrefixSet containing the intersection of the two PrefixSets (PrefixSet)
        -------------------------------------------------------
        '''
        pass

    def symmetric_difference(self, other):
        '''
        -------------------------------------------------------
        Determines the symmetric difference of two PrefixSets.
        Use: sym_diff = set.symmetric_difference(other)
        -------------------------------------------------------
        Parameters:
            other - another PrefixSet (PrefixSet)
        Returns:
            sym_diff - a new PrefixSet containing the symmetric difference of the two PrefixSets (PrefixSet)
        -------------------------------------------------------
        '''
        pass