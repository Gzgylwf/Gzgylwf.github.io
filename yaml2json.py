import yaml
import json

if __name__ == "__main__":
    # Load yaml data file
    fn = "data/resume.yaml"
    ret = yaml.safe_load(open(fn, 'rb'))
    json.dump(ret, open("data/resume.json", 'w'), indent=2)