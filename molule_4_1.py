first = int(input())
second = int(input())
from fake_math import divide as result_fake
print(result_fake(first, second))

from true_math import divide as result_true
print(result_true(first, second))

