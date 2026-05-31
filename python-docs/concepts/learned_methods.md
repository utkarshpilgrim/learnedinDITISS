### Chained Comparison

```
# Assumes i is smaller than j. Loop stops when the larger index (j) hits the limit.
while i < j < len(my_string):
    # Your code here
    i += 1

```


### Compare, Select, and Concatenate

```python3
def process_string(main_string):
    # 1. Initialize pointers and the result string
    i = 0
    j = 1
    new_string = ""
    
    # 2. Loop while both pointers are within bounds
    while i < len(main_string) and j < len(main_string):
        char1 = main_string[i]
        char2 = main_string[j]
        
        # --- COMPARE & SELECT STEP ---
        # Example rule: Select the character that comes first alphabetically
        if char1 < char2:
            selected_char = char1
        elif char2 < char1:
            selected_char = char2
        else:
            selected_char = "" # Skip if they are identical
            
        # --- CONCATENATE STEP ---
        if selected_char: # Only concatenate if a character was selected
            new_string += selected_char
            
        # Move pointers forward (e.g., checking pairs: 0&1, 2&3, etc.)
        i += 2
        j += 2
        
    return new_string

# Example testing
input_text = "badcfe" # Compares (b,a), (d,c), (f,e)
output_text = process_string(input_text)

print(f"Original: {input_text}")
print(f"Processed: {output_text}") 
# Output: "ace" (selected 'a' over 'b', 'c' over 'd', 'e' over 'f')
```

### Find the length of Longest String

```
# Returns the maximum character length found
return max(len(s) for s in strings_list)

# Example with ["apple", "hi"]: returns 5
```
