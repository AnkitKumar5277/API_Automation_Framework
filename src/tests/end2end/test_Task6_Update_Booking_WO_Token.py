# Try to update without the token

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import patch_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class Test_update_WO_token(object):
    def test_update_wo_token(self, create_booking_id):
        booking_id = create_booking_id
        token = " "
        update_url = APIConstants.patch_put_delete(booking_id)
        response = patch_request(
            url=update_url,
            auth=None,
            headers=Utils().put_patch_delete_cookie(token=token),
            payload=payload_update_booking_patch(),
            in_json=False

        )
        print(update_url)
        print(Utils().put_patch_delete_cookie(token=token))
        verify_HTTP_status_code(response_data=response, expected_status_code=403)
        verify_response_update_WO_token(response=response.text)
