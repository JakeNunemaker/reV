# -*- coding: utf-8 -*-
"""
The Renewable Energy Potential Model
"""
from __future__ import print_function, division, absolute_import
import os
from reV.version import __version__

__author__ = """Galen Maclaurin"""
__email__ = "galen.maclaruin@nrel.gov"

REVDIR = os.path.dirname(os.path.realpath(__file__))
TESTDATADIR = os.path.join(os.path.dirname(REVDIR), 'tests', 'data')
