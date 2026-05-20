from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from ai_code.cli import main


class CliTests(unittest.TestCase):
    def test_main_prints_default_greeting(self) -> None:
        stream = io.StringIO()

        with redirect_stdout(stream):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stream.getvalue(), "Hello, world!\n")

    def test_main_prints_custom_name(self) -> None:
        stream = io.StringIO()

        with redirect_stdout(stream):
            exit_code = main(["--name", "Cursor"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stream.getvalue(), "Hello, Cursor!\n")


if __name__ == "__main__":
    unittest.main()
