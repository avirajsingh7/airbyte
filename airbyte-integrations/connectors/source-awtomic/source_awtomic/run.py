#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceAwtomic

def run():
    source = SourceAwtomic()
    launch(source, sys.argv[1:])
