# PyBH
An open-source library for Bayesian statistical modeling, designed for the health sector.

## Installation
There is no PyPI package yet; you’ll need to clone the repository:
```bash
git clone https://github.com/PyBHealth/PyBH.git
```

## Contributing
We appreciate being notified of problems with the existing PyBH code. To do so, you should filed an issue on the GitHub Issue Tracker. But before doing so, do not forget to check whether the issue is already being addressed or not using the GitHub search tool to look for key words in the project issue tracker.
However, the best way to contribute is to submit your code to improve the librairie with pull request. Here are the steps to do so :

1 - If you have not already done so, fork the project repository by clicking on the 'Fork' button near the top right of the main repository page. This creates a copy of the code under your GitHub user account.

2 - Clone **your fork** of the repo from you GitHUb account to you local disk, and add the base repository as a remote
```bash
git clone git@github.com:<your GitHub handle>/PyBH.git
cd PyBH
git remote add upstream git@github.com:PyBHealth/PyBH.git
```

3 - Create a feature branch (e.g. `my-feature`) to hold your development changes :
```bash
git checkout -b my-feature
```
**Always use a feature branch**. It's good practice to never routinely work on the `main` branch of any repository.

4 - Create an environment with all the requirements (to be determined). My recommendation would be to use Anaconda, and then from the Anaconda prompt :
```bash
conda env create -f environment.yaml
```
After that, since you'll want to contribute, you'll need to install other dependencies. First, activate the environment you've just created :
```bash
conda activate PyBH
```
Then install the package (in editable mode) and its development dependencies. The --no-deps flag is used to avoid installing the dependencies of PyBH as they are already installed when installing the development dependencies. This can end up interfering with the conda-only install of pymc.
```bash
pip install --no-deps -e .
```
Install development dependencies
```bash
pip install -e ".[dev]"
pip install -e ".[test]"
pip install -e ".[doc]"
```
Set pre-commit hooks :
```bash
pre-commit install
```

5 - You can then work on you changes locally, in your feature branch. add changed files using `git add` and then `git commit` files :
```bash
git add modified_files
git commit -m "Summary of your changes"
```
To record your changes locally. After committing, it is a good idea to sync with the base repository in case there have been any changes:
```bash
git fetch upstream
git rebase upstream/main
```
Then push the changes to your GitHub account with:
```bash
git push -u origin my-feature
```

6 - Finally, to submit a pull request, go to the GitHub web page of your fork of the PyBH repo. Click the 'Pull request' button to send your changes to the project's maintainers for review. This will send an email to the committers.
