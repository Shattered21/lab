import pytest
from account import *

class Test:

    def setup_method(self):
        self.p1 = Account ('bob')

    def tear_down(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'bob'


    def test_deposit(self):

        assert self.p1.deposit(20.5) is True
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)


        assert self.p1.deposit(-100.0) is False
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)


        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)






    def test_withdraw(self):
        self.p1.deposit(20)
        assert self.p1.withdraw(20.5) is False
        assert self.p1.get_balance() == pytest.approx(20, abs=0.001)


        assert self.p1.withdraw(-100.0) is False
        assert self.p1.get_balance() == pytest.approx(20, abs=0.001)


        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(20, abs=0.001)

        assert self.p1.withdraw(19) is True
        assert self.p1.get_balance() == pytest.approx(1, abs=0.001)
