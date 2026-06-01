"""API Interface for DeepSeek LLM"""

from .model import DeepSeekModel

class DeepSeekAPI:
    """API wrapper for DeepSeek LLM"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.model = DeepSeekModel()
    
    def query(self, question: str) -> dict:
        """Query the model with a question"""
        response = self.model.generate(question)
        return {
            "status": "success",
            "question": question,
            "answer": response
        }
    
    def batch_query(self, questions: list) -> list:
        """Batch query multiple questions"""
        return [self.query(q) for q in questions]
