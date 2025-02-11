# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

This project was generated with [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) using the [BAMResearch/masterdata-generator](https://github.com/BAMresearch/masterdata-generator) repository.

## Getting started

If you are using Python, you can install the package and its dependencies by creating a virtual environment (either with `conda` or `venv`) and running:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install uv
uv pip install -e '.[dev]'
```

> [!NOTE]
> Step 8 is defined using `venv` for creating a virtual environment in an Ubuntu OS. Please, modify the commands if you use `conda` or you are installing in Windows/MacOS.

## Development

Once you have the skeleton of the Masterdata repository, you can define new classes in the corresponding file under `src/{{cookiecutter.module_name}}/`.

In case of Python, these are different modules for Object Types, Property Types, and Vocabularies.

For Excel or RDF/XML, this is a single file named `masterdata.xlsx`/`masterdata.owl`, respectively.

You can export from Python to the other formats using the `bam-masterdata` CLI. You can also generate Python code from Excel or RDF/XML with the same CLI. Read more in the [`bam-masterdata` documentation](https://bamresearch.github.io/bam-masterdata/).

## Github actions

A set of Github actions are defined in `.github/workflows/`. These will:
1. Ensure typing and formatting consistency in Python code following PEP-8 standards using `mypy` and `ruff` rules defined in the `pyproject.toml`.
2. Check consistency of the Masterdata definitions using the `bam-masterdata` checker CLI functionalities.

If the pipeline passes, it means your Masterdata definitions are formatted properly and do not clash with the current `bam-masterdata` definitions.

> [!IMPORTANT]
> In `bam-masterdata`, there is a set of Masterdata entities already defined. These correspond to the **general definitions** (to be used across MSE sub-communities). If you want to know how to define new Masterdata entities using inheritance from the general ones, read the [corresponding documentation](https://bamresearch.github.io/bam-masterdata/).

## Publishing Masterdata as an independent PyPI package

The action `.github/workflows/publish.yml` already implements the publishing of your repository to PyPI. When you are ready, you need:
1. Define a secret and name it `PYPI_API_TOKEN` from [pypi.org](https://pypi.org/).
2. Create a **Release** from the Github page of your repository.

Read more here: [Github PyPI documentation](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).
