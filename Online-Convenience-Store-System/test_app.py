from app import app

def test_health():
    res = app.test_client().get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "OK"

def test_home():
    res = app.test_client().get("/")
    assert res.status_code == 200