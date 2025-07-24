#!/usr/bin/env python

import logging
import os
import shutil
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

TMP_FILE_SOURCES = "file_sources"


def move_files(variant: str, save_path: str) -> None:
    if variant == "none" or save_path == "none":
        return None

    files = glob.glob(f"{TMP_FILE_SOURCES}/{variant}/*")

    for src_path_file in files:
        filename = os.path.basename(src_path_file)
        dst_path = os.path.join(save_path, filename)

        logger.info(f"Moving {src_path_file} to {dst_path}.")
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path_file, dst_path)


if __name__ == "__main__":
    root = os.getcwd()
    variants = [
        variant
        for variant, condition in [
            ("python", "{{cookiecutter.include_python_masterdata}}"),
            ("excel", "{{cookiecutter.include_excel_masterdata}}"),
        ]
        if condition != "False"
    ]
    module_name = "{{cookiecutter.module_name}}"
    src_path = os.path.join(root, "src", module_name)
    assert os.path.isdir(src_path), f"{src_path=} doesn't exist"
    
    # for each variant, move the python files to `src/module_name`
    for variant in variants:
        os.makedirs(src_path, exist_ok=True)
        move_files(variant=variant, save_path=src_path)
    
    # removing TMP_FILE_SOURCES
    logger.info(f"Remove temporary folder: {TMP_FILE_SOURCES}")
    shutil.rmtree(TMP_FILE_SOURCES)