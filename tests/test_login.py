class TestLogin():
    def test_correct_login(self, email, password):
        dashboard = self.login_page.correct_login(email, password)
        assert dashboard.get_page_title() == "OrangeHRM"
        assert "index.php/dashboard" in dashboard.get_page_url()
