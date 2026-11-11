# test_tool_library.py - Sprint 3 starter tests
# Run with: python -m unittest discover -s src -v
import unittest
from tool_library import PowerTool, Member


class TestToolLibrary(unittest.TestCase):

    def setUp(self):
        # setUp() runs before EVERY test, so each test starts with a fresh
        # member and a fresh drill. Tests must not depend on each other.
        self.sarah = Member("Sarah")
        self.drill = PowerTool("Drill", 650)

    # Each test method name must start with "test_" so unittest finds it.
    # Pattern for every test: ARRANGE (set up), ACT (do something), ASSERT (check).

    def test_new_tool_is_available(self):
        self.assertTrue(self.drill.is_available())

    def test_cannot_borrow_unavailable_tool(self):
        self.sarah.borrow_tool(self.drill)            # arrange: drill is on loan
        with self.assertRaises(ValueError):           # assert: next line must fail
            Member("Tom").borrow_tool(self.drill)     # act: Tom tries to borrow

    def test_interested_member_is_notified(self):
        tom = Member("Tom")
        loan = self.sarah.borrow_tool(self.drill)
        self.drill.register_interest(tom)
        loan.return_tool()
        self.assertIn("Drill is now available", tom.messages)

    # TODO Task 2: test_cannot_return_twice
    #   borrow the drill, return it, then check that returning it again
    #   raises ValueError (hint: copy the pattern of the assertRaises test above)

    # TODO Task 3: one test of your own


if __name__ == "__main__":
    unittest.main()
