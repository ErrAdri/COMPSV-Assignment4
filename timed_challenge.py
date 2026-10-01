# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
# Input: "{[(])}"
# Output: False

# Structure: a stack (a Python list using append/pop).
# The most recently opened bracket is always the one that has to close next,
# which is last-in, first-out. Each character is pushed or popped at most once,
# so the runtime is O(n) and the stack uses at most O(n) extra space.

def is_balanced(text):
    if not isinstance(text, str):
        raise TypeError("is_balanced expects a string")

    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())
    stack = []

    for char in text:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            # A closer with nothing open, or with the wrong opener on top, fails.
            if not stack or stack.pop() != pairs[char]:
                return False
        # Any other character (letters, spaces, digits) is ignored.

    # Anything left on the stack was opened but never closed.
    return len(stack) == 0


if __name__ == "__main__":
    # Examples from the prompt
    assert is_balanced("{[()]}") is True
    assert is_balanced("{[(])}") is False

    # Edge cases
    assert is_balanced("") is True              # empty string
    assert is_balanced("abc 123") is True       # no brackets at all
    assert is_balanced("(") is False            # opened, never closed
    assert is_balanced(")") is False            # closed, never opened
    assert is_balanced("())") is False          # one closer too many
    assert is_balanced("(()") is False          # one opener too many
    assert is_balanced(")(") is False           # right counts, wrong order
    assert is_balanced("()[]{}") is True        # side by side
    assert is_balanced("def f(x): return [x, {1: (2)}]") is True  # mixed text

    # Wrong data type
    for bad_input in (None, 123, ["(", ")"]):
        try:
            is_balanced(bad_input)
            assert False, "expected a TypeError"
        except TypeError:
            pass

    print("All timed challenge tests passed.")


# REFLECTION
#
# I chose question 13, Balanced Symbols, and solved it with a stack, using a
# Python list with append and pop. The problem is last-in, first-out by nature:
# the bracket that was opened most recently is the one that has to close next.
# A stack keeps that bracket on top, so every check is a single O(1) pop and
# the whole string is handled in one O(n) pass. I also used a dictionary that
# maps each closing bracket to its opener, which kept the matching logic to one
# comparison instead of a chain of if statements.
#
# The time limit shaped which question I picked as much as how I solved it. With
# only 30 minutes I wanted a problem where the right structure was obvious, so I
# could spend the time on correctness and testing instead of on design. For the
# same reason I used a built-in list as the stack instead of writing my own
# Stack class. Writing the class would have shown more of what I learned in
# earlier units, but it would have used minutes that I needed for edge cases.
#
# The main compromise was scope. My function ignores every character that is
# not a bracket, and it only returns True or False. It does not report where
# the mismatch is, which a real tool like a code editor would need to do. I also
# decided quickly that a non-string input should raise a TypeError instead of
# returning False, without comparing the two options carefully. My tests are
# plain assert statements instead of a proper test framework. With more time I
# would add the position of the first error and write the tests with unittest.