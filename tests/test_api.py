"""Tests for API module"""

from src.api import DeepSeekAPI

def test_api_init():
    api = DeepSeekAPI()
    assert api.model is not None

def test_query():
    api = DeepSeekAPI()
    result = api.query("Test question")
    assert result["status"] == "success"
    assert "Test question" in result["question"]
