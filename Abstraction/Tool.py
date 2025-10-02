import json
from typing import Callable

from Abstraction.ToolParameter import ToolParameter
from Abstraction.ToolResult import ToolResult
from Exceptions.InvalidParameterException import InvalidParameterException

class Tool:
    def __init__(self, name: str, description: str, parameters: list[ToolParameter], func: Callable):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.func = func

    def validate_input(self, **kwargs):
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
        try:
            self.validate_input(**kwargs)
            result = self.executable(**kwargs)
            return ToolResult(status=True, message="File read successfully", content=str(result), error=None)
        except InvalidParameterException as e:
            return ToolResult(status=False, message="Invalid parameters provided", content=None, error=f"{str(e)}")
        except Exception as e:
            return ToolResult(status=False, message="An error occurred", content=None, error=f"{str(e)}")

    def executable(self, **kwargs):
        try:
            content = self.func(**kwargs)
            return content
        except Exception as e:
            raise Exception(str(e))





