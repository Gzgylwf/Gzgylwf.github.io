# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import json
import typer

def readResume(fn):
    ret = yaml.safe_load(open(fn, 'rb'))
    return ret

def saveResume(resume, fn):
    yaml.safe_dump(resume, open(fn, 'w'))

def render(data: dict, template, outputFn):
    template = env.get_template(template)
    # print(data)
    # output = template.render(
    #     title = "Personal Page - {} {}".format(object['about']['lastName'], object['about']['firstName']),
    #     sessAbout = object['about'],
    #     sessExp = object['experience'],
    #     sessResearchExp = object['researchExperience'],
    #     sessEdu = object['education'],
    #     sessSkill = object['skills'],
    #     sessPublications = object['publications'],
    #     sessAwards = object['awards'],
    #     sessSummary = object['summary'],
    #     sessInterests = object['interests']
    # )
    ignore_fields = ['summary', 'interests', 'awards', 'publications']
    for field in ignore_fields:
        if field in data: data.pop(field)

    output = template.render(
        title = f"Personal Page - {data['about']['lastName']} {data['about']['firstName']}",
        about=data.pop('about'),
        skills=data.pop('skills'),
        resume=data
    )
    # Save to file
    with io.open(outputFn, "w") as f:
        f.write(output)
        f.close()

def make_resume(
        resume: str, 
        save: str=None, 
        template: str="resume.html", 
        theme: str="1d913c",
        date_cols: int=3,
    ):
    template_folder = os.path.join(os.getcwd(), "templates")
    assert os.path.exists(resume), f"{resume} does not exist"
    assert os.path.exists(template_folder), f"{template_folder} does not exist"
    # Load template
    env = Environment(loader=FileSystemLoader(template_folder))
    jinja_template = env.get_template(template)
    # Load data
    data: dict = None
    if resume.endswith(".yaml"): data = readResume(resume)
    elif resume.endswith(".json"): data = json.load(io.open(resume, 'r'))
    else: raise ValueError(f"Unsupported file type: {resume}")
    # Pop ignore fields
    ignore_fields = ['summary', 'interests', 'awards', 'publications']
    for field in ignore_fields:
        if field in data: data.pop(field)
    # Render
    title = f"{data['about']['lastName']} {data['about']['firstName']}-Resume"
    output = jinja_template.render(
        title = title,
        about=data.pop('about'),
        skills=data.pop('skills'),
        resume=data,
        theme=theme,
        date_cols=date_cols
    )
    # Save to file
    if save is None:
        filename = f"{title}.html"
        save = os.path.join(os.path.dirname(resume), filename)
    with io.open(save, "w") as f:
        f.write(output)
        f.close()


if __name__ == "__main__":
    typer.run(make_resume)
    