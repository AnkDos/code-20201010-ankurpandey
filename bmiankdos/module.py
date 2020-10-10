import ijson
import pandas as pd
import sys

from bmiankdos.exceptions import InvalidJSONFileInput, UnrealisticValues

class BMICalc:
    """Implementation of the BMI Calculator"""
    
    def __init__(self, filename):
        """"""
        self.filename = filename
        self.dataFrame_source = list()
        self.dataFrame = None
        self._bmi = None
        self._out = tuple()

    def define_logic_map(self):
        """Map to derive the Category And Risk from a given weight range"""
        self.logic_map = {
            "0,18.4" : {
                "Category": "Underweight",
                "Risk": "Malnutrition risk",
            },
            "18.5,24.9": {
                "Category": "Normal weight",
                "Risk": "Low risk"
            },
            "25,29.9":{
                "Category": "Overweight",
                "Risk": "Enhanced risk"
            },
            "30,34.9":{
                "Category": "Moderately obese",
                "Risk": "Medium risk"
            },
            "35,39.9":{
                "Category": "Severely obese",
                "Risk": "High risk"
            },
            "40,sys.maxsize":{
                "Category": "Very severely obese",
                "Risk": "Very high risk"
            }
        }
    
    def read_inputfile(self):
        """Reading the JSON Input File for the Calculation"""
        with open(self.filename,'rb') as files:
            try :
                for item in ijson.items(files, "item"):
                    self._bmi = round(BMICalc.calculate_bmi(item['WeightKg']\
                        ,item['HeightCm']/100),1)
                    bmi_map = {
                        'BMI': self._bmi,
                    }
                    bmi_map.update(self.logic_engine())
                    self.dataFrame_source.append(bmi_map)
            except ijson.common.IncompleteJSONError:
                raise InvalidJSONFileInput("Invalid Json File")

    
    @staticmethod
    def calculate_bmi(weight, height):
        """Method to calc BMI"""
        if weight > 0 and height > 0 :
            return weight/(height**2)
        raise UnrealisticValues("Please Input a realistic value")
    
    def logic_engine(self):
        """
        Method To Get the Category and Risk information
        from the calculated BMI with help of Logic Map
        """
        for key, value in self.logic_map.items():
            key = list(map(lambda x: float(x) if x!= 'sys.maxsize'\
                 else eval(x),key.split(",")))
            if key[0] <= self._bmi <= key[1]:
                return value 
    
    def gen_Pandasdataframe(self):
        """
        Generating Pandas Dataframe for deriving conclusions
        and data related calculations
        """
        self.dataFrame = pd.DataFrame(data=self.dataFrame_source)
    
    def output_conclusions(self):
        """Deriving some additional data"""
        additional_info = [
            "{counts} people lies in Overweight Category".format(
                counts=self.dataFrame['Category'].value_counts()['Overweight']
            ),
            "{counts} people are in Low risk ".format(
                counts=self.dataFrame['Category'].value_counts()['Normal weight']
            ),
            "Average BMI turns Out to Be {avg}".format(
                avg=round(self.dataFrame['BMI'].mean(),1)
            )
        ]
        self._out = (self.dataFrame.to_string(index=False),additional_info)
        
    def driver_method(self):
        """A method for all methods"""
        self.define_logic_map()
        self.read_inputfile()
        self.gen_Pandasdataframe()
        self.output_conclusions()


if __name__ == "__main__":
    obj = BMICalc('bmiankdos/input_data/input_data.json')
    obj.driver_method()
    print("Table : \n\n" , obj._out[0])
    print("\nSome Observations : \n")
    i = 1
    for observation in obj._out[1]:
        print(i," ",observation)
        i += 1