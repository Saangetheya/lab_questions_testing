from typing import Tuple

# ---------------------- Question 1b ----------------------#
def most_sold_item(record_file_name: str) -> Tuple[str, int]:
    """
    Given a record file name, return the most sold stationery item as a tuple.

    Each line in the file has the format: item_name, color, quantity
    - quantity: positive means restocked, negative means sold

    Only lines with negative quantity count as sold.
    Return a tuple of (item_name, total_sold) for the item with the highest total sales.
    If there is a tie, return the item that comes first alphabetically.
    If no items were sold, return ("", 0).

    :param record_file_name: Name of the record file.
    :return: tuple of (item_name, total_sold)
    """
    sales = {}
    with open(record_file_name,"r") as f:
        for line in f:
            parts = line.strip().split(',')
            item_name,qty = parts[0],parts[2] # item_name, color, quantity
            if qty<0:
                sales[item_name] = sales.get(item_name,0)+abs(qty)
    
    if not sales :
        return ("",0)
    
    best_name = ""
    best_sold = 0

    for name,sold in sales.items():
        if sold > best_sold or (sold == best_sold and name < best_name):
            best_name = name
            best_sold = sold

    return (best_name,best_sold)
