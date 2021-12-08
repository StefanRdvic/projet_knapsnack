from src.util import get_item_info


class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def get_value_and_weight(self, objects_dict) -> (int, int):
        total_value = 0
        total_weight = 0

        for item in self.content:
            value, weight = get_item_info(item, objects_dict)
            total_value += value
            total_weight += weight

        return total_value, total_weight

    def print_content(self, objects_dict) -> None:
        for item in self.content:
            value, weight = get_item_info(item, objects_dict)
            print(item + ' ' + str(value) + ' ' + str(weight), end='\n')

        total_value, total_weight = self.get_value_and_weight(objects_dict)
        print('Le sac a ' + str(len(self.content)) + ' objets, pour une valeur de ' + str(total_value) +
              ' et un poids de ' + str(total_weight) + '/' + str(self.capacity), end='\n')


def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    sorted_objects_dict = dict(sorted(objects_dict.items(), key=lambda i: (i[1][0] / i[1][1]), reverse=True))

    current_sack_capacity = 0

    for item in sorted_objects_dict.keys():
        if current_sack_capacity == knapsack.capacity:
            return knapsack

        _, weight = get_item_info(item, objects_dict)

        if weight + current_sack_capacity <= knapsack.capacity:
            knapsack.content.append(item)
            current_sack_capacity += weight

    return knapsack


def solve_knapsack_best(knapsack, objects_dict) -> Knapsack:
    pass


def solve_knapsack_optimal(knapsack, objects_dict) -> Knapsack:
    pass
