# helloworld
It's a simple python package that prints hello world!



## PIP install

1. Test\prerelease
https://test.pypi.org/project/azhelloworldpackage/
`pip install -i https://test.pypi.org/simple/ azhelloworldpackage`

2. Production 
https://pypi.org/project/azhelloworldpackage/
`pip install azhelloworldpackage`


## Test locally from source code

`pip install .`

`python test.py`

## create local package

1. Make sure you have the latest versions of setuptools, wheel and twine installed:
`pip install --user --upgrade setuptools wheel`

2. `python setup.py sdist bdist_wheel`

3. under `dist` there will be one or many `*.whl` file you can install it locally
`pip install C:/some-dir/some-file.whl` or 
`pip install /dist/some-file.whl`


## Steps to upload your package to the Python Package Index under your account:


1. get user account https://test.pypi.org

2. get user account https://test.pypi.org

3. Make sure you have the latest versions of setuptools, wheel and twine installed:
`pip install --user --upgrade setuptools wheel`
`pip install --user --upgrade twine`

4. rename azhelloworldpackage, your package name can contains letters, numbers, _ , and -. It also must not already taken on pypi.org
you need to rename `name` in `setup.py` file and rename the folder structure
`

/yourpackagename
    __init__.py

`

4. `python setup.py sdist bdist_wheel`

5. upload it to test\prerelease environment `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

6. to test newly uploaded package `pip install -i https://test.pypi.org/simple/ yourpackagename`

7. upload it to production environment `twine upload dist/*`

8. to test your package `pip install yourpackagename`

Resource
https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
