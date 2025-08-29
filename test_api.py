import os
from fastapi.testclient import TestClient

# Set deterministic identity for tests
os.environ["FULL_NAME_LOWER"] = "john_doe"
os.environ["DOB_DDMMYYYY"] = "17091999"
os.environ["EMAIL"] = "john@xyz.com"
os.environ["ROLL_NUMBER"] = "ABCD123"

from app.main import app  # noqa: E402

client = TestClient(app)

def post(data):
    return client.post("/bfhl", json={"data": data})

def test_example_a():
    resp = post(["a","1","334","4","R","$"])
    assert resp.status_code == 200
    j = resp.json()
    assert j["is_success"] is True
    assert j["odd_numbers"] == ["1"]
    assert j["even_numbers"] == ["334","4"]
    assert j["alphabets"] == ["A","R"]
    assert j["special_characters"] == ["$"]
    assert j["sum"] == "339"
    assert j["concat_string"] == "Ra"

def test_example_b():
    resp = post(["2","a","y","4","&","-","*","5","92","b"])
    assert resp.status_code == 200
    j = resp.json()
    assert j["is_success"] is True
    assert j["odd_numbers"] == ["5"]
    assert j["even_numbers"] == ["2","4","92"]
    assert j["alphabets"] == ["A","Y","B"]
    assert j["special_characters"] == ["&","-","*"]
    assert j["sum"] == "103"
    assert j["concat_string"] == "ByA"

def test_example_c():
    resp = post(["A","ABcD","DOE"])
    assert resp.status_code == 200
    j = resp.json()
    assert j["is_success"] is True
    assert j["odd_numbers"] == []
    assert j["even_numbers"] == []
    assert j["alphabets"] == ["A","ABCD","DOE"]
    assert j["special_characters"] == []
    assert j["sum"] == "0"
    assert j["concat_string"] == "EoDdCbAa"

def test_mixed_token_letters_included_in_concat():
    resp = post(["ab12cd","3","x!y"])
    j = resp.json()
    # numbers
    assert j["odd_numbers"] == ["3"]
    assert j["even_numbers"] == []
    # alphabets array only contains alpha-only tokens uppercased (none here)
    assert j["alphabets"] == []
    # specials keep original tokens that are not purely alpha or numeric
    assert j["special_characters"] == ["ab12cd","x!y"]
    # letters for concat: a b c d x y -> reversed y x d c b a -> alt caps: YxDcBa
    assert j["concat_string"] == "YxDcBa"
    assert j["sum"] == "3"
