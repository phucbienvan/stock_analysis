from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import TypeVar, Generic, Optional


T = TypeVar("T")

class ResponseSchemaBase(BaseModel):
    __abstract__ = True

    code: str = ''
    message: str = ''

    def custom_response(self, code: str, message: str):
        self.code = code
        self.message = message
        return self
    
class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True

    def custom_response(self, code: str, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
        return self
    
    def success_response(self, data: T):
        self.code = '000'
        self.message = 'success'
        self.data = data
        return self
