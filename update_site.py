# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import pdfkit


def readResume(fn):
    ret = yaml.safe_load(open(fn, 'r'))
    return ret

def saveResume(resume, fn):
    yaml.safe_dump(resume, open(fn, 'w'))

def render(object, template, outputFn):
    template = env.get_template(template)
    output = template.render(
        title = "Personal Page - {} {}".format(object['about']['lastName'], object['about']['firstName']),
        sessAbout = object['about'],
        sessExp = object['experience'],
        sessEdu = object['education'],
        sessSkill = object['skills'],
        sessAwards = object['awards'],
        sessSummary = object['summary']
    )
    # Save to file
    with io.open(outputFn, "w") as f:
        f.write(output)
        f.close()

if __name__ == "__main__":
    resume = readResume('data/resume.yaml')
    resumeCN = None
    if os.path.exists('data/resume_cn.yaml'): resumeCN = readResume('data/resume_cn.yaml')
    
    env = Environment(loader=FileSystemLoader("templates"))
    templatesFiles = ['index', 'resume']

    for templateFile in templatesFiles:
        render(resume, "{}.html".format(templateFile), "{}.html".format(templateFile))
        if resumeCN is not None:
            render(resumeCN, "{}.html".format(templateFile), "{}_cn.html".format(templateFile))
        '''
        template = env.get_template(templateFile)
        output = template.render(
            title = "Personal Page - LI Wenfeng",
            sessAbout = resume['about'],
            sessExp = resume['experience'],
            sessEdu = resume['education'],
            sessSkill = resume['skills'],
            sessAwards = resume['awards']
        )

        # Save to file
        with io.open(templateFile, "w") as f:
            f.write(output)
            f.close()
        '''

    # Save pdf
    '''
    options = {
        'page-size': 'A4',
        'margin-top': '0.0in',
        'margin-right': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': ""
    }
    pdfkit.from_file('resume.html', output_path='{}{}-resume.pdf'.format(resume['about']['lastName'], resume['about']['firstName']), options=options)
    '''
    print("Update finish!")
    