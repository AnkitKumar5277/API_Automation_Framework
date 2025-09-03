# Create Booking -> Delete It -> Verify

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import delete_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class Test_create_Delete_Booking(object):
    @allure.title("E2E-Verify Create Booking--->Delete")
    @allure.description("Veify that a booking created can be deleted with the booking id given")
    def test_create_delete_booking(self, create_token, create_booking_id):
        token = create_token
        booking_id = create_booking_id
        delete_url = APIConstants.patch_put_delete(booking_id)
        response = delete_request(
            url=delete_url,
            headers=Utils().put_patch_delete_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_HTTP_status_code(response_data=response, expected_status_code=201)
        verify_response_delete(response=response.text)
