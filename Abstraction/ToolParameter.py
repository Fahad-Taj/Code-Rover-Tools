import json
from tokenize import Number


class ToolParameter:
    """
    Describes a tool parameter. Every tool parameter must provide its name
    description and data type.
    This will help us validate arguments to the actual function.
    """
    allowed_types = {
        "int": int,
        "Number": Number,
        "str": str,
        "list": list,
        "dict": dict
    }

    @classmethod
    def validate_parameter(cls, val, descrType):
        """
        Class method that takes 2 arguments val and descrType (Type of value in string format).
        Checks if type of val matches that of descrType
        """
        if isinstance(val, ToolParameter.allowed_types[descrType]):
            return True
        return False

    @classmethod
    def allowedTypes(cls):
        """
        Checks if a type of parameter is allowed or not. Uses class dict for this.
        """
        return [str(key) for key in ToolParameter.allowed_types.keys()]

    def __init__(self, paramName, paramType, paramDescription=""):
        if paramType not in self.allowed_types.keys():
            raise Exception("Invalid parameter type. Invoke the ToolParameter.getTypes() method to get allowed types")

        self.name = paramName
        self.type = paramType
        self.description = paramDescription

    def to_json(self):
        """
        Converts the tool parameter description into JSON format
        """
        param_dict = self.to_dict()
        json_string = json.dumps(param_dict)
        return json_string

    def to_dict(self):
        """
        Converts the tool parameter description into a Python dictionary
        """
        param_dict = self.__dict__
        return param_dict


def main():
    print(ToolParameter.allowedTypes())
    fileName = ToolParameter("fileName", "str", "Relative path of the file")
    print(fileName.to_json())

if __name__ == "__main__":
    main()
