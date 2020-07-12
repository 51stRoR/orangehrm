import pytest
from data.data_classes import LocationData


class TestLocation():
    location = LocationData()

    @pytest.mark.skip
    def test_add_location(self, email, password):
        admin_page = self.login_page.correct_login(email, password).to_admin_module()
        admin_page.create_location_record(self.location)
        assert admin_page.is_success_save_msg_displayed() is True, "Location success save message not displayed"
        assert admin_page.get_success_save_msg_txt() == "Successfully Saved", "Message incorrect"

    @pytest.mark.skip
    def test_find_location(self, email, password):
        admin_page = self.login_page.correct_login(email, password).to_admin_module()
        admin_page.find_location_record(self.location)
        assert admin_page.is_location_found() is True, "Location record not found"
        assert admin_page.is_location_found() is True, "Location record not displayed"

    # @pytest.mark.skip
    def test_remove_location(self, email, password):
        admin_page = self.login_page.correct_login(email, password).to_admin_module()
        admin_page.delete_location_record(self.location)
        assert admin_page.is_success_save_msg_displayed() is True, "Location success delete message not displayed"
        assert admin_page.get_success_save_msg_txt() == "Successfully Deleted", "Message incorrect"
