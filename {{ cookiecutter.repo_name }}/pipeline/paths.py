# -*- coding: utf-8 -*-
"""
Date: 6/2023
Version: 1.0
Author: (I) Jose Pena
Website: https://github.com/JoseJuan98


Paths
=====

...
"""
# Native libs
import os
from pathlib import Path

_ROOT_PATH = Path(__file__).parent.parent
_ARTIFACTS_PATH = os.path.join(_ROOT_PATH, 'artifacts')

DATA_PATH = os.path.join(_ARTIFACTS_PATH, 'data')
MODEL_PATH = os.path.join(_ARTIFACTS_PATH, 'models')

DATASET_PATH = os.path.join(DATA_PATH, 'raw', '.csv')  # TODO
PREPARED_DATA = os.path.join(DATA_PATH, 'processed', '_prepared.csv')  # TODO
DOWNLOAD_URI = "https://"  # TODO
