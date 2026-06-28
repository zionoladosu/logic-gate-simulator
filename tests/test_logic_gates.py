"""
Unit Tests for Logic Gate Simulator
=====================================
Verifies all logic gates and circuits produce correct outputs.
Run with: python tests/test_logic_gates.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_gates import (
    AND_gate, OR_gate, NOT_gate, NAND_gate, NOR_gate,
    XOR_gate, XNOR_gate, half_adder, full_adder,
    four_bit_adder, multiplexer_2to1
)

def test_AND_gate():
    """Test AND gate truth table."""
    assert AND_gate(0, 0) == 0
    assert AND_gate(0, 1) == 0
    assert AND_gate(1, 0) == 0
    assert AND_gate(1, 1) == 1
    print(" AND gate: PASSED")

def test_OR_gate():
    """Test OR gate truth table."""
    assert OR_gate(0, 0) == 0
    assert OR_gate(0, 1) == 1
    assert OR_gate(1, 0) == 1
    assert OR_gate(1, 1) == 1
    print(" OR gate: PASSED")

def test_NOT_gate():
    """Test NOT gate truth table."""
    assert NOT_gate(0) == 1
    assert NOT_gate(1) == 0
    print(" NOT gate: PASSED")

def test_NAND_gate():
    """Test NAND gate truth table (opposite of AND)."""
    assert NAND_gate(0, 0) == 1
    assert NAND_gate(0, 1) == 1
    assert NAND_gate(1, 0) == 1
    assert NAND_gate(1, 1) == 0
    print(" NAND gate: PASSED")

def test_NOR_gate():
    """Test NOR gate truth table (opposite of OR)."""
    assert NOR_gate(0, 0) == 1
    assert NOR_gate(0, 1) == 0
    assert NOR_gate(1, 0) == 0
    assert NOR_gate(1, 1) == 0
    print(" NOR gate: PASSED")

def test_XOR_gate():
    """Test XOR gate truth table (different inputs → 1)."""
    assert XOR_gate(0, 0) == 0
    assert XOR_gate(0, 1) == 1
    assert XOR_gate(1, 0) == 1
    assert XOR_gate(1, 1) == 0
    print(" XOR gate: PASSED")

def test_XNOR_gate():
    """Test XNOR gate truth table (same inputs → 1)."""
    assert XNOR_gate(0, 0) == 1
    assert XNOR_gate(0, 1) == 0
    assert XNOR_gate(1, 0) == 0
    assert XNOR_gate(1, 1) == 1
    print(" XNOR gate: PASSED")

def test_half_adder():
    """Test half adder: adds two bits."""
    assert half_adder(0, 0) == (0, 0) # 0+0 = 0, carry 0
    assert half_adder(0, 1) == (1, 0) # 0+1 = 1, carry 0
    assert half_adder(1, 0) == (1, 0) # 1+0 = 1, carry 0
    assert half_adder(1, 1) == (0, 1) # 1+1 = 0, carry 1 (binary 10)
    print(" Half adder: PASSED")

def test_full_adder():
    """Test full adder: adds two bits + carry in."""
    assert full_adder(0, 0, 0) == (0, 0) # 0+0+0 = 0
    assert full_adder(0, 0, 1) == (1, 0) # 0+0+1 = 1
    assert full_adder(0, 1, 0) == (1, 0) # 0+1+0 = 1
    assert full_adder(0, 1, 1) == (0, 1) # 0+1+1 = 10
    assert full_adder(1, 0, 0) == (1, 0) # 1+0+0 = 1
    assert full_adder(1, 0, 1) == (0, 1) # 1+0+1 = 10
    assert full_adder(1, 1, 0) == (0, 1) # 1+1+0 = 10
    assert full_adder(1, 1, 1) == (1, 1) # 1+1+1 = 11
    print(" Full adder: PASSED")

def test_4bit_adder():
    """Test 4-bit adder with various additions."""
    # 5 + 3 = 8 → 0101 + 0011 = 1000
    result, carry = four_bit_adder([0, 1, 0, 1], [0, 0, 1, 1])
    assert result == [1, 0, 0, 0] and carry == 0

    # 7 + 1 = 8 → 0111 + 0001 = 1000
    result, carry = four_bit_adder([0, 1, 1, 1], [0, 0, 0, 1])
    assert result == [1, 0, 0, 0] and carry == 0

    # 15 + 1 = 16 → 1111 + 0001 = 10000 (overflow!)
    result, carry = four_bit_adder([1, 1, 1, 1], [0, 0, 0, 1])
    assert result == [0, 0, 0, 0] and carry == 1

    # 0 + 0 = 0
    result, carry = four_bit_adder([0, 0, 0, 0], [0, 0, 0, 0])
    assert result == [0, 0, 0, 0] and carry == 0

    print(" 4-bit adder: PASSED")

def test_multiplexer():
    """Test 2-to-1 multiplexer."""
    # Select = 0 → output = A
    assert multiplexer_2to1(0, 1, 0) == 0 # A=0 selected
    assert multiplexer_2to1(1, 0, 0) == 1 # A=1 selected

    # Select = 1 → output = B
    assert multiplexer_2to1(0, 1, 1) == 1 # B=1 selected
    assert multiplexer_2to1(1, 0, 1) == 0 # B=0 selected

    print(" 2-to-1 Multiplexer: PASSED")

def test_nand_is_universal():
    """
    Test that NAND can build other gates (universal gate property).
    NOT from NAND: NOT(A) = NAND(A, A)
    AND from NAND: AND(A,B) = NOT(NAND(A,B)) = NAND(NAND(A,B), NAND(A,B))
    """
    # NOT using NAND
    for a in [0, 1]:
        assert NAND_gate(a, a) == NOT_gate(a)

    # AND using NAND
    for a in [0, 1]:
        for b in [0, 1]:
            nand_result = NAND_gate(a, b)
            and_from_nand = NAND_gate(nand_result, nand_result)
            assert and_from_nand == AND_gate(a, b)

    print(" NAND universality (builds NOT and AND): PASSED")

def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 55)
    print(" LOGIC GATE SIMULATOR - TEST SUITE")
    print("=" * 55 + "\n")

    test_AND_gate()
    test_OR_gate()
    test_NOT_gate()
    test_NAND_gate()
    test_NOR_gate()
    test_XOR_gate()
    test_XNOR_gate()
    test_half_adder()
    test_full_adder()
    test_4bit_adder()
    test_multiplexer()
    test_nand_is_universal()

    print("\n" + "=" * 55)
    print(" ALL 12 TESTS PASSED ")
    print("=" * 55 + "\n")

if __name__ == "__main__":
    run_all_tests()