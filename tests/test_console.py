import unittest
from unittest.mock import patch, call
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    @patch('console.HBNBCommand.cmdloop', return_value=None)
    def test_quit(self, mock_cmdloop):
        console = HBNBCommand()
        result = console.cmdloop()
        self.assertIsNone(result)
        mock_cmdloop.assert_called_once()


if __name__ == '__main__':
    unittest.main()
