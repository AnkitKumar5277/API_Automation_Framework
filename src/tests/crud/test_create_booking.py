# create booking so that thsi can be reused
from http.client import responses

import allure
import pytest
import logging  # This is used to print the messages - Logs.This module is alreaddy installed by Python
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *  # import all verifications in this file
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.postive
    @allure.title("Verify that Creating Booking status and Booking ID should not be null")
    @allure.description("Create a booking from teh payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_postive(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting the testcase of TestCreateBooking")
        LOGGER.info("POST request started")
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        LOGGER.info("POST request Done")
        LOGGER.info("Now verifying")
        verify_HTTP_status_code(response_data=response,expected_status_code=200)
        LOGGER.info(str(response.json()))
        LOGGER.info(f'"Booking Id is --{response.json()["bookingid"]}')
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Verify the Creating Booking status with invalid payload")
    @allure.description(
        "Creating no Booking id and verify 500 for the incorrect payload")
    def test_create_booking_negative_tc1(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the negative testcase of TestCreateBooking ")
        LOGGER.info("POST request started")
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False

        )

        verify_HTTP_status_code(response_data=response,expected_status_code=500)
    @pytest.mark.negatve
    @allure.title("Verify the status for Create booking with invalid payload ")
    @allure.description("Create a booking with invalid payload and verify that the status code is 500 and no booking id is created")
    def test_create_booking_negative_tc2(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting the test case for POST with invalid payload")
        LOGGER.info("POST request started")
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={"name": "pramod"},
            in_json=False
        )
        verify_HTTP_status_code(response_data=response,expected_status_code=500)