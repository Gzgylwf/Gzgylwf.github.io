from setuptools import setup, find_packages

setup(
    name='relic',
    version='0.0.7',
    description='A personal assistant for my own usage',
    author='LI Wenfeng',
    author_email='liwenfeng20112012@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.35.0',
        'Jinja2>=3.1.4',
        'pydantic>=2.7.0',
        'typer>=0.12.3',
    ],
    python_requires='>=3.9'
)
