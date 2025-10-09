from click.testing import CliRunner
from src.cli import calculate

def test_add_command():
    runner = CliRunner()
    result = runner.invoke(calculate, ["add", "5", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "8"

def test_subtract_command():
    runner = CliRunner()
    result = runner.invoke(calculate, ["subtract", "10", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "6"

def test_multiply_command():
    runner = CliRunner()
    result = runner.invoke(calculate, ["multiply", "7", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "14"

def test_divide_command():
    runner = CliRunner()
    result = runner.invoke(calculate, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "5"

def test_square_root_command():
    runner = CliRunner()
    result = runner.invoke(calculate, ["sqrt", "16"])
    assert result.exit_code == 0
    assert result.output.strip() == "4"
