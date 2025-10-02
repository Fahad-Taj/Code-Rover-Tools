import json
from typing import Callable

from Abstraction.ToolParameter import ToolParameter
from Abstraction.ToolResult import ToolResult
from Exceptions.InvalidParameterException import InvalidParameterException

class Tool:
    """
    Wrapper class over an actual Python function.
    This class provides all the necessary information about a tool (function) such as
    its name, description, the parameters required for the actual function and their types.
    Holds reference to the actual function.
    Checks if input parameters to function are valid.
    Function will take only key worded arguments. Check actual function for parameters required.
    """
    def __init__(self, name: str, description: str, parameters: list[ToolParameter], func: Callable):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.func = func

    def validate_input(self, **kwargs):
        """
        Checks if input key worded arguments are valid or not.
        Checks name of arguments as well as type of values.
        """
        for param in self.parameters:
            if param.name in kwargs.keys():
                argVal = kwargs[param.name] # This is actual value
                descrType = param.type # This is string
                if ToolParameter.validate_parameter(argVal, descrType):
                    continue
                else:
                    raise InvalidParameterException(f"Invalid parameter type for parameter: {param.name}")
            else:
                raise InvalidParameterException(f"Parameter {param.name} not given")
        return True

    def toJson(self):
        """
        Converts description of tool into JSON format
        """
        params_dict_list = []
        for param in self.parameters:
            params_dict_list.append(param.toDict())

        json_string = json.dumps(params_dict_list)
        tool_dict = {
            "name": self.name,
            "description": self.description,
            "parameters": json_string
        }
        return tool_dict

    def execute(self, **kwargs) -> ToolResult:
        """
        Executes the actual tool function. Provides required arguments.
        Handles errors. Output is an object of type Tool Result.
        """
        try:
            self.validate_input(**kwargs)
            result = self.func(**kwargs)
            return ToolResult(status=True, message="File read successfully", content=str(result), error=None)
        except InvalidParameterException as e:
            return ToolResult(status=False, message="Invalid parameters provided", content=None, error=f"{str(e)}")
        except Exception as e:
            return ToolResult(status=False, message="An error occurred", content=None, error=f"{str(e)}")





