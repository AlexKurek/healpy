def pytest_configure(config):
    config.option.astropy_header = True
    try:
        from pytest_astropy_header.display import PYTEST_HEADER_MODULES
        PYTEST_HEADER_MODULES.pop('Pandas')
        PYTEST_HEADER_MODULES.pop('h5py')
        PYTEST_HEADER_MODULES['astropy'] = 'astropy'
        PYTEST_HEADER_MODULES['cython'] = 'cython'
    except ImportError:
        pass
