if __name__ == '__main__':
    import pytest
    args = ['tests', '--html=report.html', '--split-by race']
    pytest.main(args)