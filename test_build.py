from unittest import TestCase


class TestBuild(TestCase):
#check if the strings or parameter are added or not
#check if the string is there or not
#check if first parameter is word only
#check if second parameter is word only
#check check if both parameter are same
#check if both parameter are same but swap

    def test_check_if_the_strings_or_parameter_are_added_or_not(self):
       try:
        from build import build
       except ImportError:
           self.assertFalse("Import Error")

           result = build(None,None)
           self.assertEqual(False,result)

    def test_check_if_the_string_is_there_or_not(self):
       try:
        from build import build
       except ImportError:
           self.assertFalse("Import Error")

           result = build("","")
           self.assertEqual(False,result)

    def test_check_if_first_parameter_words_only(self):
       try:
        from build import build
       except ImportError:
           self.assertFalse("Import Error")

           result = build("123sa","as")
           self.assertEqual(False,result)

    def test_check_if_second_parameter_words_only(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

            result = build("wqw", "12wqw")
            self.assertEqual(False, result)

    def test_check_if_both_parameter_are_same(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

            result = build("wqw", "wqw")
            self.assertEqual(False, result)


    def test_check_if_both_parameter_are_same_swap(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

            result = build("wqw", "qww")
            self.assertEqual(True, result)

    def test_check_if_both_parameter_have_different_letter(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

            result = build("adfe", "ret")
            self.assertEqual(False, result)