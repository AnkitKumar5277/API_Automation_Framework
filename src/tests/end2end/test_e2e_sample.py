#Verify that Create Booking, Create Token -> Update -> Delete -> It is not visible

import pytest
import allure
class TestE2E(object):
    @allure.title("E2E-Verify Create Booking--->Update--->Delete")
    @allure.description("Verify that created booking id when we update we are able to update it and delete it also | Full CRUD")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1",name="E2ETC1")
    def test_update_booking_with_id_token(self):
        pass

    @allure.title("E2E-Verify Delete Booking")
    @allure.description("Verify if teh booking gets deleted given the booking id and token ")
    def test_delete_booking_with_id_token(self):
        pass

