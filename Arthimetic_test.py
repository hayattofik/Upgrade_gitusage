
from operations import ArthimeticClass
import pytest

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
    def test_multiply(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 2.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
    def test_divide(self ):
        # arrange
        x, y = 4.0, 2.0
        expected_output = 2.0
        # act
        actual_output = ArthimeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
    def test_subtract(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = -1.0
        # act
        actual_output = ArthimeticClass.subtract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
        