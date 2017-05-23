from unittest import TestCase


class TestBuild(TestCase):
    def test_ransom_note(self):
        try:
            from build import match_note_to_magazine
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, match_note_to_magazine, None, None)
        self.assertEqual(match_note_to_magazine('', ''), True)
        self.assertEqual(match_note_to_magazine('a', 'b'), False)
        self.assertEqual(match_note_to_magazine('aa', 'ab'), False)
        self.assertEqual(match_note_to_magazine('aa', 'aab'), True)