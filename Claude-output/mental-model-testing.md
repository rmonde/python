# Python Testing — Mental Models & Cheat Sheet
*Read before any interview or before writing tests.*

---

## The One-Line Mental Model

Testing answers one question: **"Does my code do what I think it does — and will I know immediately when it stops?"**

The three A's every test follows:
```
Arrange → Act → Assert
Set up inputs → call the thing → verify the result
```

---

## pytest Discovery Rules

pytest scans for tests automatically — no registration required:

| What | Rule |
|---|---|
| Files | Must be named `test_*.py` or `*_test.py` |
| Functions | Must start with `test_` |
| Classes | Must start with `Test` (no `__init__`) |

Plain `assert` works — pytest catches the `AssertionError` and reports it. No `self.assertEqual()` needed.

---

## Pattern 1 — Basic assert

```python
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
```

**Downside:** If first `assert` fails, the rest don't run — you don't see all failures at once. Use parametrize for multiple inputs.

---

## Pattern 2 — `@pytest.mark.parametrize`

```python
@pytest.mark.parametrize("input,expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_to_fahrenheit(input, expected):
    assert celsius_to_fahrenheit(input) == expected
```

Each tuple → separate test case: `test_celsius_to_fahrenheit[0-32]`, `test_celsius_to_fahrenheit[100-212]`

**Why:** If one input fails, all others still run. You see the full picture of what's broken.

**When to use:** Any function with multiple distinct input/output scenarios.

---

## Pattern 3 — `@pytest.fixture`

```python
@pytest.fixture
def k8s_pod_names():
    return {"valid": ["my-app", "pod-123"], "invalid": ["MyApp", "a" * 64]}

def test_valid_pods(k8s_pod_names):   # pytest injects by parameter name
    for name in k8s_pod_names["valid"]:
        assert is_valid_pod_name(name)
```

**Fixture vs global variable:**
- Global: created once, mutations bleed between tests, no cleanup
- Fixture: fresh per test by default, supports teardown via `yield`

**Fixture with teardown:**
```python
@pytest.fixture
def temp_file():
    path = "/tmp/test.txt"
    open(path, "w").write("data")
    yield path           # test runs here
    os.remove(path)      # cleanup runs after test, even on failure
```

**When to use:** Shared setup (DB connections, temp files, test objects), especially when cleanup is needed.

---

## Pattern 4 — Mocking with `unittest.mock.patch`

```python
from unittest.mock import patch

def test_pod_is_expired():
    with patch("utils.get_current_time", return_value=10000):
        assert is_pod_expired(created_at=1000) == True  # 10000 - 1000 = 9000 > 3600
```

### Why mock?
1. **Isolation** — test YOUR logic, not whether Azure/AWS/GitHub is up
2. **Control** — make the dependency return exactly what you need
3. **Cost/speed** — don't hit real APIs (and pay for them) on every test run

### The patch location rule
**Patch where the name is USED, not where it's DEFINED.**

```python
# utils.py imports and calls requests.get
import requests
def fetch_data(url):
    return requests.get(url).json()
```

```python
# CORRECT — patch in the module that uses it
with patch("utils.requests.get", return_value=mock_response): ...

# WRONG — utils.py already imported requests; patching the original has no effect
with patch("requests.get", return_value=mock_response): ...
```

### Common mock patterns
```python
# Control return value
with patch("module.function", return_value="fake_data"): ...

# Control side effect (raise exception)
with patch("module.function", side_effect=ConnectionError("timeout")): ...

# Verify it was called
with patch("module.function") as mock_fn:
    call_my_code()
    mock_fn.assert_called_once_with("expected_arg")
```

---

## Pattern 5 — Coverage

```bash
pytest tests/ --cov=mymodule --cov-report=term-missing
```

Output:
```
Name         Stmts   Miss  Cover   Missing
------------------------------------------
utils.py        10      2    80%   10-11
```

**What "Missing: 10-11" means:** Lines 10-11 were never executed by any test.

**Why a line might be missed:**
- Code inside a mocked function (mock replaces it; body never runs)
- Error handling paths that tests don't trigger
- Dead code

**Coverage targets:**
- 80% = industry floor for production code
- 100% = not always the goal; executing every line without asserting is meaningless
- Mocked external paths are intentionally uncovered — that's fine

---

## Decision Tree — Which Testing Pattern?

```
What are you testing?
│
├── Pure logic (input → output, no external calls)
│   └── Basic assert + parametrize
│
├── Code that needs shared setup (objects, files, DB)
│   └── @pytest.fixture (with yield for cleanup)
│
└── Code that calls external dependencies (API, file system, time, DB)
    └── unittest.mock.patch
        ├── return_value — control what it returns
        ├── side_effect — make it raise an exception
        └── assert_called_* — verify it was called correctly
```

---

## Interview Answers to Memorise

**"What is pytest and how does test discovery work?"**
→ Python testing framework. Discovers files named `test_*.py` and functions named `test_*()`. No class inheritance required, plain `assert` works. Run with `pytest` or `pytest tests/ -v`.

**"What is parametrize and why use it instead of multiple asserts?"**
→ Runs one test function with multiple input/expected pairs, each as a separate test case. If one fails, others still run. Multiple asserts in one function stop at the first failure — you lose visibility into how many things are broken.

**"What is a fixture?"**
→ A function that provides shared test setup, injected into test functions by parameter name. Runs fresh per test (no state bleed). Supports teardown via `yield` — code after `yield` runs after the test completes, even on failure.

**"What is mocking and why do you need it?"**
→ Replacing an external dependency with a controlled fake. Use when your code calls APIs, databases, the file system, or the clock — things you don't want running in tests. Gives you isolation (test your logic, not the dependency), control (exact return values), and cost savings (no real API calls per test run).

**"Explain the 'patch where it's used' rule."**
→ When module A imports and calls `requests.get`, patch `"module_a.requests.get"` — not `"requests.get"`. Module A holds its own reference to requests; patching the original has no effect on module A's already-imported reference.

**"Is 100% coverage always the goal?"**
→ No. 100% means every line executed, not that your tests are good — you can execute every line and assert nothing. Mocked external paths are intentionally excluded. 80% is a reasonable production floor. The missing 20% is typically error handlers, mocked infrastructure, or defensive code for unreachable edge cases.

---

*Last updated: 2026-06-13 | Phase 4 complete | Next: Phase 5 Flask deeper*
