import pytest
from data.data_classes import PunchData


class TestPunch():
    punch_for_test = PunchData()

    @pytest.mark.skip
    def test_empty_punch_record(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.check_empty_records_table(self.punch_for_test.future_date)
        assert time_page.is_empty_record_displayed() is True, "Empty records message not displayed"
        assert time_page.get_empty_record_msg() == "No attendance records to display", "Message incorrect"

    @pytest.mark.skip
    def test_create_punch_record(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.create_punch_record(self.punch_for_test)
        assert time_page.is_success_save_msg_displayed() is True, "Punch success save message not displayed"
        assert time_page.get_success_save_msg_txt() == "Successfully Saved", "Message incorrect"

    @pytest.mark.skip
    def test_punch_record_in_list(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.get_punch_data_from_records(self.punch_for_test)
        assert time_page.is_punch_found() is True, "Punch record not found"
        assert time_page.is_punch_displayed() is True, "Punch record not displayed"

