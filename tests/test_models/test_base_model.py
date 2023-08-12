#!/usr/bin/python3
''' Unit tests for the BaseModel class '''
import unittest
import time
from models import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Testing the BaseModel class '''

    def test_class_name(self):
        ''' Testing if the created object is of type BaseModel '''
        model = BaseModel()
        self.assertTrue(isinstance(model, BaseModel))

    def test_has_id(self):
        ''' Testing if the BaseModel object has an id at creation '''
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))

    def test_created_at(self):
        ''' Testing if the BaseModel object has
            the created_at attribute value set at creation'''
        model = BaseModel()
        self.assertTrue(hasattr(model, "created_at"))

    def test_updated_at(self):
        ''' Testing if the BaseModel object has
            the updated_at attribute value set at creation'''
        model = BaseModel()
        self.assertTrue(hasattr(model, "updated_at"))

    def test_update_at_eql_created_at(self):
        ''' Testing if the BaseModel object created_at and updated_at
            attributes have the same value at creation '''
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_str(self):
        ''' Testing the string formating of the BaseModel class '''
        model = BaseModel()
        self.assertEqual(str(model),
                         "[{}] ({}) {}".format(model.__class__.__name__,
                                               model.id, model.__dict__))

    def test_save(self):
        ''' Testing the save method of the BaseModel class '''
        model = BaseModel()
        a = model.updated_at
        time.sleep(1)
        model.save()
        self.assertTrue(a != model.updated_at)

    def test_to_dict(self):
        ''' Testing the formating of the BaseModel instance
            into a dictionary '''
        model = BaseModel()
        m_dict = model.to_dict()
        self.assertIsInstance(m_dict, dict)
        self.assertEqual(m_dict['__class__'], 'BaseModel')
        self.assertEqual(m_dict['id'], model.id)

    def test_arguments(self):
        ''' Testing the instantiation of the BaseModel
            using a dictionary '''
        i_dict = {'name': "John Doe", 'age': 89}
        model = BaseModel(**i_dict)
        self.assertEqual(model.name, "John Doe")
        self.assertEqual(model.age, 89)


if __name__ == '__main__':
    unittest.main()
