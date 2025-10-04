from pydantic import BaseModel
from LLM.LLMResponseParameter import  LLMResponseParameter

class LLMResponse(BaseModel):
    toolName: str
    toolParameters: list[LLMResponseParameter]

