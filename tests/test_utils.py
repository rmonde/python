import pytest
from utils import celsius_to_fahrenheit, is_pod_expired, is_valid_pod_name
from unittest.mock import patch

@pytest.mark.parametrize("input,expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_to_fahrenheit(input, expected):
    assert celsius_to_fahrenheit(input) == expected

@pytest.mark.parametrize("name,expected", [
    ("valid-pod-name", True),
    ("123", True),
    ("PODNAME", False),
    ("a" * 64, False),
])
def test_is_valid_pod_name(name, expected):
    assert is_valid_pod_name(name) == expected

@pytest.fixture
def k8s_pod_names():
    return {"valid": ["my-app", "pod-123"],
            "invalid": ["MyApp", "a" * 64, 
            "-starts-with-hyphen"]}

def test_valid_pod_names(k8s_pod_names):
    for name in k8s_pod_names["valid"]:
        assert is_valid_pod_name(name)

def test_invalid_pod_names(k8s_pod_names):
    for name in k8s_pod_names["invalid"]:
        assert not is_valid_pod_name(name)


    
def test_pod_is_expired():
    with patch("utils.get_current_time", return_value=10000):
        assert is_pod_expired(created_at=1000) == True

def test_pod_not_expired():
    with patch("utils.get_current_time", return_value=10000):
        assert is_pod_expired(created_at=9990) == False