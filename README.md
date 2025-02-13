# River View Buildings

## Problem Statement
You have gone fishing in a river located to the right of a line of buildings. There are `n` buildings in a row, and each building has a height represented by an integer array. A building has a river view if all buildings to its right have a smaller height.

### Objective
Return a list of indices (0-indexed) of buildings that have a river view, sorted in increasing order.

## Visualization
Consider an example:

```
Heights:  [25, 20, 45, 30, 35, 40, 30, 30, 50, 30, 30, 25]
Indices:  [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
```

### Expected Output
A list of indices of buildings that have a river view in increasing order.

## Approach
### **Data Structure Used**
We use a **Stack** to efficiently track buildings with a river view due to its **Last In, First Out (LIFO)** nature.

### **Justification for Stack**
- Helps in reversing the order naturally.
- Efficient memory handling.
- Supports key operations with optimal time complexity.

### **Pseudocode**
```python
1. Read heights of buildings -> heightList
2. Initialize an empty stack
3. Set maxHeight = heightList[-1] (height of last building)
4. Push the index of the last building onto the stack
5. Iterate through heightList in reverse order (except last building):
    - If current building's height > maxHeight:
      - Push its index onto stack
      - Update maxHeight
6. Initialize empty list result
7. While stack is not empty:
    - Pop element from stack and append to result
8. Write result to output file
```

### **Explanation**
- The algorithm iterates from right to left.
- If a building is taller than all buildings to its right, it is added to the stack.
- The stack is then reversed to obtain the correct order of indices.

## Implementation Details
### **Platform**
- Python 3.7

### **Files**
- `inputPS02.txt`: Contains test input.
- `outputPS02.txt`: Stores the generated output.
- `main.py`: The Python program implementing the solution.

## Time Complexity Analysis
- **Stack Operations**:
  - `push()`: O(1)
  - `pop()`: O(1)
  - `isEmpty()`, `__len__()`: O(1)
- **Main Loop**: O(N)
- **Overall Complexity**: **O(N)** (Linear Time)

## Alternative Approaches
### **1. Using List**
- Instead of a stack, we could use a list to store indices.
- Additional sorting would be required, increasing complexity.

### **2. Using Binary Search Tree (BST)**
- Storing indices in BST ensures sorted order.
- However, BST insertion is costly (`O(N log N)` time complexity).

## 🌍 Explore More Projects  
For more exciting machine learning and AI projects, visit **[The iVision](https://theivision.wordpress.com/)** and stay updated with the latest innovations and research! 🚀  

---
