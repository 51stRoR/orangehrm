from data.data_classes import LocationData


class TestLocation():
    location = LocationData()

    def test_add_location(self, email, password):
        admin_page = self.login_page.correct_login(email, password).to_admin_module()
        admin_page.create_location(self.location)
        assert admin_page.is_success_save_msg_displayed() is True, "Location success save message not displayed"
        assert admin_page.get_success_save_msg_txt() == "Successfully Saved", "Message incorrect"
