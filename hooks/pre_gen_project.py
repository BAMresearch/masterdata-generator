#!/usr/bin/env python

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")

project_name = "{{cookiecutter.project_name}}"
PROJECT_REGEX = r"masterdata-[a-z0-9]*"
if not re.match(PROJECT_REGEX, project_name):
    logger.warning(
        f"{project_name} is not starting with the string `masterdata-`. "
        "We will continue generating the project, but please make sure to follow the naming convention."
    )


module_name = "{{cookiecutter.module_name}}"
MODULE_REGEX = r"^[a-z][_a-z0-9]+$"
if not re.match(MODULE_REGEX, module_name):
    link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
    logger.error(f"Module name should be pep-8 compliant. More info: {link}")
    sys.exit(1)