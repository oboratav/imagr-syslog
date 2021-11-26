import falcon
from falcon import testing

import pytest

from imagr_syslog.server import application

# TODO: Add tests for invalid data
# TODO: Test actual log output

@pytest.fixture
def client():
    return testing.TestClient(application)

def test_post_valid_log(client):
    response = client.simulate_post('/', body='{"message": "Test message", "hostname": "test-device", "status": "testing", "serial": "TESTSERIAL"}')
    assert response.status == falcon.HTTP_OK