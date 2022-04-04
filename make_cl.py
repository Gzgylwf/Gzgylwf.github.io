# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import argparse


def render(object, template, outputFn):
    template = env.get_template(template)
    output = template.render(
        title = "Personal Page - {} {}".format(object['about']['lastName'], object['about']['firstName']),
        sessAbout = object['about'],
        sessExp = object['experience'],
        sessEdu = object['education'],
        sessSkill = object['skills'],
        sessAwards = object['awards'],
        sessSummary = object['summary'],
        sessInterests = object['interests']
    )
    # Save to file
    with io.open(outputFn, "w") as f:
        f.write(output)
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('string', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    headers = readResume('data/resume.yaml')
    resumeCN = None
    if os.path.exists('data/resume_cn.yaml'): resumeCN = readResume('data/resume_cn.yaml')
    
    env = Environment(loader=FileSystemLoader("templates"))
    templatesFiles = ['index', 'resume']

    for templateFile in templatesFiles:
        render(resume, "{}.html".format(templateFile), "{}.html".format(templateFile))
        if resumeCN is not None:
            render(resumeCN, "{}.html".format(templateFile), "{}_cn.html".format(templateFile))
    print("Update finish!")
    