from pydantic import BaseModel, Field
from typing import Optional
import os
import io
import json

class RELIC(BaseModel):
    root: str = Field(None, description="[*]The root directory of the RELIC project")
    first_name: Optional[str] = Field(None, description="The first name of the soul")
    last_name: Optional[str] = Field(None, description="The last name of the soul")

    def save(self):
        if not os.path.exists(self.root): os.makedirs(self.root)
        with io.open(os.path.join(self.root, "soul.json"), "w") as f:
            json.dump(self.model_dump(), f)
            f.close()

    @staticmethod
    def load(soul_folder: str):
        with io.open(os.path.join(soul_folder, "soul.json"), "r") as f:
            return RELIC.model_validate_json(f.read())