from collections import deque

"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Justification: A set fits because the only question asked about each ID is
    # "have I seen this before?", and a set answers that with a hash lookup instead
    # of scanning. Each ID gets one membership check and one insert, both O(1) on
    # average, so the whole pass is O(n) time and O(n) extra space, compared with
    # O(n^2) for checking every ID against a list. Returning as soon as a repeat
    # is found means the best case stops early.
    seen = set()
    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    # Justification: This is first-in, first-out behavior, so a queue is the right
    # structure, and collections.deque is built for adding at one end and removing
    # from the other. add_task uses append() and remove_oldest_task uses popleft(),
    # which are both O(1). A plain list would also keep the order, but list.pop(0)
    # is O(n) because every remaining task has to shift down one position.
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        # Return None instead of raising an error when there is nothing to remove.
        if not self.tasks:
            return None
        return self.tasks.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    # Justification: A set fits because it stores each value only once, so repeats
    # in the stream are ignored automatically and no separate duplicate check is
    # needed. add() is an O(1) average hash insert, and get_unique_count() is O(1)
    # because Python keeps track of a set's size, so len() does not have to count.
    # Space is O(u), where u is the number of unique values, not the stream length.
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


if __name__ == "__main__":
    # Problem 1
    assert has_duplicates([10, 20, 30, 20, 40]) is True
    assert has_duplicates([1, 2, 3, 4, 5]) is False
    assert has_duplicates([]) is False
    assert has_duplicates([7]) is False

    # Problem 2
    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    assert task_queue.remove_oldest_task() == "Email follow-up"
    assert task_queue.remove_oldest_task() == "Code review"
    assert task_queue.remove_oldest_task() is None

    # Problem 3
    tracker = UniqueTracker()
    assert tracker.get_unique_count() == 0
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    assert tracker.get_unique_count() == 2

    print("All practice problem tests passed.")