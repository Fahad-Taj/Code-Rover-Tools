from pydantic import BaseModel

class LLMResponseParameter(BaseModel):
    name: str
    type: str
    val: str