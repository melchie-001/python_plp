# Python Challenge – Week 2

## 🧠 Task Summary

This challenge covers basic list operations in Python:

1. Create an empty list called `my_list`.
2. Append the following elements: `10`, `20`, `30`, `40`.
3. Insert `15` at the second position.
4. Extend the list with `[50, 60, 70]`.
5. Remove the last element.
6. Sort the list in ascending order.
7. Find and print the index of the value `30`.

## ✅ Code Implementation

```python
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print("Index of 30:", my_list.index(30))
