from pydantic import BaseModel, Field

class DengueFeatures(BaseModel):
    id_municip:int
    febre:int
    mialgia:int
    cefaleia:int
    # exantema:int
    vomito:int