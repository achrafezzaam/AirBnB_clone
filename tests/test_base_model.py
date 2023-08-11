#!/usr/bin/python3

import unittest
from datetime import datetime
import os
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], self.base.id)

    def test_save(self):
        prev_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(prev_updated_at, self.base.updated_at)


    def test_str(self):
        base_str = str(self.base)
        self.assertEqual(base_str, "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__))

    def test_create_instance(self):
        instance = BaseModel.create()
        self.assertIsInstance(instance, BaseModel)
        self.assertIn(instance.id, BaseModel.instances)

if __name__ == '__main__':
    unittest.main()
