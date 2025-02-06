from copy import deepcopy

class TieredPriorityQueue():

    
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty tiered priority queue.
        Use: queue = TieredPriorityQueue()
        -------------------------------------------------------
        Returns:
            a new TieredPriorityQueue object (TieredPriorityQueue)
        -------------------------------------------------------
        """
        self.tiers = []

    
    def push(self, tier, value):
        """
        -------------------------------------------------------
        Adds a copy of value to a tier of the tiered priority queue.
        Use: queue.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
            tier - the priority of the element to be added to the queue (int)
        Returns:
            None
        -------------------------------------------------------
        """
        pass
    
    def pop(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value in the tiered priority queue.
        Use: value = queue.pop()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the tiered priority queue (?)
        -------------------------------------------------------
        """
        pass
    
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value in the tiered priority queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the tiered priority queue (?)
        """
        pass
    
    def shift(self, tier, target):
        """
        -------------------------------------------------------
        Moves all the values in one tier to target tier.
        Use: queue.shift(tier, target)
        -------------------------------------------------------
        Parameters:
            tier - the priority of the elements to be moved (int)
            target - the new priority of the elements (int)
        Returns:
            None
        -------------------------------------------------------
        """
        pass
    
    def pop(self, tier):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value in a tier
        Use: value = queue.pop()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in a tier (?)
        -------------------------------------------------------
        """
        pass
    
    def peek(self, tier):
        """
        -------------------------------------------------------
        Peeks at the highest priority value in a tier.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in a tier (?)
        """

        pass
    
    def split(self, tier, key, target):
        """
        -------------------------------------------------------
        Splits a tier into two tiers.
        Use: queue.split(tier, key, target)
        -------------------------------------------------------
        Parameters:
            tier - the priority of the elements to be split (int)
            key - the priority of the split (int)
            target - the priority of the new tier (int)
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        pass