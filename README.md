# Parametrizing pytest with json

[pytest parameterization](https://docs.pytest.org/en/latest/parametrize.html) is a very powerful tool for python unit tests. 

Sometimes the standard decorator technique starts to get unwieldy:

```python

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("1+1", 2),
        ("2*6", 12),
        ("10-2", 8),
        ("100/10", 10),
        ("2+4", 6),
        ("6*9", 42),
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

By using json files for tests cases you can keep unit test *code* simple and small. Test code is almost as important at the 'actual' code, so it's critical to keep test code understandable. 

### Example:

This is an example of using a json file to parameterize pytest. 

It reads in the json file and creates parameters for each test case.

One important thing to note is the id function 

```python
def id_func(item: dict) -> str:
    """ Returns a unique id for each test, just make testing clear """
    return item["input"]
```

This will give each test an id so it's easy to see what failed with a `pytest` (in this case `jbr`)

```bash
$ pytest -v
==================================================================== test session starts =====================================================================
platform darwin -- Python 3.7.4, pytest-5.1.1, py-1.8.0, pluggy-0.12.0 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /example-pytest-json-input
plugins: dash-1.0.2, cov-2.7.1, requests-mock-1.6.0
collected 3 items                                                                                                                                            

test_json_input.py::test_greeter[John] PASSED                                                                                                          [ 33%]
test_json_input.py::test_greeter[jbr] FAILED                                                                                                           [ 66%]
test_json_input.py::test_greeter[Zachariah] PASSED                                                                                                     [100%]

========================================================================== FAILURES ==========================================================================
_____________________________________________________________________ test_greeter[jbr] ______________________________________________________________________

test_case = {'input': 'jbr', 'output': 'Hi jbr!'}

    def test_greeter(test_case):
        """ Do we introduce customers correctly? """
>       assert greeter(test_case["input"]) == test_case["output"]
E       AssertionError: assert 'Howdy jbr!' == 'Hi jbr!'
E         - Howdy jbr!
E         + Hi jbr!

test_json_input.py:27: AssertionError
================================================================ 1 failed, 2 passed in 0.38s =================================================================
```

This simple example uses json, but it's easy to adapt this to other test case formats. 
