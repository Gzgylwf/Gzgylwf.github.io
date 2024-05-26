# RELIC

The name is from my love game Cyberpunk 2077, it is can save the soul of people. Hope the tools can used to manage yourself data.
The repo is a tools as personal page assitants for my own usage, some tool are very personalized. It consists of 2 parts:

## RELIC web apps

It is built with [Streamlit.io](https://streamlit.io/). Follow the step to initial the env.

The project structure and explanation as below:

folder/file|description
:---|:---
relic.py|The main entry of the apps
index.html|The public github page. It a static page, can be updated by the tool.
souls/All the user profile stored.

### Env prepare

- Python 3.9

### Install (activate your env)

```bash
pip install -e ./relic
```

### Run

The following command will run the apps for selected user.

```bash
streamlit relic.py [soul_name]
```

## Static Github page [Optional]

Please refer to [Github pages](https://pages.github.com/) to set up your own public page. This tool only use to update and manage the content of `index.html`, you need to set your own repo to make the page can be visited.