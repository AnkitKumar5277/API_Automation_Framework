# Verify that Create Booking, Create Token -> Update -> Delete -> It is not visible

import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request, delete_request, put_request
from src.helpers.common_verification import verify_HTTP_status_code, verify_response_key, verify_response_delete
from src.helpers.payload_manager import payload_update_booking
from src.utils.utils import Utils


class TestE2E(object):
    @allure.title("E2E-Verify Create Booking--->Update--->Delete")
    @allure.description(
        "Verify that created booking id when we update we are able to update it and delete it also | Full CRUD")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2ETC1")
    def test_update_booking_with_id_token(self, create_token, create_booking_id):
        booking_id = create_booking_id
        token = create_token
        put_url = APIConstants.patch_put_delete(booking_id=booking_id)
        print(put_url)
        response = put_request(
            url=put_url,
            headers=Utils().put_patch_delete_cookie(token=token),
            auth=None,
            payload=payload_update_booking(),
            in_json=False
        )
        print("Update headers")
        print(Utils().put_patch_delete_cookie(token=token))
        print(put_url)

        verify_HTTP_status_code(response_data=response, expected_status_code=200)
        verify_response_key(key=response.json()["firstname"], expected_key="Joy")
        verify_response_key(key=response.json()["lastname"], expected_key="Brown")

    @allure.title("E2E-Verify Delete Booking")
    @allure.description("Verify if the booking gets deleted given the booking id and token ")
    def test_delete_booking_with_id_token(self, create_token, create_booking_id):
        booking_id = create_booking_id
        token = create_token
        # print("For delete---",create_token, create_booking_id)
        delete_url = APIConstants.patch_put_delete(booking_id=booking_id)
        print(" delete url---", booking_id, token, delete_url)
        response = delete_request(
            url=delete_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            in_json=False
        )
        print("Delete headers")
        print(delete_url)
        print(Utils().put_patch_delete_cookie(token=token))
        print(response.status_code)
        verify_HTTP_status_code(response_data=response, expected_status_code=201)
        verify_response_delete(response=response.text)
