# tool_library.py - Northpoint Community Tool Library
# Sprint 3 starter code for CSDD5012 Software Engineering, Week 8.
# There is a deliberate bug in Loan.return_tool(): finding it is Task 2 (US10).
from datetime import date


class Tool:
    """A tool that members can borrow. Other members can ask to be told
    when it comes back (Observer pattern)."""

    def __init__(self, name):
        self.name = name
        self._available = True     # US1: new tools start available
        self._interested = []      # members waiting for this tool

    def is_available(self):
        return self._available

    def check_out(self):
        if not self._available:
            raise ValueError(f"{self.name} is already on loan")
        self._available = False

    def check_in(self):
        self._available = True
        self._notify()

    def register_interest(self, member):
        self._interested.append(member)

    def _notify(self):
        for member in self._interested:
            member.receive(f"{self.name} is now available")
        self._interested.clear()

    def describe(self):
        return self.name


class PowerTool(Tool):
    """A tool that needs mains power (inheritance)."""

    def __init__(self, name, watts):
        super().__init__(name)
        self.watts = watts

    def describe(self):
        return f"{self.name} (power tool, {self.watts}W)"


class Ladder(Tool):
    """A ladder, described by its height in metres (inheritance)."""

    def __init__(self, name, height_m):
        super().__init__(name)
        self.height_m = height_m

    def describe(self):
        return f"{self.name} (ladder, {self.height_m}m)"


class Member:
    """A member of the tool library."""

    def __init__(self, name):
        self.name = name
        self.messages = []

    def borrow_tool(self, tool):
        return Loan(self, tool)

    def receive(self, message):
        self.messages.append(message)


class Loan:
    """Records who borrowed which tool, and when it went out and came back."""

    def __init__(self, member, tool):
        tool.check_out()               # FIRST: an unavailable tool stops the loan
        self.member = member
        self.tool = tool
        self.borrowed_on = date.today()
        self.returned_on = None

    def return_tool(self):
        self.returned_on = date.today()
        self.tool.check_in()
