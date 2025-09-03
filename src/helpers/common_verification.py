# Common Verification

# HTTP status code
# Headers
# Data Verification
# JSON schema
# Verify HTTP status code
def verify_HTTP_status_code(response_data, expected_status_code):
    assert response_data.status_code == expected_status_code, "Failed  to get the status code match "


# Verify the key is as expected
def verify_response_key(key, expected_key):
    assert key == expected_key, "Falied to match the key"


# Verify if the key value  is not null
def verify_json_key_not_null(key):
    assert key != 0, "Failed.Key is null"


# Verify if the key value  is not None
def verify_json_key_not_none(key):
    assert key is not None, "Failed.Key is None"


# Verify if key value is greater than zero
def verify_json_key_gr_zero(key):
    assert key > 0, "Failed .Key is not gretaer than zero"


# Verify the response after deleting a booking id
def verify_response_delete(response):
    assert "Created" in response


# Verify the response while trying to update a deleted  booking id
def verify_response_update_delete(response):
    assert "Method Not Allowed" in response


# Verify the reponse while  updating  a booking id without entring the token
def verify_response_update_WO_token(response):
    assert "Forbidden" in response


# Verify the response text  while giving any invalid HTTP request  -Bad Request
def verify_bad_request_error(response):
    assert "Bad Request" in response
