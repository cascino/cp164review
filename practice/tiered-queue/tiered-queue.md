# tiered-queue
___
The Tiered Priority Queue (TPQ) is a priority queue variant that categorizes elements into discrete tiers, each representing a fixed priority level. Unlike a conventional priority queue that orders all elements in a single sorted order, TPQ groups elements by tier, where each tier is internally managed (for example, with an array or circular buffer) and the tiers themselves are linearly ordered. This structure is especially useful when tasks or jobs naturally fall into a limited number of priority categories and when bulk operations on specific tiers are desirable.

# operations
___
You must support t