import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='azhelloworldpackage',  
    version='0.1',
    author="Azadeh Khojandi",
    author_email="azadehkhojandi@gmail.com",
    description="hello world!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Azadehkhojandi/helloworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )