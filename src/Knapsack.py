class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []
        # Tracking attributs used to get time on accessing knapsacks value and weight
        self.available_capacity = capacity
        self.current_value = 0

    def copy(self):
        # Make a copy of the calling knapsack
        knapsack_copy = Knapsack(self.capacity)
        knapsack_copy.content.extend(self.content)
        knapsack_copy.available_capacity = self.available_capacity
        knapsack_copy.current_value = self.current_value
        return knapsack_copy

    def add_item(self, item, objects_dict):
        # Add an item to the knapsack content
        # Precondition : the knapsack have the necessary capacity
        assert not self.available_capacity - objects_dict[item][1] < 0
        self.content.append(item)
        self.available_capacity -= objects_dict[item][1]
        self.current_value += objects_dict[item][0]
        return self

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
            print("%s %d %d" % (item, value, weight))

        total_value, total_weight = self.get_value_and_weight(objects_dict)
        print(
            "Le sac a %d objets, pour une valeur de %d et un poids de %d/%d"
            % (len(self.content), total_value, total_weight, self.capacity)
        )


# -------------------------------------------------------------------------
# Utils
# -------------------------------------------------------------------------
def compare(knapsack1, knapsack2):
    # Return the knapsack with the best value
    # If both knapsacks have the same value, choose the one with the most available capacity
    if knapsack1.current_value == knapsack2.current_value:
        return knapsack1 if knapsack1.available_capacity > knapsack1.available_capacity else knapsack2

    return knapsack1 if knapsack1.current_value >= knapsack2.current_value else knapsack2


# -------------------------------------------------------------------------
# Greedy solution
# -------------------------------------------------------------------------
def solve_knapsack_greedy(knapsack, objects_dict) -> Knapsack:
    # the dictionary is sorted by the ratio between the value and the weight
    sorted_objects_dict = dict(sorted(objects_dict.items(), key=lambda i: (i[1][0] / i[1][1]), reverse=True))

    for item in sorted_objects_dict.keys():
        if knapsack.available_capacity == 0:    # No space left = no need to continue
            return knapsack

        weight = objects_dict[item][1]

        if weight <= knapsack.available_capacity:
            knapsack.add_item(item, objects_dict)

    return knapsack


# -------------------------------------------------------------------------
# Best solution
# -------------------------------------------------------------------------
def solve_knapsack_best(knapsack, objects_dict) -> Knapsack:
    keys = list(objects_dict.keys())
    return get_max_value_memoization(dict(), knapsack, objects_dict, keys, len(keys) - 1, knapsack.capacity)


def get_max_value_memoization(mem, knapsack, objects_dict, keys, n, remaining):
    """
    Get the best knapsack, this method uses dynamic programing and memoization concept
    :param mem: The calculated knapsack memory
    :param knapsack: Current knapsack
    :param objects_dict: Object dictionary
    :param keys: List of the dictionary keys (used to work with indexes)
    :param n: Number of item left
    :param remaining: Number of space left before the knapsack filling
    :return: the calculated knapsack with the best value
    """

    #  When the knapsack at nTh item and current remaining is already calculated simply returns it
    if (n, remaining) in mem.keys():
        return mem[(n, remaining)].copy()

    if n < 0 or remaining == 0:
        return knapsack.copy()

    weight = objects_dict[keys[n]][1]

    # Follow the same pattern as the Brute-Force method
    # The stored knapsacks has to be copied when accessed to avoid overwriting

    if weight > remaining:
        return get_max_value_memoization(mem, knapsack.copy(), objects_dict, keys, n - 1, remaining)

    knapsack_include = get_max_value_memoization(
        mem, knapsack, objects_dict, keys, n - 1, remaining - weight
    ).add_item(keys[n], objects_dict)   # Add the item after the processing

    knapsack_exclude = get_max_value_memoization(mem, knapsack, objects_dict, keys, n - 1, remaining)

    mem[(n, remaining)] = compare(knapsack_include, knapsack_exclude)   # Store the best calculated value
    return mem[(n, remaining)].copy()


# -------------------------------------------------------------------------
# Optimal solution
# -------------------------------------------------------------------------
def solve_knapsack_optimal(knapsack, objects_dict):
    keys = list(objects_dict.keys())
    return get_max_value(knapsack, objects_dict, keys, 0)


def get_max_value(knapsack, objects_dict, keys, current_index):
    """
    Brute-force algorithm checking each individual knapsack solution and landing the best one
    :param knapsack: current knapsack
    :param objects_dict: objects dictionary
    :param keys: List of the dictionary keys (used to work with indexes)
    :param current_index: the current index lol
    :return: the best knapsack solution within all possibilities
    """
    if current_index == len(keys) or knapsack.available_capacity == 0:
        return knapsack

    weight = objects_dict[keys[current_index]][1]

    # Follow the simple pattern : if the item can be added -> add it or don't then continue
    # End with a comparison between the two path
    if weight <= knapsack.available_capacity:
        knapsack_copy = knapsack.copy().add_item(keys[current_index], objects_dict)

        knapsack_include = get_max_value(knapsack_copy, objects_dict, keys, current_index + 1)
        knapsack_exclude = get_max_value(knapsack, objects_dict, keys, current_index + 1)

        return compare(knapsack_include, knapsack_exclude)

    # If it can't be added just go to the next item without the processing
    return get_max_value(knapsack, objects_dict, keys, current_index + 1)
