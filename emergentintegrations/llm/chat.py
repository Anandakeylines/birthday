# A minimal example to get started

class UserMessage:
    def __init__(self, content: str):
        self.content = content

class LlmChat:
    def __init__(self):
        self.history = []

    def send_message(self, msg: UserMessage):
        self.history.append(msg.content)
        # Here you can add real LLM logic later
        return f"Echo: {msg.content}"
