from arithmetic_arranger import arithmetic_arranger
import pytest


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "9999 + 9998"], True))


# Run unit tests automatically
pytest.main(['test_module.py', '--verbose'])
