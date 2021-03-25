# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import pandas as pd
import numpy as np
import yaml


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
        sessExp = resume['experience']
    )

    # Save to file
    with io.open('index_test.html', "w") as f:
        f.write(output)
        f.close()
    print("Update finish!")
    
    print(resume['experience'])
    