from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import io
import typer
import re
from jinja2 import Template

class CoverLetter:
    def __init__(self, resume, jd):
        self.resume = resume
        self.jd = jd
        env = Environment(loader=FileSystemLoader("templates"))
        # Load template
        self.prompt_template = env.get_template("cl_prompt.txt")
        self.cover_letter_template = env.get_template("cover_letter.html")

    def make(self, output_file: str = None, **kwargs):
        cl_prompt = self.prompt_template.render(resume=self.resume, jd=self.jd, **kwargs)
        # Save to file
        if output_file is not None:
            with io.open(output_file, "w") as f:
                f.write(cl_prompt)
                f.close()
        return cl_prompt
    
    def render(self, letter_body_fn: str, output_file: str = None):
        # Read the content from body fn
        with io.open(letter_body_fn, "r") as f:
            letter_body = f.read()
            f.close()
        paragraphs = re.split(r"\n{2,}", letter_body)
        cover_letter = self.cover_letter_template.render(resume=self.resume, jd=self.jd, content=paragraphs)
        # Save to file
        if output_file is not None:
            with io.open(output_file, "w") as f:
                f.write(cover_letter)
                f.close()
        return cover_letter



def make_cover_letter(
        resume_fn: str, 
        job_fn: str,
        save_fn: str=None
    ) -> CoverLetter:
    assert os.path.exists(resume_fn), f"{resume_fn} does not exist"
    assert os.path.exists(job_fn), f"{job_fn} does not exist"
    resume = yaml.safe_load(io.open(resume_fn, 'rb'))
    jd = yaml.safe_load(io.open(job_fn, 'rb'))
    cl = CoverLetter(resume, jd)
    # Generate a unique filename
    jb_name = os.path.splitext(os.path.basename(job_fn))[0]
    filename = f"Coverletter_{resume['about']['lastName']}_{resume['about']['firstName']}_{jb_name}"

    # Check if the prompt output file already exists
    prompt_output_fn = os.path.join(os.path.dirname(job_fn), f"{filename}.prompt.output.txt")
    if os.path.exists(prompt_output_fn):        # It already exists, the task is render the cover letter
        cl_page = os.path.join(os.path.dirname(job_fn), f"{filename}.html")
        print(f"{prompt_output_fn} found, will generate the cover letter {cl_page}")
        cl.render(letter_body_fn=prompt_output_fn, output_file=cl_page)
    else:
        cl_prompt_fn = os.path.join(os.path.dirname(job_fn), f"{filename}.prompt.txt")
        print(f"{prompt_output_fn} not found, will generate the prompt {cl_prompt_fn}, please send to LLM to generate.")
        cl.make(output_file=cl_prompt_fn)
    return cl

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
    typer.run(make_cover_letter)
    