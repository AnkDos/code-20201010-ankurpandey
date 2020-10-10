import pytest

from bmiankdos.module import BMICalc
from bmiankdos.exceptions import InvalidJSONFileInput, UnrealisticValues

def pytest_generate_tests(metafunc):
    '''
      Using Parameterized , so collecting
      all the methods and params to be tested
    '''
    funcargl = metafunc.cls.params[metafunc.function.__name__]
    arg_name = sorted(funcargl[0]) 
    metafunc.parametrize(
        arg_name, [[funcargs[name] for name in arg_name] \
            for funcargs in funcargl]
    )

class TestClass:
    '''
       Test class to test different methods used in app
    '''
    params = {
        "test_valid_json_file":[{
            "file_url": "bmiankdos/tests/test_json_files/valid_json.json"
        }],
        "test_invalid_json_file":[{
            "file_url": "bmiankdos/tests/test_json_files/invalid_json.json"
        }],
        "test_valid_BMI_calc":[{
            "height" : 170,
            "weight" : 65,
            "result" : 22.5
        },{
            "height" : 180,
            "weight" : 85,
            "result" : 26.2
        }],
        "test_invalid_BMI_calc":[{
            "height" : -10,
            "weight" : 85
        }]
    }

    def test_valid_json_file(self, file_url):
        """Test to check wheter valid json files been loading properly"""
        obj = BMICalc(file_url)
        try :
            obj.define_logic_map()
            obj.read_inputfile()
        except Exception as exp:
            assert False
        else :
            assert True
    
    def test_invalid_json_file(self, file_url):
        """Test invalid json file raising error"""
        obj = BMICalc(file_url)
        with pytest.raises(InvalidJSONFileInput):
            obj.read_inputfile()
    
    def test_valid_BMI_calc(self, height, weight, result):
        """Test Valid BMI Calc"""
        assert round(BMICalc.calculate_bmi(weight,height/100),1) == result
    
    def test_invalid_BMI_calc(self, height, weight):
        """Test Invalid Value Raising Error"""
        with pytest.raises(UnrealisticValues):
            BMICalc.calculate_bmi(weight,height/100)
