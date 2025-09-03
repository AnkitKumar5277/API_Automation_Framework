# Try to Update the Deleted Booking
import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import delete_request, put_request, post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *


class Test_update_deleted_booking(object):
    @allure.title("E2E-Verify if a deleted booking id can be updated")
    @allure.description("Verify that updating a deleted booking id gives 404 error-Delete operation testcase")
    def test_delete_Booking_id(self, create_token, create_booking_id):
        booking_id = create_booking_id
        token = create_token
        delete_url = APIConstants.patch_put_delete(booking_id)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            in_json=False
        )
        print(response.text)
        verify_HTTP_status_code(response_data=response, expected_status_code=201)
        verify_response_delete(response=response.text)


@allure.title("E2E-Verify if a deleted booking id can be updated")
@allure.description("Verify that updating a deleted booking id gives 404 error-Update operation testcase")
def test_update_deleted_booking_id(create_token, create_booking_id):
    token = create_token
    booking_id = create_booking_id
    update_url = APIConstants.patch_put_delete(booking_id=booking_id)
    response = put_request(
        url=update_url,
        auth=None,
        headers=Utils().put_patch_delete_cookie(token=token),
        payload=payload_update_booking(),
        in_json=False
    )
    print(response.text)
    verify_HTTP_status_code(response_data=response, expected_status_code=405)
    verify_response_update_delete(response=response.text)
