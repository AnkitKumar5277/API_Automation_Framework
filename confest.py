# Reason for creating this file: To reuse the Create Token and Create Booking.
import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False

    )
    verify_HTTP_status_code(response_data=response, expected_status_code=200)
    print("Payload---", payload_create_token())
    verify_json_key_not_none(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def create_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False
    )
    verify_HTTP_status_code(response_data=response, expected_status_code=200)
    booking_id = response.json()["bookingid"]
    verify_json_key_not_null(booking_id)
    print("Created")
    print(response.json())
    return booking_id


@pytest.fixture(scope="session")
def get_booking_id():
    get_url = APIConstants().url_create_booking()
    response = get_request(
        url=get_url,
        auth=None,
        in_json=False
    )
    verify_HTTP_status_code(response_data=response, expected_status_code=200)
    print(response.json())
    verify_json_key_not_null(key="bookingid")
    booking_id = response.json()[0]["bookingid"]
    print("Booking id---->", booking_id)
    return booking_id
