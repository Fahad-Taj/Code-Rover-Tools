from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Abstraction.ToolResult import ToolResult
from Exceptions.InvalidParameterException import InvalidParameterException
from Functions.ReadTextFile import read_text_file

class TextFileReader(Tool):
    def __init__(self, name: str, description: str, parameters: list[ToolParameter]):
        super().__init__(name, description, parameters)

    def execute(self, **kwargs) -> ToolResult:
        try:
            self.validate_input(**kwargs)
            content = read_text_file(**kwargs)
            return ToolResult(status=True, message="File read successfully", content=str(content), error=None)
        except InvalidParameterException as e:
            return ToolResult(status=False, message="Invalid parameters provided", content=None, error=f"{str(e)}")
        except Exception as e:
            return ToolResult(status=False, message="An error occurred", content=None, error=f"{str(e)}")

def main():
    textFileReader = TextFileReader("Text File Reader", "Tool used to read text files", [ToolParameter("filePath", "str", "Relative path of the file")])
    print(textFileReader.execute(filePath=r"C:\Users\fahad\OneDrive\Documents\changes in report.txt").content)
    print(textFileReader.toJson())
if __name__ == "__main__":
    main()