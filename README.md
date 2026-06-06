# Lab: Object Oriented Programming (OOP) - Part 2: Cash Register

## Description

A Python implementation of a `CashRegister` class that simulates
core e-commerce cash register functionality, built as part of the
Moringa School OOP curriculum.

## Features

- Add items with name, price, and quantity
- Apply percentage-based discounts to the total
- Void (undo) the last transaction
- Validates discount values (must be integer, 0–100)

## Class Design

### Attributes
| Attribute | Type | Default | Description |
|---|---|---|---|
| `discount` | int | 0 | Percentage discount (0–100) |
| `total` | float | 0 | Running total |
| `items` | list | [] | Names of added items |
| `previous_transactions` | list | [] | History of transactions |

### Methods
| Method | Description |
|---|---|
| `add_item(item, price, quantity=1)` | Adds item and updates total |
| `apply_discount()` | Applies discount % to total |
| `void_last_transaction()` | Removes last transaction |

## Usage

```python
register = CashRegister(discount=20)

register.add_item("apple", 1.50, 3)
register.add_item("bread", 2.00)

register.apply_discount()
# After the discount, the total comes to $3.60.

register.void_last_transaction()
```

## Setup

```bash
git clone <your-fork-url>
cd lab-object-oriented-programming-part-2-cash-register
npm install  # for tests
```

## Screenshot

![Cash Register Demo](screenshot.png)

## Author

Nesh