"""
How Computers Add Numbers
======================================================
Shows step-by-step how logic gates perform binary addition,
which is the basis of all arithmetic in a computer.

Run with: python examples/how_computers_add.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_gates import half_adder, full_adder, four_bit_adder, AND_gate, XOR_gate

def demo_1_basic_concept():
    """Explain the basic concept of how computers add."""
    print("=" * 55)
    print(" HOW COMPUTERS ADD NUMBERS")
    print(" (Using only AND and XOR gates!)")
    print("=" * 55)
    print()
    print(" Computers don't 'know' math. They use logic gates")
    print(" (simple electronic switches) to perform addition.")
    print()
    print(" The key insight:")
    print(" XOR gate gives us the SUM of two bits")
    print(" AND gate gives us the CARRY")
    print()
    print(" Binary addition rules:")
    print(" 0 + 0 = 0 (sum=0, carry=0)")
    print(" 0 + 1 = 1 (sum=1, carry=0)")
    print(" 1 + 0 = 1 (sum=1, carry=0)")
    print(" 1 + 1 = 10 (sum=0, carry=1) ← like 5+5=10 in decimal!")
    print()

def demo_2_half_adder_detail():
    """Show the half adder working step by step."""
    print("\n" + "=" * 55)
    print(" THE HALF ADDER — Adding Two Single Bits")
    print("=" * 55)
    print()
    print(" A half adder uses just 2 gates:")
    print(" Sum = A XOR B")
    print(" Carry = A AND B")
    print()
    print(" Let's see all possible additions:")
    print(" " + "-" * 45)
    print(f" {'A':<4} {'B':<4} {'XOR(Sum)':<10} {'AND(Carry)':<12} {'Result'}")
    print(f" {' '*4} {' '*4} {' '*10} {' '*12} {' '*8}")

    for a in [0, 1]:
        for b in [0, 1]:
            s, c = half_adder(a, b)
            decimal_result = c * 2 + s
            print(f" {a:<4} {b:<4} {s:<10} {c:<12} {c}{s} = {decimal_result}")

    print()
    print(" Notice: 1 + 1 = 10 in binary (which is 2 in decimal)")
    print(" The carry bit moves to the next column — just like")
    print(" carrying a 1 when you add 5+5=10 in decimal!")
    print()

def demo_3_full_adder_detail():
    """Show how full adder handles carry from previous column."""
    print("\n" + "=" * 55)
    print(" THE FULL ADDER — Adding With Carry")
    print("=" * 55)
    print()
    print(" When adding multi-bit numbers, we need to handle")
    print(" the carry from the previous column.")
    print()
    print(" A full adder takes THREE inputs: A, B, and Carry-In")
    print()
    print(" Example: Adding 11 + 01 (3 + 1 = 4)")
    print(" " + "-" * 45)
    print()
    print(" 1 1 (3 in decimal)")
    print(" + 0 1 (1 in decimal)")
    print(" ")

    # Column 0 (rightmost): 1 + 1 + carry(0)
    s0, c0 = full_adder(1, 1, 0)
    print(f" Column 0: 1 + 1 + carry(0) = sum={s0}, carry={c0}")

    # Column 1: 1 + 0 + carry from column 0
    s1, c1 = full_adder(1, 0, c0)
    print(f" Column 1: 1 + 0 + carry({c0}) = sum={s1}, carry={c1}")

    print(f"\n Result: {c1}{s1}{s0} = {c1*4 + s1*2 + s0} in decimal ")
    print()

def demo_4_four_bit_addition():
    """Demonstrate 4-bit addition with multiple examples."""
    print("\n" + "=" * 55)
    print(" 4-BIT ADDER — How a CPU Adds Numbers")
    print("=" * 55)
    print()
    print(" A 4-bit adder chains 4 full adders together.")
    print(" Each handles one column, passing its carry to the next.")
    print()

    examples = [
        ([0, 0, 1, 1], [0, 1, 0, 1]), # 3 + 5 = 8
        ([0, 1, 1, 0], [0, 0, 1, 1]), # 6 + 3 = 9
        ([1, 0, 1, 0], [0, 1, 0, 1]), # 10 + 5 = 15
        ([1, 1, 1, 1], [0, 0, 0, 1]), # 15 + 1 = 16 (overflow!)
    ]

    for a_bits, b_bits in examples:
        result, carry = four_bit_adder(a_bits, b_bits)

        a_str = "".join(str(x) for x in a_bits)
        b_str = "".join(str(x) for x in b_bits)
        r_str = "".join(str(x) for x in result)

        a_dec = int(a_str, 2)
        b_dec = int(b_str, 2)
        r_dec = int(f"{carry}" + r_str, 2)

        print(f" {a_str} ({a_dec:>2})")
        print(f" + {b_str} ({b_dec:>2})")
        print(f" ")
        print(f" {carry} {r_str} ({r_dec:>2})")

        if carry:
            print(f" OVERFLOW — result needs more than 4 bits!")
        print()

    print(" This is EXACTLY how your computer's processor adds numbers.")
    print(" A 64-bit CPU uses 64 full adders chained together!")
    print()

def demo_5_scale():
    """Show how this scales to real processors."""
    print("\n" + "=" * 55)
    print(" FROM GATES TO PROCESSORS")
    print("=" * 55)
    print()
    print(" Modern CPUs contain BILLIONS of logic gates:")
    print()
    print(f" {'Component':<25} {'Gates Used':<20}")
    print(f" {' '*25} {' '*20}")
    print(f" {'1 Half Adder':<25} {'2 gates (XOR + AND)':<20}")
    print(f" {'1 Full Adder':<25} {'5 gates':<20}")
    print(f" {'4-Bit Adder':<25} {'~20 gates':<20}")
    print(f" {'32-Bit Adder':<25} {'~160 gates':<20}")
    print(f" {'64-Bit Adder':<25} {'~320 gates':<20}")
    print(f" {'Simple Calculator':<25} {'~10,000 gates':<20}")
    print(f" {'Modern CPU (M3 chip)':<25} {'~25 BILLION gates':<20}")
    print()
    print(" Every single one of those billions of gates is just")
    print(" a simple AND, OR, NOT, NAND, or XOR — the same gates")
    print(" this program simulates!")
    print()

if __name__ == "__main__":
    print()
    demo_1_basic_concept()
    demo_2_half_adder_detail()
    demo_3_full_adder_detail()
    demo_4_four_bit_addition()
    demo_5_scale()
    print("=" * 55)
    print(" Demo complete! Now you know how computers really add.")
    print("=" * 55)
    print()
