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
    return ()
