from pydantic import BaseModel


class Settings(BaseModel):
    value: str


global_variable = Settings(value="Universe")
