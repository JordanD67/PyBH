# Contributing to PyBH

We appreciate being notified of problems with the existing PyBH code. To do so, you should file an issue on the GitHub Issue Tracker. But before doing so, do not forget to check whether the issue is already being addressed or not using the GitHub search tool to look for key words in the project issue tracker.

However, the best way to contribute is to submit your code to improve the library with pull requests. Here are the steps to do so:

## 1. Fork the Repository

If you have not already done so, fork the project repository by clicking on the 'Fork' button near the top right of the main repository page. This creates a copy of the code under your GitHub user account.

## 2. Clone Your Fork

Clone **your fork** of the repo from your GitHub account to your local disk, and add the base repository as a remote:

```bash
git clone git@github.com:<your GitHub handle>/PyBH.git
cd PyBH
git remote add upstream git@github.com:PyBHealth/PyBH.git
```

## 3. Create a Feature Branch

Create a feature branch (e.g. `my-feature`) to hold your development changes:

```bash
git checkout -b my-feature
```

**Always use a feature branch**. It's good practice to never routinely work on the `main` branch of any repository.

## 4. Set Up Development Environment

Create an environment with all the requirements. We recommend using Anaconda:

```bash
conda env create -f environment.yaml
```

After that, activate the environment you've just created:

```bash
conda activate PyBH
```

Then install the package (in editable mode) and its development dependencies:

```bash
pip install --no-deps -e .
pip install -e ".[dev]"
pip install -e ".[test]"
pip install -e ".[doc]"
```

Set pre-commit hooks:

```bash
pre-commit install
```

## 5. Make Your Changes

Work on your changes locally in your feature branch. Add changed files using `git add` and then commit files:

```bash
git add modified_files
git commit -m "Summary of your changes"
```

After committing, sync with the base repository in case there have been any changes:

```bash
git fetch upstream
git rebase upstream/main
```

Then push the changes to your GitHub account:

```bash
git push -u origin my-feature
```

## 6. Submit a Pull Request

Finally, to submit a pull request, go to the GitHub web page of your fork of the PyBH repo. Click the 'Pull request' button to send your changes to the project's maintainers for review. This will send an email to the committers.
