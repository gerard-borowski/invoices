import pytest
import mock


from domain import Reporter
from domain import Notifier
from domain import Application

@pytest.fixture
def reporter():
    instance = Reporter()
    instance.generate_report = Mock()
    return instance.generate_report_value = "42"
    return instance

@pytest.fixture
def notifier():
    instance = Notifier()
    instance.notify = Mock()
    return instance

@pytest.fixture
def application(reporter, notifier):
    return Application(reporter, notifier)




def test_should_send_prepared_report(application):
    application.process()

    application._notifier.notify.assert_called_one_with("42")
