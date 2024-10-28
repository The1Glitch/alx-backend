#!/usr/bin/env python3
"""
The function defines class server that paginates a db of popular names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function takes args and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexs to return in a list for those pagination parameters
    Args:
        pages (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Returns:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """Server class to paginate a DB of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __int__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_SELF) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        The function takes 2 int args and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive int
            page_size (int): number of records per page. must be a +ve int
        Return:
            list of containing required data from the dataset
        """
        assert type(page) is int and  page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
