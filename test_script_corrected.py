"Tests del script"

# Import the functions to be tested from script.py
from script import add, subtract


# Function to test the add function
def test_add():
    """Test de la suma"""
    # Check if adding 3 and 2 equals 5
    assert add(3, 2) == 5  # Passes if the sum is correct


# Function to test the subtract function
def test_subtract():
    """Test de la resta"""
    # Check if subtracting 2 from 5 equals 3
    assert subtract(5, 2) == 3  # Passes if the result is correct
