from typing import NamedTuple, Optional


class PartitionKeyRange(NamedTuple):
    """
    A range of partition keys, inclusive on both sides.

    A start value of None means start from the first partition, and an end value of None means end
    at the last partition. So [None, None] means all partitions in the set.
    """

    start: Optional[str]
    end: Optional[str]
