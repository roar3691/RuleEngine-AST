# Rule Engine with Abstract Syntax Tree (AST)

A sophisticated rule engine implementation using Abstract Syntax Tree for dynamic rule creation, combination, and evaluation. This 3-tier application provides a flexible framework for determining user eligibility based on various attributes like age, department, income, and experience.

## Project Overview

The Rule Engine is designed to:
- Create and manage conditional rules using AST
- Combine multiple rules efficiently
- Evaluate rules against user data
- Provide a simple web interface for rule management
- Store and retrieve rules using SQLite database

## Technical Architecture

### Data Structure
The system implements an Abstract Syntax Tree (AST) with the following node structure:
```python
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type    # "operator" or "operand"
        self.left = left         # Left child node
        self.right = right       # Right child node
        self.value = value       # Value for operand nodes
