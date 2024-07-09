from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import io
import typer

class CoverLetter:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

def make_cover_letter(
    resume_fn: str, 
    job_fn: str
    ) -> CoverLetter:
    assert os.path.exists(resume_fn), f"{resume_fn} does not exist"
    assert os.path.exists(job_fn), f"{job_fn} does not exist"
    resume = yaml.safe_load(io.open(resume_fn, 'rb'))
    jd = yaml.safe_load(io.open(job_fn, 'rb'))

    return None

def render_cover_letter(
        cover_letter_fn: str, 
        template_fn: str="cover_letter.html",
        save_fn: str=None,
    ):
    assert os.path.exists(cover_letter_fn), f"{cover_letter_fn} does not exist"
    conver_letter = yaml.safe_load(io.open(cover_letter_fn, 'rb'))
    template_folder = os.path.join(os.getcwd(), "templates")
    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template(template_fn)
    output = template.render(conver_letter)
    # Save to file
    if save_fn is not None:
        with io.open(save_fn, "w") as f:
            f.write(output)
            f.close()


if __name__ == "__main__":
    typer(make_cover_letter)
    