"""
Logic Gate Simulator
=====================
Simulates fundamental digital logic gates and builds simple
combinational circuits — the building blocks of all digital electronics.

Author: [Student Name]
Purpose: Demonstrating understanding of digital logic — the foundation
         of computer processors, memory, and all digital systems.
"""


# ============================================================
# BASIC LOGIC GATES
# ============================================================

def AND_gate(a, b):
    """
    AND Gate: Output is 1 ONLY when BOTH inputs are 1.

    Real-world analogy: Two switches in SERIES — both must be ON
    for the light to turn on.

    Truth Table:
        A | B | Output
        0 | 0 |   0
        0 | 1 |   0
        1 | 0 |   0
        1 | 1 |   1

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    if a == 1 and b == 1:
        return 1
    return 0


def OR_gate(a, b):
    """
    OR Gate: Output is 1 when AT LEAST ONE input is 1.

    Real-world analogy: Two switches in PARALLEL — either one
    can turn on the light.

    Truth Table:
        A | B | Output
        0 | 0 |   0
        0 | 1 |   1
        1 | 0 |   1
        1 | 1 |   1

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    if a == 1 or b == 1:
        return 1
    return 0


def NOT_gate(a):
    """
    NOT Gate (Inverter): Flips the input. 0 becomes 1, 1 becomes 0.

    Real-world analogy: A normally-closed switch — when you press it,
    the light turns OFF instead of on.

    Truth Table:
        A | Output
        0 |   1
        1 |   0

    Args:
        a (int): Input (0 or 1)

    Returns:
        int: Inverted output (0 or 1)
    """
    if a == 0:
        return 1
    return 0


def NAND_gate(a, b):
    """
    NAND Gate: NOT-AND. Output is 0 ONLY when both inputs are 1.
    (Opposite of AND gate)

    NAND is called a "universal gate" because you can build ANY
    other gate using only NAND gates!

    Truth Table:
        A | B | Output
        0 | 0 |   1
        0 | 1 |   1
        1 | 0 |   1
        1 | 1 |   0

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    return NOT_gate(AND_gate(a, b))


def NOR_gate(a, b):
    """
    NOR Gate: NOT-OR. Output is 1 ONLY when both inputs are 0.
    (Opposite of OR gate)

    NOR is also a "universal gate" — like NAND, you can build
    anything with just NOR gates.

    Truth Table:
        A | B | Output
        0 | 0 |   1
        0 | 1 |   0
        1 | 0 |   0
        1 | 1 |   0

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    return NOT_gate(OR_gate(a, b))


def XOR_gate(a, b):
    """
    XOR Gate (Exclusive OR): Output is 1 when inputs are DIFFERENT.

    XOR is used in addition circuits and error detection.

    Truth Table:
        A | B | Output
        0 | 0 |   0
        0 | 1 |   1
        1 | 0 |   1
        1 | 1 |   0

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    if a != b:
        return 1
    return 0


def XNOR_gate(a, b):
    """
    XNOR Gate (Exclusive NOR): Output is 1 when inputs are THE SAME.
    (Opposite of XOR)

    Used in equality comparators.

    Truth Table:
        A | B | Output
        0 | 0 |   1
        0 | 1 |   0
        1 | 0 |   0
        1 | 1 |   1

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)

    Returns:
        int: Output (0 or 1)
    """
    return NOT_gate(XOR_gate(a, b))


# ============================================================
# COMBINATIONAL CIRCUITS (Built from basic gates)
# ============================================================

def half_adder(a, b):
    """
    Half Adder: Adds two single bits.

    A half adder is the simplest addition circuit. It produces:
    - Sum (S) = A XOR B
    - Carry (C) = A AND B

    This is how computers add numbers at the hardware level!

    Args:
        a (int): First bit (0 or 1)
        b (int): Second bit (0 or 1)

    Returns:
        tuple: (sum_bit, carry_bit)
    """
    sum_bit = XOR_gate(a, b)
    carry_bit = AND_gate(a, b)
    return (sum_bit, carry_bit)


def full_adder(a, b, carry_in):
    """
    Full Adder: Adds two bits plus a carry-in from a previous addition.

    Full adders are chained together to add multi-bit numbers.
    A 32-bit processor uses 32 full adders connected in series!

    Args:
        a (int): First bit (0 or 1)
        b (int): Second bit (0 or 1)
        carry_in (int): Carry from previous stage (0 or 1)

    Returns:
        tuple: (sum_bit, carry_out)
    """
    # First half adder: add A and B
    sum1, carry1 = half_adder(a, b)

    # Second half adder: add first sum with carry_in
    sum_out, carry2 = half_adder(sum1, carry_in)

    # Final carry: OR of both carries
    carry_out = OR_gate(carry1, carry2)

    return (sum_out, carry_out)


def four_bit_adder(a_bits, b_bits):
    """
    4-Bit Adder: Adds two 4-bit binary numbers using full adders.

    This is a simplified version of what's inside every CPU!

    Args:
        a_bits (list): 4 bits [MSB, ..., LSB] for first number
        b_bits (list): 4 bits [MSB, ..., LSB] for second number

    Returns:
        tuple: (result_bits as list, carry_out)
    """
    result = [0, 0, 0, 0]
    carry = 0

    # Add from LSB (rightmost) to MSB (leftmost)
    for i in range(3, -1, -1):
        sum_bit, carry = full_adder(a_bits[i], b_bits[i], carry)
        result[i] = sum_bit

    return (result, carry)


def multiplexer_2to1(a, b, select):
    """
    2-to-1 Multiplexer: Selects one of two inputs based on a select signal.

    Like a railway switch — directs one of two inputs to the output.

    When select = 0: output = A
    When select = 1: output = B

    Args:
        a (int): Input A (0 or 1)
        b (int): Input B (0 or 1)
        select (int): Select signal (0 or 1)

    Returns:
        int: Selected output (0 or 1)
    """
    # Output = (NOT select AND A) OR (select AND B)
    term1 = AND_gate(NOT_gate(select), a)
    term2 = AND_gate(select, b)
    return OR_gate(term1, term2)


# ============================================================
# TRUTH TABLE GENERATOR
# ============================================================

def generate_truth_table(gate_name, gate_function, num_inputs=2):
    """
    Generate and display a complete truth table for any gate.

    Args:
        gate_name (str): Name of the gate.
        gate_function (callable): The gate function.
        num_inputs (int): Number of inputs (1 or 2).
    """
    print(f"\n  {gate_name} Gate — Truth Table")
    print("  " + "-" * 30)

    if num_inputs == 1:
        print(f"  {'A':<5} | {'Output':<8}")
        print(f"  {'─'*5} | {'─'*8}")
        for a in [0, 1]:
            output = gate_function(a)
            print(f"  {a:<5} | {output:<8}")
    else:
        print(f"  {'A':<5} {'B':<5} | {'Output':<8}")
        print(f"  {'─'*5} {'─'*5} | {'─'*8}")
        for a in [0, 1]:
            for b in [0, 1]:
                output = gate_function(a, b)
                print(f"  {a:<5} {b:<5} | {output:<8}")

    print()


# ============================================================
# INTERACTIVE PROGRAM
# ============================================================

def display_banner():
    """Display the program banner."""
    print()
    print("=" * 55)
    print("  🔲 DIGITAL LOGIC GATE SIMULATOR")
    print("  The Building Blocks of All Computers")
    print("=" * 55)


def display_menu():
    """Display the main menu."""
    print("\n  Choose an operation:")
    print("  " + "-" * 45)
    print("  --- Basic Gates ---")
    print("  1.  AND Gate")
    print("  2.  OR Gate")
    print("  3.  NOT Gate")
    print("  4.  NAND Gate (universal)")
    print("  5.  NOR Gate (universal)")
    print("  6.  XOR Gate")
    print("  7.  XNOR Gate")
    print("  --- Circuits ---")
    print("  8.  Half Adder (adds 2 bits)")
    print("  9.  Full Adder (adds 2 bits + carry)")
    print("  10. 4-Bit Adder (adds two 4-bit numbers)")
    print("  11. 2-to-1 Multiplexer")
    print("  --- Display ---")
    print("  12. Show ALL truth tables")
    print("  13. Exit")
    print("  " + "-" * 45)


def get_bit_input(prompt):
    """Get a valid bit (0 or 1) from the user."""
    while True:
        value = input(prompt).strip()
        if value in ['0', '1']:
            return int(value)
        print("  ⚠ Please enter 0 or 1 only.")


def get_4bit_input(prompt):
    """Get a valid 4-bit binary number from the user."""
    while True:
        value = input(prompt).strip()
        if len(value) == 4 and all(c in '01' for c in value):
            return [int(c) for c in value]
        print("  ⚠ Please enter exactly 4 binary digits (e.g., 1010).")


def run_basic_gate(gate_name, gate_function, num_inputs):
    """Run a basic gate interactively."""
    print(f"\n  {gate_name} Gate")
    print("  " + "-" * 30)

    if num_inputs == 1:
        a = get_bit_input("  Enter input A (0 or 1): ")
        result = gate_function(a)
        print(f"\n  ✅ {gate_name}({a}) = {result}")
    else:
        a = get_bit_input("  Enter input A (0 or 1): ")
        b = get_bit_input("  Enter input B (0 or 1): ")
        result = gate_function(a, b)
        print(f"\n  ✅ {gate_name}({a}, {b}) = {result}")

    generate_truth_table(gate_name, gate_function, num_inputs)


def run_half_adder():
    """Run the half adder interactively."""
    print("\n  Half Adder (adds two 1-bit numbers)")
    print("  " + "-" * 30)
    a = get_bit_input("  Enter bit A (0 or 1): ")
    b = get_bit_input("  Enter bit B (0 or 1): ")

    sum_bit, carry = half_adder(a, b)

    print(f"\n  ✅ {a} + {b} =")
    print(f"     Sum   = {sum_bit}")
    print(f"     Carry = {carry}")
    print(f"     Result: {carry}{sum_bit} (binary) = {carry * 2 + sum_bit} (decimal)")


def run_full_adder():
    """Run the full adder interactively."""
    print("\n  Full Adder (adds two bits + carry in)")
    print("  " + "-" * 30)
    a = get_bit_input("  Enter bit A (0 or 1): ")
    b = get_bit_input("  Enter bit B (0 or 1): ")
    cin = get_bit_input("  Enter carry-in (0 or 1): ")

    sum_bit, carry_out = full_adder(a, b, cin)

    print(f"\n  ✅ {a} + {b} + carry({cin}) =")
    print(f"     Sum       = {sum_bit}")
    print(f"     Carry Out = {carry_out}")
    decimal_result = carry_out * 2 + sum_bit
    print(f"     Result: {carry_out}{sum_bit} (binary) = {decimal_result} (decimal)")


def run_4bit_adder():
    """Run the 4-bit adder interactively."""
    print("\n  4-Bit Adder (adds two 4-bit binary numbers)")
    print("  " + "-" * 30)
    print("  Enter two 4-bit binary numbers:")
    a_bits = get_4bit_input("  Number A (e.g., 0101): ")
    b_bits = get_4bit_input("  Number B (e.g., 0011): ")

    result, carry = four_bit_adder(a_bits, b_bits)

    a_str = "".join(str(x) for x in a_bits)
    b_str = "".join(str(x) for x in b_bits)
    r_str = "".join(str(x) for x in result)

    # Convert to decimal for verification
    a_dec = int(a_str, 2)
    b_dec = int(b_str, 2)
    r_dec = int(r_str, 2) + (carry * 16)

    print(f"\n    {a_str}  ({a_dec})")
    print(f"  + {b_str}  ({b_dec})")
    print(f"  ─────────")
    print(f"   {carry}{r_str}  ({r_dec})")
    print(f"\n  ✅ {a_dec} + {b_dec} = {r_dec}")

    if carry:
        print(f"     ⚠ Overflow! Result needs 5 bits (carry = {carry})")


def run_multiplexer():
    """Run the 2-to-1 multiplexer interactively."""
    print("\n  2-to-1 Multiplexer (data selector)")
    print("  " + "-" * 30)
    print("  When select=0 → output=A, When select=1 → output=B")
    a = get_bit_input("  Enter input A (0 or 1): ")
    b = get_bit_input("  Enter input B (0 or 1): ")
    sel = get_bit_input("  Enter select (0 or 1): ")

    output = multiplexer_2to1(a, b, sel)

    selected_input = "A" if sel == 0 else "B"
    print(f"\n  ✅ MUX(A={a}, B={b}, Select={sel}) = {output}")
    print(f"     Selected input {selected_input} → Output = {output}")


def show_all_truth_tables():
    """Display truth tables for all gates."""
    print("\n  ALL LOGIC GATE TRUTH TABLES")
    print("  " + "=" * 40)
    generate_truth_table("AND", AND_gate, 2)
    generate_truth_table("OR", OR_gate, 2)
    generate_truth_table("NOT", NOT_gate, 1)
    generate_truth_table("NAND", NAND_gate, 2)
    generate_truth_table("NOR", NOR_gate, 2)
    generate_truth_table("XOR", XOR_gate, 2)
    generate_truth_table("XNOR", XNOR_gate, 2)


def main():
    """Main program loop."""
    display_banner()

    while True:
        display_menu()
        choice = input("\n  Enter choice (1-13): ").strip()

        if choice == "1":
            run_basic_gate("AND", AND_gate, 2)
        elif choice == "2":
            run_basic_gate("OR", OR_gate, 2)
        elif choice == "3":
            run_basic_gate("NOT", NOT_gate, 1)
        elif choice == "4":
            run_basic_gate("NAND", NAND_gate, 2)
        elif choice == "5":
            run_basic_gate("NOR", NOR_gate, 2)
        elif choice == "6":
            run_basic_gate("XOR", XOR_gate, 2)
        elif choice == "7":
            run_basic_gate("XNOR", XNOR_gate, 2)
        elif choice == "8":
            run_half_adder()
        elif choice == "9":
            run_full_adder()
        elif choice == "10":
            run_4bit_adder()
        elif choice == "11":
            run_multiplexer()
        elif choice == "12":
            show_all_truth_tables()
        elif choice == "13":
            print("\n  Thank you for using Logic Gate Simulator! Goodbye.\n")
            break
        else:
            print("  ⚠ Invalid choice. Please enter 1-13.")

        print()


if __name__ == "__main__":
    main()