import unittest
import jsonio
# import json_checker

class Test_jsonio(unittest.TestCase):
    _schema1 = {"number": int}
    _schema2 = {"number": int, "array":[str]}
    _schema3 = {"number": int, "nested":{"array":[bool], "name":str}}
    
    def test_getDataOK(self):
        exp = {"Name": "Slim"}
        data = jsonio.getData('test/resource_t1.json', jsonio.listeSchema)
        self.assertEquals(exp, data)
    
    # def test_getDataFail(self):
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm:
        #     data = jsonio.getData('data.json', self._schema1)
        
"""    
    def test_schema1Valid(self):
        data = {"number":1}
#        jsonio.validate(data, self._schema1)
    
    def test_schema1Invalid(self):
        # wrong data type
        data = {"number":"1"}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema1)
        # # additional data before
        data = {"foo": 0, "number":1}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema1)
        # additional data after
        data = {"number":1, "bar":"2"}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema1)
        
    def test_schema2Valid(self):
        data = {"number":1, "array": ["a", "b", "c"]}
        # jsonio.validate(data, self._schema2)
    
    def test_schema2InValid(self):
        # wrong type
        data = {"number":1, "array": "a, b, c"}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema2)        
        # wrong type in array
        data = {"number":1, "array": [1,2,3]}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema2)
        # additional data in betwee 
        data = {"number":1, "foo": "bar", "array": ["a", "b", "c"]}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema2)
    
    def test_schema3Valid(self):
        data = {"number":1, "nested": {"array": [True, False], "name": "Iko"}}
        # jsonio.validate(data, self._schema3)
    
    def test_schema3InValid(self):
        # wrong type
        data = {"number":1, "nested": 1}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
            # jsonio.validate(data, self._schema3)        
        # wrong type in nested object
        data = {"number":1, "nested": {"array": [0, 1], "name": "Iko"}}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema3)        
        # additional data nested object
        data = {"number":1, "nested": {"array": [True, False],"foo":"bar", "name":"Iko"}}
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm: 
        #     jsonio.validate(data, self._schema3)        
"""        

        
if __name__ == '__main__':
    unittest.main()