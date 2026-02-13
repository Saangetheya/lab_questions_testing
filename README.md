# Stationery Lab Tasks
In this lab, you will be asked to implement 2 questions. After you finish your codes, submit the assignment with the following lines:
```bash
git add .
git commit -m "<some description>"
git push
```

## Q1 (12 pts)
You own a stationery shop and maintain records of all items that go in and out. These records are stored in a file with the following format:
```
pen, red, 50
pen, red, -10
pen, blue, 30
pencil, green, 20
pencil, green, -5
eraser, white, 15
pen, blue, -8
```

### Format Details:
- Each line follows the format: `<item_name>, <color>, <quantity>`
- The item name **does not contain commas** and is a single word (e.g., `pen`, `pencil`, `marker`).
- The color is a single word (e.g., `red`, `blue`, `green`).
- The quantity:
  - A **positive number (`N`)** indicates that `N` items were **restocked**.
  - A **negative number (`-N`)** indicates that `N` items were **sold**.


### 1. Items Sold (6 pts)
Implement the function in `lab_1.py`:
```python
def items_sold(record_file_name: str) -> Dict[str, Dict[str, int]]:
```
- Reads the record file and computes the total number of items **sold** for each item, grouped by color.
- Returns a dictionary in the following format:
  ```python
  {
      "<item_name>": { "<color>": <total_sold>, ... }, ...
  }
  ```
- If an item has not been sold (only restocked), it should **not appear** in the result.

#### **Example Output:**
```python
{
    "pen": {"red": 10, "blue": 8},
    "pencil": {"green": 5}
}
```
Note: `eraser` does not appear because it was only restocked, never sold.

---

### 2. Most Sold Item (6 pts)
Implement the function in `lab_2.py`:
```python
def most_sold_item(record_file_name: str) -> Tuple[str, int]:
```
- Computes the total number of items **sold** per item across all colors. Return the most sold item.
- Returns a tuple:
  ```python
  ("<item_name>", total_sold)
  ```
- If multiple items tie for most sold, return the one that comes **first alphabetically**.
- If no items were sold, return `("", 0)`.

#### **Example Output:**
```python
("pen", 18)
```
