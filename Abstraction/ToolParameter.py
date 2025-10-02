import json
from tokenize import Number


class ToolParameter:
    allowed_types = {
        "int": int,
        "Number": Number,
        "str": str,
        "list": list,
        "dict": dict
    }

    @classmethod
    def validate_parameter(cls, val, descrType):
        if isinstance(val, ToolParameter.allowed_types[descrType]):
            return True
        return False

    @classmethod
    def allowedTypes(cls):
        return [str(key) for key in ToolParameter.allowed_types.keys()]

    def __init__(self, paramName, paramType, paramDescription):
        if paramType not in self.allowed_types.keys():
            raise Exception("Invalid parameter type. Invoke the ToolParameter.getTypes() method to get allowed types")

        self.name = paramName
        self.type = paramType
        self.description = paramDescription

    def toJson(self):
        param_dict = self.toDict()
        json_string = json.dumps(param_dict)
        return json_string

    def toDict(self):
        param_dict = self.__dict__
        return param_dict


def main():
    print(ToolParameter.allowedTypes())
    fileName = ToolParameter("fileName", "str", "Relative path of the file")
    print(fileName.toJson())

if __name__ == "__main__":
    main()
