from typing import Any, List, Dict, Optional
import json

class ToolResult:
    """
    Defines the data format for output of a tool call.
    Contains 4 parameters: status, message, content and error
    """
    def __init__(self, status: bool, message: Any = None, content: Optional[Any] = None, error: Optional[str] = None):
        self.status = status
        self.message = message
        self.content = content
        self.error = error

    def to_json(self):
        """
        Converts object into JSON format
        """
        result_dict = self.__dict__
        json_string = json.dumps(result_dict)
        return json_string

def main():
    tResult = ToolResult(True, "Success", "Arbitrary content", None)
    print(tResult.to_json())

if __name__ == "__main__":
    main()