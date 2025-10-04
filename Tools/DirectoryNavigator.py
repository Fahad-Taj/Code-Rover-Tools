from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Functions.NavigateDirectoryStructure import navigate_directory_structure

directoryNavigator = Tool(
    name="Directory Navigator",
    description="Gets the directory and file structure of the entire project. Excludes folders such as pycache, node_modules etc",
    parameters=[
        ToolParameter(
            paramName="path",
            paramType="str",
            paramDescription="Path of the base directory in raw format."
        )
    ],
    func=navigate_directory_structure
)

def main():
    try:
        print(directoryNavigator.execute(path=r"C:\Users\fahad\OneDrive\Documents\CodeRover").to_json())
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()