class TestMyFirst:
    """
    """
    my_number = 10
    def test_number_is_valid(self):
        """
        :return:
        """
        assert TestMyFirst.my_number <= 10
        assert TestMyFirst.my_number > 0
    def test_number_is_int(self):
        """
        :return:
        """
        assert (TestMyFirst.my_number + 1) == 10, 'Oops test failed'