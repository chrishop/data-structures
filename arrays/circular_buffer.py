
"""

A Circular Buffer is a data structure which uses a single fixed sized buffer as if it were connected end to end.
This structure lends itself to buffering datastreams.
Buffers operate essentially like a FIFO queue.

The useful property of a circular buffer is that it does not need to have its elements shuffled around when one is consumed.
Circular buffering makes a good implementation strategy for a queue that has fixed maximum size.
For queues that grow and shrink in size a linked list implementation can be used. (as copying values from a small to larger queue is costly)

Circular buffers can be implemented using 4 pointers or 3 pointers and 2 variables.
- buffer start in memory
- buffer end in memory, or buffer capacity
- start of valid data (index or pointer)
- end of valid data (index or pointer), or amount of data currently in the buffer (integer)

https://en.wikipedia.org/wiki/Circular_buffer
"""


class ArrayBuffer:
    
    def __init__(self, size) -> None:
        self.size = size
        self.array = [None for _ in range(size)]
        self.elems = 0
        self.queue_head = 0
        self.queue_end = 0
        
    def enqueue(self, elem):
        if self.elems >= self.size:
            raise BufferError("buffer is full, can't enqueue")
            
        self.array[self.queue_head] = elem
        self.queue_head = (self.queue_head + 1) % self.size
        self.elems += 1
        return elem
    
    def dequeue(self):
        if self.elems <= 0:
            raise BufferError("buffer is empty, can't dequeue")
        value = self.array[self.queue_end]
        self.queue_end = (self.queue_end + 1) % self.size
        self.elems -= 1
        return value
    
    def empty(self):
        return self.elems <= 0
        
    def full(self):
        return self.elems <= self.size 
    
    def elements(self):
        return self.elems