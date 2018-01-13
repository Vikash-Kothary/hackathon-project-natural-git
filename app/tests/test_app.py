#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests/test_app.py - Testing App
"""

import unittest

from ..app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.debug = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_success(self):
        response = self.app.get('/success', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
