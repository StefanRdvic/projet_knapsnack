import json

from test_knapsack import (
    get_medium_objects_dict, get_small_objects_dict
)

import pytest
from src.Knapsack import (
    Knapsack, solve_knapsack_greedy, solve_knapsack_optimal
)


sack, objects_dict = get_small_objects_dict(12)
filled_sack = solve_knapsack_optimal(sack, objects_dict)
filled_sack.print_content(objects_dict)
