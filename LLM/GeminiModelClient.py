import json
from google import genai
from google.genai import types
from LLM.LLMResponse import LLMResponse

with open(r"C:\Users\fahad\PycharmProjects\CodeRoverTools\prompt.txt", 'r') as f:
    systemPrompt = f.read()

class GeminiModelClient:
    def __init__(self, systemPrompt, modelId, apiKey, temp):
        self.systemPrompt = systemPrompt
        self.modelId = modelId
        self.apiKey = apiKey
        self.temp = temp
        self.client = genai.Client(api_key=self.apiKey)
        self.chat = self.client.chats.create(
            model=self.modelId,
            config=types.GenerateContentConfig(
                system_instruction=self.systemPrompt,
                temperature=self.temp,
                response_mime_type="application/json",
                response_schema=LLMResponse
            )
        )

    def send_message(self, message):
        response = self.chat.send_message(message)
        return response.text

def main():
    geminiClient = GeminiModelClient(systemPrompt, "gemini-2.5-flash", "AIzaSyAe5_bu6r1RHwNHORCN_51AkHQw_K7Lu5Q", 0.5)
    response = geminiClient.send_message("Create a small Python script to create a turn based chatting application. Keep it short and sweet")
    json_response = json.loads(response)
    print(response)
    print(json_response["toolName"])
    for param in json_response["toolParameters"]:
        print(param["name"])
        print(param["type"])
        print(param["val"])


if __name__ == "__main__":
    main()