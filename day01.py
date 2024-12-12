import re
import sys

left = []
right = []
for line in sys.stdin:
  line_numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
  left.append(line_numbers[0])
  right.append(line_numbers[1])

left.sort()
right.sort()

assert len(left) == len(right)

distances = [abs(l-right[i]) for i,l in enumerate(left)]
print(sum(distances))

similarities = [l*right.count(l) for l in left]
print(sum(similarities))
