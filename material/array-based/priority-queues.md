___
Similarly to the queue, the priority queue supports the following operations: `push`, `pop`, and `peek`. The `push` operation adds an element to the priority queue, the `pop` operation removes and returns the element with the highest priority, and the `peek` operation returns the element with the highest priority without removing it. 

Dissimilarly to the queue, the order in which the elements are stored is determined entirely by the attributes of the elements themselves.

A (relatively) low level implementation of a priority queue can be done using an array. The following is an example of one. 

```python
