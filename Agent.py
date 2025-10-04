import os
import json
from dotenv import load_dotenv

from Tools.FileWriter import fileWriter
from Tools.TextFileReader import textFileReader
from Tools.DirectoryCreator import directoryCreator
from Tools.DirectoryNavigator import directoryNavigator
from LLM.GeminiModelClient import GeminiModelClient, systemPrompt

load_dotenv()

class Agent:
    def __init__(self):
        self.tools = [fileWriter, textFileReader, directoryNavigator, directoryCreator]
        self.llm = GeminiModelClient(systemPrompt=systemPrompt, modelId="gemini-2.5-flash",apiKey=os.getenv("GEMINI_API_KEY"), temp=0.5)

    # Makes API call and returns response in string format
    def send_message(self, message):
        response = self.llm.send_message(message)
        return response.text

    # Get's string response, converts it into JSON and then parses it
    def parse_output(self, output):
        output = json.loads(output)
        if not output["toolName"] in [tool.name for tool in self.tools] + ["Quit"]:
            raise Exception("Tool not found")

        toolName = output["toolName"]
        params = {}
        for param in output["toolParameters"]:
            paramName = param["name"]
            paramType = param["type"]
            if paramType == "int":
                paramVal = int(param["val"])
            elif paramType == "Number":
                paramVal = float(param["val"])
            else:
                paramVal = str(param["val"])

            params[paramName] = paramVal

        return [toolName, params]

    def tool_call(self, fields):
        [toolName, params] = fields

        for tool in self.tools:
            if tool.name == toolName:
                response = tool.execute(**params)
                return response

        raise Exception("Error encountered while executing tool call")

    def run(self):
        while True:
            user_input = input("Enter query: ")
            tool_call_result = user_input
            flag = True
            while True:
                if flag:
                    raw_response = self.llm.send_message(user_input)
                    flag = False
                else:
                    raw_response = self.llm.send_message(tool_call_result.content)

                print(raw_response)
                parsed_response = self.parse_output(raw_response)
                # print(f"{type(parsed_response[0])} {type(parsed_response[1])}")
                print(f"{parsed_response[0]} {parsed_response[1]}")
                if parsed_response[0] == "Quit":
                    break
                tool_call_result = self.tool_call(parsed_response)
                print(f"{tool_call_result.to_json()}")


def main():
    os.environ["BASE_DIR"] = os.getcwd()
    agent = Agent()
    agent.run()

if __name__ == "__main__":
    main()