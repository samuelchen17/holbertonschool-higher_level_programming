"""Module that defines VerboseList Class"""


class VerboseList(list):
    """verboseList class"""

    def append(self, item):
        """Extend append"""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, x):
        """Extend extend"""
        super().extend(x)
        print(f"Extended the list with {len(x)} items.")

    def remove(self, item):
        """extend remove"""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """extend pop"""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
