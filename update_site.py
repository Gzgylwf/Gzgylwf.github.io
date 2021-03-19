# Read data and generate the personal static pages, CV and namecard
from brokers import *
from jinja2 import Environment, FileSystemLoader
import io


if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template('index.html')
    output = template.render(
        title = "Personal Page - LI Wenfeng"
    )

    # Save to file
    with io.open('index.html', "w") as f:
        f.write(output)
        f.close()
    print("Update finish!")