if __name__ == '__main__':
    import pytest
    args = ['tests', '--json-report', '--json-report-file=report.json']
    pytest.main(args)