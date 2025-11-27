import unittest
from src import models as md

class TestChemicalLookup(unittest.TestCase):
    
    def test_lookup_by_name(self):
        # Valid name returns Compound(24823)
        self.assertIsNotNone(md.lookup_by_name('ozone'))
        # Invalid name returns None
        self.assertIsNone(md.lookup_by_name('oozone'))
    
    def test_lookup_by_formula(self):
        # Valid formula returns Compound(24823)
        self.assertIsNotNone(md.lookup_by_formula('O3'))
        # Invalid formula returns None
        self.assertIsNone(md.lookup_by_formula('O32l'))
    
    def test_search(self):
        # Valid names/formulas return dictionaries
        self.assertIsInstance(md.search('ozone'), dict)
        self.assertIsInstance(md.search('O3'), dict)
        # Invalid input returns None
        self.assertIsNone(md.search('O123'))
    
    def test_filter_cmpd_info(self):
        # Invalid input returns message
        self.assertEqual(md.filter_cmpd_info('oozone'), 'Please Enter Name or Formula Again')
        # Valid compound returns dictionary
        self.assertIsInstance(md.filter_cmpd_info('ozone'), dict)
        # Filtering single property
        result = md.filter_cmpd_info('ozone', ['molecular_weight'])
        self.assertIsInstance(result, dict)
        self.assertIn('Molecular Weight', result)
        # Filtering multiple properties
        result = md.filter_cmpd_info('ozone', ['molecular_weight', 'molecular_formula'])
        self.assertIsInstance(result, dict)
        self.assertIn('Molecular Weight', result)
        self.assertIn('Molecular Formula', result)

if __name__ == '__main__':
    unittest.main()