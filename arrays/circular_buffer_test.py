import pytest
from circular_buffer import ArrayBuffer

def test_enqueue_item():
    ab = ArrayBuffer(3)
    ab.enqueue(3)
    
    assert ab.array == [3, None, None]
    assert ab.elements() == 1
    assert ab.queue_head == 1
    assert ab.queue_end == 0
    
    
def test_dequeue_item():
    ab = ArrayBuffer(3)
    ab.enqueue(3)
    
    assert ab.dequeue() == 3
    assert ab.array == [3, None, None]
    assert ab.elements() == 0
    assert ab.queue_end == 1
    assert ab.queue_head == 1
    
    
def test_insert_till_full():
    ab = ArrayBuffer(3)
    ab.enqueue(3)
    ab.enqueue(2)
    ab.enqueue(1)
    
    with pytest.raises(BufferError, match="buffer is full, can't enqueue"):
        ab.enqueue(0)
    
    
def test_dequeue_when_empty():
    ab = ArrayBuffer(3)
    
    with pytest.raises(BufferError, match="buffer is empty, can't dequeue"):
        ab.dequeue()