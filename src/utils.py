"""Utility functions"""

def format_prompt(question: str) -> str:
    """Format user question into prompt"""
    return f"User: {question}\nAssistant:"

def count_tokens(text: str) -> int:
    """Simple token counter"""
    return len(text.split())
