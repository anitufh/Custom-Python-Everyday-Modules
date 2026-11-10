"""Runnable examples that use the helpers from :mod:`custom_print`.

Run this file with ``python print.py`` to see a shopping plan, a numbered
task list, a small expense summary, and a boxed reminder.
"""

from custom_print import (
    print_bullets,
    print_box,
    print_heading,
    print_numbered_list,
    print_separator,
)


def show_shopping_plan() -> None:
    """Display a practical meal-prep shopping plan."""
    print_heading("Weekly Meal Prep Plan", "=")
    print("Meals: vegetable pasta, rice bowls, and overnight oats")

    print_heading("Shopping list")
    print_bullets(
        [
            "Pasta - 500 g",
            "Rice - 1 kg",
            "Mixed vegetables - 1 kg",
            "Rolled oats - 500 g",
            "Milk - 2 litres",
        ],
        bullet="*",
    )

    print_heading("Preparation steps")
    print_numbered_list(
        [
            "Wash and chop the vegetables.",
            "Cook rice and pasta for the first few meals.",
            "Portion meals into containers and refrigerate.",
            "Prepare overnight oats the evening before.",
        ]
    )


def show_expense_summary() -> None:
    """Calculate and display the total for a small grocery receipt."""
    print_separator(40, "-")
    print_heading("Grocery Expense Summary")
    expenses = [("Pasta", 120.00), ("Vegetables", 240.50), ("Oats", 180.00)]

    for name, price in expenses:
        print(f"{name:<20} ${price:>7.2f}")

    print_separator(30, ".")
    total = sum(price for _, price in expenses)
    print(f"{'Total':<20} ${total:>7.2f}")


def show_reminder() -> None:
    """Display a reminder that stays readable across multiple lines."""
    print_separator(40, "-")
    print_box("Meal prep reminder\nLabel containers with the date.\nUse refrigerated meals within 3 days.")


def main() -> None:
    show_shopping_plan()
    show_expense_summary()
    show_reminder()


if __name__ == "__main__":
    main()
