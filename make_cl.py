# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io
import os
import yaml
import argparse
import pathlib


def renderCL(info, body, template):
    template = env.get_template(template)
    output = template.render(
        title = "Cover Letter - {} to {}".format(info['name'], info['company']),
        info = info,
        body=body
    )
    # Save to file
    with io.open('{}_Coverletter.html'.format(info['company']), "w") as f:
        f.write(output)
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('coverletter', type=str, help='Cover letter file')
    args = parser.parse_args()

    assert os.path.exists(args.coverletter), "{} not existed!".format(args.resume)
    # Read files
    info, body = {}, []
    for line in io.open(args.coverletter, 'r', encoding='utf8').readlines():
        line = line.strip()
        if line.startswith("#") or line == '': continue
        elif ':' in line:
            chunks = line.split(":")
            info[chunks[0].strip()] = chunks[1].strip()
        else:
            body.append(line)
    
    env = Environment(loader=FileSystemLoader("templates"))
    renderCL(info, body, "coverletter.html")
    print("Update finish!")
    