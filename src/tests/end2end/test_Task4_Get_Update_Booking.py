# Get a Booking -> Delete it -> Verify

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import get_request, delete_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class Test_get_Delete_Booking(object):

    @allure.title("E2E-Verify Get and delete Booking--->")
    @allure.description("Verify that a existing booking id can be retrieved and deleted")
    def test_del_booking_id(self,get_booking_id,create_token):
        booking_id=get_booking_id
        token=create_token
        delete_url=APIConstants.patch_put_delete(booking_id=booking_id)
        response=delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            in_json=False

        )
        print(response.text)
        verify_HTTP_status_code(response_data=response, expected_status_code=201)
        verify_response_delete(response=response.text)