# Try to update with invalid PUT
import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import put_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


# Here in this update request we are sending PUT request with a blank payload so that it is invalid.Gives 400 error
class Test_update_Invalid_PUT_request(object):
    def test_update_invalid_put_request(self, create_token, create_booking_id):
        token = create_token
        booking_id = create_booking_id
        update_url = APIConstants.patch_put_delete(booking_id=booking_id)
        response = put_request(
            url=update_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            payload={},
            in_json=False

        )
        verify_HTTP_status_code(response_data=response, expected_status_code=400)
        verify_bad_request_error(response.text)
