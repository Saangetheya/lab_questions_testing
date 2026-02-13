from typing import Dict

# ---------------------- Question 1a ----------------------#
def items_sold(record_file_name: str) -> Dict[str, Dict[str, int]]:
    """
    Given a record file name, return a dictionary with the count of items sold.

    Each line in the file has the format: item_name, color, quantity
    - item_name: name of the stationery item (e.g., "pen", "pencil")
    - color: color of the item (e.g., "red", "blue")
    - quantity: positive means restocked, negative means sold

    Only lines with negative quantity count as sold.
    The returned dictionary maps item_name -> {color: total_sold}.
    Items that were only restocked (never sold) should NOT appear in the result.

    :param record_file_name: Name of the record file.
    :return: nested dictionary {item_name: {color: total_sold}}
    """
    return {}
