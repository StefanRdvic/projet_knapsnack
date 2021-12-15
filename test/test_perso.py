from test_knapsack import get_small_objects_dict
from src.Knapsack import solve_knapsack_optimal, Knapsack

small_objects_dict = {
        "Épée de lumière lunaire": [909, 6],
        "Flèche incassable": [697, 5],
        "Grimoire résistant": [878, 6],
        "Armure rutilante": [349, 14]
}

sack = Knapsack(12)
filled_sack = solve_knapsack_optimal(knapsack=sack, objects_dict=small_objects_dict)
