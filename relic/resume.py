from pydantic import BaseModel, Field
from typing import Optional
import io
import os
import json

class Profile(BaseModel):
    first_name: Optional[str] = Field(None, description="The first name of the soul")
    last_name: Optional[str] = Field(None, description="The last name of the soul")

class Resume(BaseModel):
    profile: Optional[Profile] = None

    def save(self, resume_folder: str):
        if not os.path.exists(resume_folder): os.makedirs(resume_folder)
        fn = os.path.join(resume_folder, "resume.json")
        with io.open(fn, "w") as f:
            json.dump(self.model_dump(), f)
            f.close()

    @staticmethod
    def load(resume_folder: str):
        with io.open(os.path.join(resume_folder, "resume.json"), "r") as f:
            return Resume.model_validate_json(f.read())