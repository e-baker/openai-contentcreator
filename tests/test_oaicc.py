# test_oaicc.py

import pytest
from openaicc import *

def test_openaicc():
    oaicc = OpenAICC()
    assert oaicc is not None