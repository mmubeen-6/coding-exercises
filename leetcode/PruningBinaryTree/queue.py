from collections import deque
from typing import Any


class Queue:
    """
    A Queue implementation
    """

    def __init__(self) -> None:
        """Initialize the Queue"""
        self._queue = deque()

    def push(self, value: int) -> None:
        """Pushes a value onto the queue

        Args:
            value (int): element to add to the queue
        """
        self._queue.append(value)

    def peek(self) -> Any:
        """Peek at the top of the queue

        Raises:
            IndexError: If queue is empty

        Returns:
            Any: the top element of the queue
        """
        if len(self._queue) == 0:
            raise IndexError("queue is empty")
        return self._queue[0]

    def pop(self) -> Any:
        """Pops and returns the top element of the queue

        Raises:
            IndexError: If queue is empty

        Returns:
            Any: the top element of the queue
        """
        if len(self._queue) == 0:
            raise IndexError("queue is empty")
        return self._queue.popleft()

    def size(self) -> int:
        """Returns the size of the queue

        Returns:
            int: the size of the queue
        """
        return len(self._queue)

    def __len__(self) -> int:
        """Returns length of queue

        Returns:
            int: length of queue
        """
        return len(self._queue)

    def __repr__(self) -> str:
        """Returns a string representation of the queue

        Returns:
            str: string representation of the queue
        """
        out_str = "["
        for element in self._queue:
            out_str += element + ", "
        out_str = out_str + "]"
        return out_str
