# Digital Logic Gate Simulator

A Python program that simulates all fundamental digital logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR) and builds simple combinational circuits like adders — the building blocks of every computer processor.

## About This Project

This project demonstrates my understanding of:
- **Digital logic** — the foundation of ALL computer hardware
- **How computers perform arithmetic** — using only simple logic gates
- **Boolean algebra** — the mathematics behind digital circuits
- **Python programming** — functions, conditionals, and modular design

Every computer processor ever made — from a simple calculator to a modern laptop — is built from these exact logic gates. I built this simulator to understand how billions of tiny switches combine to perform complex computations.

## Features

| Feature | Description |
|---------|-------------|
| 7 Logic Gates | AND, OR, NOT, NAND, NOR, XOR, XNOR |
| Truth Tables | Auto-generated for any gate |
| Half Adder | Adds two single-bit numbers |
| Full Adder | Adds two bits with carry |
| 4-Bit Adder | Adds two 4-bit numbers (like a mini CPU!) |
| Multiplexer | 2-to-1 data selector |
| Educational Demo | Step-by-step explanation of how CPUs add |

## How to Run

### Prerequisites
- Python 3.7 or higher
- No external libraries needed

### Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/logic-gate-simulator.git
cd logic-gate-simulator
```

### Running the Interactive Simulator

```bash
python logic_gates.py
```

### Running Educational Demo

```bash
# Learn how computers add numbers using only logic gates
python examples/how_computers_add.py
```

### Running Tests

```bash
python tests/test_logic_gates.py
```

## How It Works

### What Are Logic Gates?

Logic gates are simple electronic circuits that take binary inputs (0 or 1) and produce a binary output based on a rule. They are the "atoms" of digital electronics.

### The 7 Basic Gates

```
AND: Output=1 only when BOTH inputs are 1
OR: Output=1 when AT LEAST ONE input is 1
NOT: Flips the input (0→1, 1→0)
NAND: Opposite of AND (universal gate!)
NOR: Opposite of OR (universal gate!)
XOR: Output=1 when inputs are DIFFERENT
XNOR: Output=1 when inputs are the SAME
```

### How Computers Add (The Key Insight!)

```
To add two bits:
  SUM = A XOR B (gives the addition result)
  CARRY = A AND B (gives the carry to next column)

This is a HALF ADDER — the simplest addition circuit!
```

Chain multiple adders together → you get a processor that can add any size numbers.

### Code Structure

```
logic-gate-simulator/
logic_gates.py # All gates + circuits + interactive menu
examples/
how_computers_add.py # Educational step-by-step demo
tests/
test_logic_gates.py # Unit tests (12 tests)
requirements.txt # No dependencies needed
README.md # This file
```

## Sample Output

```
  4-Bit Adder (adds two 4-bit binary numbers)
  ----------------------------------------
  Enter two 4-bit binary numbers:
  Number A (e.g., 0101): 0101
  Number B (e.g., 0011): 0011

    0101 (5)
  + 0011 (3)
  
   01000 (8)

  5 + 3 = 8
```

## What I Learned

- How logic gates are the building blocks of ALL digital systems
- How computers perform addition using nothing but simple switches
- What "universal gates" means (NAND/NOR can build anything)
- The connection between Boolean algebra and physical circuits
- How 25 billion gates in a modern CPU all work together

## Future Improvements

- Add a visual circuit diagram using ASCII art or Tkinter
- Implement a subtractor using two's complement
- Build a 4-bit ALU (Arithmetic Logic Unit)
- Add sequential logic (flip-flops, registers, memory)
- Simulate a simple clock signal

## References

- Logic Gates: [Wikipedia](https://en.wikipedia.org/wiki/Logic_gate)
- Binary Adder: [Wikipedia](https://en.wikipedia.org/wiki/Adder_(electronics))
- Boolean Algebra: [All About Circuits](https://www.allaboutcircuits.com/textbook/digital/)

## Author

**[Student Name]** — Aspiring Electrical & Computer Engineering Student

---

*Built with Python 3 | No external dependencies required*