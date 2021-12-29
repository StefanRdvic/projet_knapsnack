class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def copy(self):
        knapsack_copy = Knapsack(self.capacity)
        knapsack_copy.content.extend(self.content)
        return knapsack_copy

    def get_value_and_weight(self, objects_dict) -> (int, int):
        total_value = 0
        total_weight = 0

        for item in self.content:
            value, weight = objects_dict[item][0], objects_dict[item][1]
            total_value += value
            total_weight += weight

        return total_value, total_weight

    def print_content(self, objects_dict) -> None:
        for item in self.content:
            value, weight = objects_dict[item][0], objects_dict[item][1]
            print(item + ' ' + str(value) + ' ' + str(weight), end='\n')

        total_value, total_weight = self.get_value_and_weight(objects_dict)
        print(
            "Le sac a %d objets, pour une valeur de %d et un poids de %d/%d"
            % (len(self.content), total_value, total_weight, self.capacity)
        )


# -------------------------------------------------------------------------
# Greedy solution
# -------------------------------------------------------------------------
def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    sorted_objects_dict = dict(sorted(objects_dict.items(), key=lambda i: (i[1][0] / i[1][1]), reverse=True))
    current_sack_capacity = 0

    for item in sorted_objects_dict.keys():
        if current_sack_capacity == knapsack.capacity:
            return knapsack

        weight = objects_dict[item][1]

        if weight + current_sack_capacity <= knapsack.capacity:
            knapsack.content.append(item)
            current_sack_capacity += weight

    return knapsack


# -------------------------------------------------------------------------
# best solution
# -------------------------------------------------------------------------
def solve_knapsack_best(knapsack, objects_dict) -> Knapsack:
    pass


# -------------------------------------------------------------------------
# Optimal solution
# -------------------------------------------------------------------------
def solve_knapsack_optimal(knapsack, objects_dict):
    keys = list(objects_dict.keys())
    return get_max_value(knapsack, objects_dict, keys, knapsack.capacity, 0)


def get_best(knapsack1, knapsack2, objects_dict):
    sack1_value, sack1_weight = knapsack1.get_value_and_weight(objects_dict)
    sack2_value, sack2_weight = knapsack2.get_value_and_weight(objects_dict)

    if sack1_value == sack2_value:
        return knapsack1 if sack1_weight < sack2_weight else knapsack2

    return knapsack1 if sack1_value > sack2_value else knapsack2


def get_max_value(knapsack, objects_dict, keys, current_capacity, current_index):
    if current_index == len(keys) or current_capacity <= 0:
        return knapsack

    weight = objects_dict[keys[current_index]][1]
    knapsack_copy = knapsack.copy()

    if weight <= current_capacity:
        knapsack.content.append(keys[current_index])

        knapsack_include = get_max_value(
            knapsack, objects_dict, keys, current_capacity - weight, current_index + 1
        )

        knapsack_exclude = get_max_value(
            knapsack_copy, objects_dict, keys, current_capacity, current_index + 1
        )
        return get_best(knapsack_include, knapsack_exclude, objects_dict)

    return get_max_value(knapsack_copy, objects_dict, keys, current_capacity, current_index + 1)
