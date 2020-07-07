import pytest
from data.data_classes import PunchData


class TestPunch():
    punch_for_test = PunchData()

    def test_empty_punch_record(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.check_empty_records_table(self.punch_for_test.future_date)
        assert time_page.is_empty_record_displayed() is True, "Empty records message not displayed"
        assert time_page.get_empty_record_msg() == "No attendance records to display", "Message incorrect"

    @pytest.mark.skip
    def test_create_punch_record(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.create_punch_record(self.punch_for_test.punch_in_msg, self.punch_for_test.punch_out_msg)
        assert time_page.is_success_punch_msg_displayed() is True, "Punch success save message not displayed"
        assert time_page.get_success_punch_msg() == "Successfully Saved", "Message incorrect"

    @pytest.mark.skip
    def test_check_last_punch_record(self, email, password):
        time_page = self.login_page.correct_login(email, password).to_time_module()
        time_page.check_punch_in_records_table(self.punch_for_test.today_date)
        assert time_page.get_last_record_punch_in_note() == self.punch_for_test.punch_in_msg
        assert time_page.get_last_record_punch_out_note() == self.punch_for_test.punch_out_msg

