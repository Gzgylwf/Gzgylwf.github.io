# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import pandas as pd
import numpy as np
import yaml
import pdfkit


def readResume(fn):
    ret = yaml.load(open(fn, 'r'))
    return ret


if __name__ == "__main__":
    resume = readResume('data/resume.yaml')
    
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template('index.html')
    output = template.render(
        title = "Personal Page - LI Wenfeng",
        sessAbout = resume['about'],
        sessExp = resume['experience'],
        sessEdu = resume['education'],
        sessSkill = resume['skills'],
        sessAwards = resume['awards']
    )

    # Save to file
    targetFn = 'index_test.html'
    with io.open(targetFn, "w") as f:
        f.write(output)
        f.close()

    # Save pdf
    #pdfkit.from_string(output, output_path='{}{}-resume.pdf'.format(resume['about']['lastName'], resume['about']['firstName']))
    print("Update finish!")
    