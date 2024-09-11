from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow - Gemini"
    produtos2 = "ZapFlow - chatGPT"
    produtos3 = "zapFlow - Lhama"


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum