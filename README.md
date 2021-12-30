# Personal Page & Resume Editor

The repo is used for update the personal page and resume.

## 1. __Write the YAML__

For the personal page, it will show all fields except `summary` session.

For the resume page, it will only show the those field w/o `hidden` attributes.

## 2. __Run the code__

```shell
source env/bin/activate
python update_site.py
```

## 3. __Open and print the resume__

Open the resume.html page and print out to replace the .pdf resume in the root directory. Then the personal page can download normally.