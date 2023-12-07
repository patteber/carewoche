import os
import unittest
from app.care import Carewoche

class Test_Carewoche(unittest.TestCase):
    file_t1 = 'test/resource_t1.json'
    t1_exp =    {
                    "Members": {
                        "Alice": { "IsActive": True },
                        "Bob": { "IsActive": True },
                        "Charlie": { "IsActive": True },
                        "Doris": {"IsActive": False}
                    },  
                    "Order": ["Alice", "Bob", "Charlie"]
                }

    def setUp(self) -> None:
        self.cut = Carewoche(self.file_t1)
        return super().setUp()
    
    def tearDown(self) -> None:
        f = self.file_t1 + ".update"
        if os.path.exists(f):
            os.remove(f)
        return super().tearDown()
    
    def test_getDataOK(self):
        self.assertEqual(self.t1_exp, self.cut.getData())
        self.assertIsNotNone(self.cut.getMembers())
        self.assertIsNotNone(self.cut.getOrder())
        
    def test_createMemberOK(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.postMember("Eve", True)
        self.assertTrue("Eve" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie", "Eve"])
    
    def test_updateMemberOK(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.postMember("Doris", True)
        self.assertTrue("Doris" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie", "Doris"])
        
    def test_createMemberTwiceOK(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.postMember("Eve", True)
        self.assertTrue("Eve" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie", "Eve"])
        self.cut.postMember("Eve", True)
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie", "Eve"])
        
    def test_deleteMemberOK(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.deleteMember("Alice")
        self.assertFalse("Alice" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Bob", "Charlie"])
        self.assertTrue("Doris" in self.cut.getMembers())
        self.cut.deleteMember("Doris")
        self.assertFalse("Doris" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Bob", "Charlie"])
        # double delete has no effects
        self.cut.deleteMember("Doris")
        self.assertFalse("Doris" in self.cut.getMembers())
        self.assertEqual(self.cut.getOrder(), ["Bob", "Charlie"])
        
    def test_accessMemberByNameOK(self):
        members = self.cut.getMembers()
        exp_name = ("Alice", "Bob", "Charlie", "Doris")
        exp_active = (True, True, True, False)
        i = 0
        for m in members:
            self.assertEqual(m, exp_name[i])
            m_data = members[exp_name[i]]
            self.assertEqual(m_data, members[m])
            self.assertEqual(members[m]["IsActive"], exp_active[i])
            i += 1
            
    def test_deactivateMember(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.assertEqual(self.cut.getMembers()["Alice"]["IsActive"], True)
        self.cut.deactivateMeber("Alice")
        self.assertEqual(self.cut.getOrder(), ["Bob", "Charlie"])
        self.assertEqual(self.cut.getMembers()["Alice"]["IsActive"], False)
        
    def test_activateMember(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.assertEqual(self.cut.getMembers()["Doris"]["IsActive"], False)
        self.cut.activateMeber("Doris")
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie", "Doris"])
        self.assertEqual(self.cut.getMembers()["Doris"]["IsActive"], True)

    def test_iterateOrderOK(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.iterateOrder()
        self.assertEqual(self.cut.getOrder(), ["Bob", "Charlie", "Alice"])
        
    def test_iterateOrderOnOneMemberOK(self):
        o = self.cut.getOrder()
        o.pop(0)
        o.pop(0)
        self.assertEqual(self.cut.getOrder(), ["Charlie"])
        self.cut.iterateOrder()
        self.assertEqual(self.cut.getOrder(), ["Charlie"])
        
    def test_changeOrderPlus(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.changeMembersOrder("Bob", 1)
        self.assertEqual(self.cut.getOrder(), ["Alice", "Charlie", "Bob"])
    
    def test_changeOrderPlusOverflow(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.changeMembersOrder("Bob", 2)
        self.assertEqual(self.cut.getOrder(), ["Bob", "Alice", "Charlie"])
        
    def test_changeOrderMinus(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.changeMembersOrder("Bob", -1)
        self.assertEqual(self.cut.getOrder(), ["Bob", "Alice", "Charlie"])
        
    def test_changeOrderMinusOverflow(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.changeMembersOrder("Alice", -2)
        self.assertEqual(self.cut.getOrder(), ["Bob", "Alice", "Charlie"])
        
    def test_changeOrderOnOneMemberOK(self):
        o = self.cut.getOrder()
        o.pop(0)
        o.pop(0)
        self.assertEqual(self.cut.getOrder(), ["Charlie"])
        self.cut.changeMembersOrder("Charlie", 2)
        self.assertEqual(self.cut.getOrder(), ["Charlie"])
        
    def test_changeOrderWrongMemberFail(self):
        o = self.cut.getOrder()
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        with self.assertRaises(ValueError) as cm:
            self.cut.changeMembersOrder("Doris", 2)
        
    def test_writeUpdateOk(self):
        self.assertEqual(self.cut.getOrder(), ["Alice", "Bob", "Charlie"])
        self.cut.changeMembersOrder("Bob", 2)
        self.assertEqual(self.cut.getOrder(), ["Bob", "Alice", "Charlie"])
        self.cut.writeFile(".update")
        cut2 = Carewoche(self.file_t1 + ".update")
        self.assertEqual(cut2.getOrder(), ["Bob", "Alice", "Charlie"])
        
if __name__ == '__main__':
    unittest.main()