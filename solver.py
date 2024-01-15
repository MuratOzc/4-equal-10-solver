from itertools import permutations

def generate_all_number_permutations(numbers):
    """
    Generate all permutations of the given numbers.
    """
    return list(permutations(numbers))

def parse_input(input_str):
    """
    Extract numbers and determine disallowed operations from the input string.
    """
    # Extract numbers
    numbers = [int(input_str[i]) for i in range(4)]

    # Default to all operations allowed
    allowed_ops = ['+', '-', '*', '/']
    allow_parentheses = True

    # Remove disallowed operations based on the input
    if len(input_str) > 4:
        for char in input_str[4:]:
            if char in allowed_ops:
                allowed_ops.remove(char)
            elif char == 'p':
                allow_parentheses = False

    return numbers, allowed_ops, allow_parentheses

def generate_expressions(numbers, allowed_ops, allow_parentheses):
    """
    Generate all possible expressions with a single set of parentheses, or none, according to the rules.
    """
    expressions = []
    ops = [op for op in allowed_ops if op in ['+', '-', '*', '/']]

    # Generate expressions without parentheses
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expr_no_paren = f"{numbers[0]}{op1}{numbers[1]}{op2}{numbers[2]}{op3}{numbers[3]}"
                expressions.append(expr_no_paren)
                if allow_parentheses:
                    # Generate expressions with a single set of parentheses
                    exprs_with_paren = [
                        f"({numbers[0]}{op1}{numbers[1]}){op2}{numbers[2]}{op3}{numbers[3]}",
                        f"{numbers[0]}{op1}({numbers[1]}{op2}{numbers[2]}){op3}{numbers[3]}",
                        f"{numbers[0]}{op1}{numbers[1]}{op2}({numbers[2]}{op3}{numbers[3]})",
                        f"{numbers[0]}{op1}({numbers[1]}{op2}{numbers[2]}{op3}{numbers[3]})",
                        f"({numbers[0]}{op1}{numbers[1]}{op2}{numbers[2]}){op3}{numbers[3]}"
                    ]
                    expressions.extend(exprs_with_paren)

    return expressions

def solve_game(input_str):
    """
    Solve the game by finding expressions that evaluate to 10 using the given input string.
    Consider all permutations of the numbers.
    """
    numbers, allowed_ops, allow_parentheses = parse_input(input_str)
    all_permutations = generate_all_number_permutations(numbers)
    solutions = set()

    for perm in all_permutations:
        expressions = generate_expressions(perm, allowed_ops, allow_parentheses)
        for expr in expressions:
            try:
                if eval(expr) == 10:
                    solutions.add(expr)
            except ZeroDivisionError:
                continue
    return list(solutions)

while True:
    # Ask for user input
    input_str = input("####################################################################\n\nEnter 4 numbers followed by disallowed operations (e.g., '1853', '1853+', '1853p*/'): ")
        
    # Process the input and find solutions
    solutions = solve_game(input_str)
        
    # Output the solutions
    if solutions:
        print(f"\nSolution:\n\n{solutions[:1]}\n")
        print(f"\nAll solutions:{solutions}\n")
        print(f"\nNumber of solutions: {len(solutions)}\n")
    else:
        print("\nNo solutions found.\n")