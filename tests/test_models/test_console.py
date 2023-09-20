import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleCommands(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, command, expected_output, mock_stdout):
        with patch('builtins.input', return_value=command):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_help_commands(self):
        # Test the help messages for various commands
        self.assert_stdout("help quit", "Exits the program with formatting\n")
        self.assert_stdout(
            "help EOF",
            "Exits the program without formatting\n")
        self.assert_stdout(
            "help create",
            "Creates a class of any type\n[Usage]: create <className>\n")
        self.assert_stdout(
            "help show",
            "instance of a class\n[Usage]: show <className> <objectId>\n")
        self.assert_stdout(
            "help destroy",
            "instance of a class\n[Usage]: destroy <className> <objectId>\n")
        self.assert_stdout(
            "help all",
            "Shows all objects, or all of a class\n[Usage]: all <className>\n")
        self.assert_stdout("help count", "Usage: count <class_name>\n")
        self.assert_stdout(
            "help update",
            "information\nUsage: update <className> <id> <attName> <attVal>\n")

    def test_quit_command(self):
        # Test the quit command
        with self.assertRaises(SystemExit):
            self.assert_stdout("quit", "")

    def test_EOF_command(self):
        # Test the EOF command
        with self.assertRaises(SystemExit):
            self.assert_stdout("EOF", "\n")

    def test_create_command(self):
        # Test the create command
        self.assert_stdout("create", "** class name missing **\n")
        self.assert_stdout(
            "create NonExistentClass",
            "** class doesn't exist **\n")
        self.assert_stdout("create BaseModel",
                           "f1403f0f-824f-47e4-8e1c-df8e35ec6092\n")
        self.assert_stdout(
            "create User",
            "f1403f0f-824f-47e4-8e1c-df8e35ec6092\n")

    def test_show_command(self):
        # Test the show command
        self.assert_stdout("show", "** class name missing **\n")
        self.assert_stdout(
            "show NonExistentClass",
            "** class doesn't exist **\n")
        self.assert_stdout("show BaseModel", "** instance id missing **\n")
        self.assert_stdout("show BaseModel 123", "** no instance found **\n")

    # Similar tests can be created for other commands (destroy, all, count,
    # update)


if __name__ == '__main__':
    unittest.main()
