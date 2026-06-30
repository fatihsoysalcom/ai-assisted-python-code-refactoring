# main.py

def process_numbers_manual(numbers):
    """
    Developer's initial approach: Filters odd numbers and doubles even numbers
    using traditional loops.
    """
    print("  [Developer's Initial Attempt]")
    print(f"  Input numbers: {numbers}")

    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    print(f"  Step 1 (Filter Evens): {even_numbers}")

    doubled_evens = []
    for num in even_numbers:
        doubled_evens.append(num * 2)
    print(f"  Step 2 (Double Evens): {doubled_evens}")

    return doubled_evens

def process_numbers_ai_assisted(numbers):
    """
    AI-assisted approach: Achieves the same result using a more concise and
    Pythonic list comprehension, as an AI tool might suggest.
    """
    print("\n  [AI-Assisted Solution]")
    print(f"  Input numbers: {numbers}")

    # AI tools like GitHub Copilot or ChatGPT can suggest more efficient
    # and idiomatic ways to write code, such as list comprehensions.
    # This helps developers learn faster and solve problems more elegantly.
    doubled_evens = [num * 2 for num in numbers if num % 2 == 0]

    print(f"  AI-suggested (Filter & Double): {doubled_evens}")
    return doubled_evens

if __name__ == "__main__":
    print("--- Demonstrating AI as a Learning Catalyst for Developers ---")
    print("Problem: Given a list of numbers, filter out odd numbers and then double the remaining even numbers.")

    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("\n--- Scenario 1: Developer's Initial Approach ---")
    manual_result = process_numbers_manual(sample_numbers)
    print(f"  Final Result (Manual): {manual_result}")

    print("\n--- Scenario 2: AI-Assisted Refinement ---")
    print("  An AI tool (like Copilot or ChatGPT) could analyze the initial approach")
    print("  and suggest a more concise, Pythonic, and often more efficient alternative.")
    ai_result = process_numbers_ai_assisted(sample_numbers)
    print(f"  Final Result (AI-Assisted): {ai_result}")

    print("\n--- Conclusion ---")
    print("AI doesn't replace developers but transforms learning by:")
    print("1. Suggesting best practices and idiomatic code (e.g., list comprehensions).")
    print("2. Accelerating problem-solving by providing optimized or clearer solutions.")
    print("3. Acting as a continuous learning companion for new patterns and efficiencies.")
