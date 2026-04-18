from utils import Grid, DELETION_COST, REPLACE_COST, INSERTION_COST


def min_edit_distance(distance_matrix: Grid, source: str, target: str) -> int:
    n = len(source)
    m = len(target)
    
    distance_matrix[0, 0] = 0

    for i in range(1, n+1):
        distance_matrix[i, 0] = distance_matrix[i - 1, 0] + DELETION_COST
    
    for j in range(1, m+1):
        distance_matrix[0, j] = distance_matrix[0, j - 1] + INSERTION_COST
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            replace_cost_adjusted_for_same_elements = 0 if source[i - 1] == target[j - 1] else REPLACE_COST

            distance_matrix[i, j] = min(
                distance_matrix[i - 1, j] + DELETION_COST,
                distance_matrix[i - 1, j - 1] + replace_cost_adjusted_for_same_elements,
                distance_matrix[i, j - 1] + INSERTION_COST
            )

    for row in distance_matrix:
        print(row)
    
    return distance_matrix[n, m]


def main():
    source = input("Enter the source string: ")
    target = input("Enter the target string: ")

    distance_matrix = Grid(n=len(source) + 1, m=len(target) + 1)
    min_distance = min_edit_distance(distance_matrix=distance_matrix, source=source, target=target)

    print(f"Minimum edit distance of {source} to {target} is {min_distance}")


if __name__ == "__main__":
    main()
