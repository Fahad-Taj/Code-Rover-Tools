from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Functions.CreateDirectory import create_directory

directoryCreator = Tool(
    name="Directory Creator",
    description="Creates a directory structure based on given input relative to project's root directory.. Intermediary directory will also be created if they don't exist",
    parameters=[
        ToolParameter(
            paramName="dirPath",
            paramType="str",
            paramDescription="Path of the directory relative to project's root directory in raw format."
        )
    ],
    func=create_directory
)

def main():
    try:
        print(directoryCreator.execute(dirPath=r"C:\Users\fahad\OneDrive\Documents\CodeRover\CodeRover-An-Agent-by-AI-beats-with-Educasheer\temp\temp2").to_json())
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()