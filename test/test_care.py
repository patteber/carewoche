import unittest
from care import Carewoche

class Test_Carewoche(unittest.TestCase):
    _schema1 = {"number": int}
    _schema2 = {"number": int, "array":[str]}
    _schema3 = {"number": int, "nested":{"array":[bool], "name":str}}
    
    file_t1 = 'test/resource_t1.json'
    t1_exp =    {
                    "Members": {
                        "Alice": { "ID": 1 },
                        "Bob": { "ID": 2 },
                        "Charlie": { "ID": 3 }
                    },  
                    "Order": [1, 2, 3]
                }

    def setUp(self) -> None:
        self.cut = Carewoche(self.file_t1)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_getDataOK(self):
        self.assertEqual(self.t1_exp, self.cut.getData())
        self.assertIsNotNone(self.cut.getMembers())
        self.assertIsNotNone(self.cut.getOrder())
        
    def test_accessMemberByNameOK(self):
        data = self.cut.getData()
        members = data["Members"]
        exp = ("Alice", "Bob", "Charlie")
        i = 0
        for m in members:
            self.assertEqual(m, exp[i])
            m_data = members[exp[i]]
            self.assertEqual(m_data, members[m])
            self.assertEqual(members[m]["ID"], (i+1))
            i=i+1

    def test_iterateOrderOK(self):
        self.assertEqual(self.cut.getOrder(), [1, 2, 3])
        self.cut.iterateOrder()
        self.assertEqual(self.cut.getOrder(), [2, 3, 1])
        
    def test_changeOrderAdd(self):
        self.cut.changeMembersOrder(2, 1)
        self.assertEqual(self.cut.getOrder(), [1, 3, 2])
    
    def test_changeOrderAddOverflow(self):
        self.cut.changeMembersOrder(2, 2)
        self.assertEqual(self.cut.getOrder(), [2, 1, 3])
        
    # def test_getDataFail(self):
        # with self.assertRaises(json_checker.core.exceptions.CheckerError) as cm:
        #     data = Carewoche.getData('data.json', self._schema1)
        
        
if __name__ == '__main__':
    unittest.main()