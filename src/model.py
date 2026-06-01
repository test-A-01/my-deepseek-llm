"""LLM Model Interface"""

class DeepSeekModel:
    """Simple DeepSeek LLM model wrapper"""
    
    def __init__(self, model_name: str = "deepseek-chat"):
        self.model_name = model_name
        self.temperature = 0.7
    
    def generate(self, prompt: str) -> str:
        """Generate response from prompt"""
        return f"Response to: {prompt}"
    
    def chat(self, messages: list) -> str:
        """Chat with conversation history"""
        return "Hello! How can I help you?"
