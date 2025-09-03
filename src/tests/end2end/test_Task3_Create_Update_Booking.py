# Task3--->Create Booking -> Update Booking (Patch)
import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


# Update booking -Patch request-Firstname and lastname updated

class Test_create_Update_Booking(object):
    def test_create_update_booking(self, create_token, create_booking_id):
        token = create_token
        booking_id = create_booking_id
        update_url = APIConstants.patch_put_delete(booking_id)
        response = patch_request(
            url=update_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            payload=payload_update_booking_patch(),
            in_json=False
        )
        verify_HTTP_status_code(response_data=response,expected_status_code=200)
        verify_response_key(key=response.json()["firstname"],expected_key="James")
        verify_response_key(key=response.json()["lastname"],expected_key="Brown")
        print("Results for create update ")
        print(response.json())