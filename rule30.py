def rule_30(start_row, num_rows):
    length = len(start_row)
    for _ in range(num_rows):
        # Print the current row
        print(''.join(str(cell) for cell in start_row))
        
        # Generate the next row
        new_row = []
        for i in range(length):
            # Determine the left, center, and right values
            left = start_row[i - 1] if i > 0 else 0
            center = start_row[i]
            right = start_row[i + 1] if i < length - 1 else 0

            # Apply Rule 30
            new_value = left ^ (center or right)
            new_row.append(new_value)
        
        start_row = new_row

# Example usage
initial_row = [0]*30 + [1] + [0]*30  # a single 1 in the middle of 31 cells
rule_30(initial_row, 30)
