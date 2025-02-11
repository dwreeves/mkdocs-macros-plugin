"""
Testing the project

(C) Laurent Franceschetti 2024
"""


import pytest

from test.fixture import DocProject

CURRENT_PROJECT = 'null'



def test_pages():
    PROJECT = DocProject(CURRENT_PROJECT)
    build_result = PROJECT.build(strict=False)
    # did not fail
    return_code = PROJECT.build_result.returncode
    assert not return_code, "Failed when it should not" 


    # ----------------
    # First page
    # ----------------


    page = PROJECT.get_page('index')
    ERROR_MSG = f"Is rendered!:\n{page.markdown}\n---SOURCE:\n{page.source_page.markdown}\n---"
    assert not page.is_rendered, ERROR_MSG
    assert not page.has_error
    


    # ----------------
    # Second page
    # ----------------
    # there is intentionally an error (`foo` does not exist)
    page = PROJECT.get_page('second')

    assert not page.is_rendered
    assert not page.has_error
    
def test_strict():
    "This project must fail"
    PROJECT = DocProject(CURRENT_PROJECT)

    # it must not fail with the --strict option,
    PROJECT.build(strict=True)
    assert not PROJECT.build_result.returncode, "Failed when it should not"



    