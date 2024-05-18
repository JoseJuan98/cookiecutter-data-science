# -*- coding: utf-8 -*-
"""
Date: 6/2023
Version: 1.0
Author: (I) Jose Pena
Website: https://github.com/JoseJuan98


Data Extraction
===============

...
"""
# Native libs
import os
import logging
from typing import Union
from pathlib import Path
from urllib.request import urlretrieve

# Data Analysis
import pandas

from pipeline.paths import DATASET_PATH, DOWNLOAD_URI

# Utils
logger = logging.getLogger('main')
logger.addHandler(logging.StreamHandler())


def fetch_data(
        url: Union[str, Path] = DOWNLOAD_URI,
        path: Union[str, Path] = DATASET_PATH,
        force_retrieve: bool = False
) -> pandas.DataFrame:
    """
    Method to extract the data from a URL and stores it in a file into the `path` or if the file already exists in
    the `path` skips the extraction. Finally, returns a dataframe reading this file. Args: url (str, Path): URL to
    the source to extract path (str, Path): location where to store the csv data force_retrieve(bool): if
    `force_retrieve=True` it retrieves data from URL, if `force_retrieve=True` it retrieves data only if file doesn't
    exist

    Returns:
        DataFrame: data extracted from path or URL
    """
    if not os.path.exists(path) or force_retrieve:
        dir_path = os.path.dirname(path)

        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        urlretrieve(url, path)

    return pandas.read_csv(filepath_or_buffer=path, low_memory=False)
