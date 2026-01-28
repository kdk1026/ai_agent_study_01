from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Adds a and b

    Args:
        a (int): first
        b (int): second

    Returns:
        int: first + second
    """
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b

    Args:
        a (int): first
        b (int): second

    Returns:
        int: a * b
    """
    return a * b

tools = [add, multiply]