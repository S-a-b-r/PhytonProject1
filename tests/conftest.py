import pytest
import sys
sys.path[0] = 'd:\\Univer\\Alg\\PythonProject1'
from db.DB import DB

db = DB()

@pytest.hookimpl(tryfirst = True, hookwrapper = True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    db.insertTestResult(report.nodeid, report.outcome == 'passed')