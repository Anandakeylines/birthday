from openai import OpenAI

# Minimal user message class
class UserMessage:
    def __init__(self, content: str):
        self.content = content

# LLM chat class
class LlmChat:
    def __init__(self, api_key: str, session_id: str = None, system_message: str = None):
        self.api_key = api_key
        self.session_id = session_id
        self.system_message = system_message
        self.history = []
        self.client = OpenAI(api_key=self.api_key)

    def send_message(self, msg: UserMessage):
        # Add user message to history
        self.history.append(msg.content)

        # Generate response using OpenAI
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.system_message},
                *[{"role": "user", "content": m} for m in self.history]
            ],
            max_tokens=200
        )

        # Return the content of the response
        return response.choices[0].message.content
