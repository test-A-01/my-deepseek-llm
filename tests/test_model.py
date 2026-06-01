"""Tests for model module"""

from src.model import DeepSeekModel

def test_model_init():
    model = DeepSeekModel()
    assert model.model_name == "deepseek-chat"

def test_generate():
    model = DeepSeekModel()
    result = model.generate("Hello")
    assert "Hello" in result
