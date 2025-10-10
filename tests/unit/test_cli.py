from click.testing import CliRunner
from src.cli import calculate


def test_add_command():
    """Test add command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["add", "5", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "8"


def test_subtract_command():
    """Test sub command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["subtract", "10", "4"])
    assert result.exit_code == 0
    assert result.output.strip() == "6"


def test_multiply_command():
    """Test mul command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["multiply", "7", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "14"


def test_divide_command():
    """Test div command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert result.output.strip() == "5"


def test_square_root_command():
    """Test sqr command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["sqrt", "16"])
    assert result.exit_code == 0
    assert result.output.strip() == "4"


def test_divide_by_zero():
    """Test divz command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["divide", "5", "0"])
    assert result.exit_code != 0
    assert "Cannot divide by zero" in result.output


def test_unknown_operation():
    """Test unk command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["modulus", "5", "3"])
    assert result.exit_code != 0
    assert "Unknown operation" in result.output


def test_square_root_negative():
    """Test sqrneg command"""
    runner = CliRunner()
    result = runner.invoke(calculate, ["sqrt", "-9"])
    assert result.exit_code != 0
    assert "Error" in result.output or "Cannot" in result.output

def test_unexpected_error(monkeypatch):
    """Test unexp command"""
    runner = CliRunner()
    monkeypatch.setattr(
        "src.cli.add", lambda x, y: (_ for _ in ()).throw(Exception("Random error"))
    )
    result = runner.invoke(calculate, ["add", "2", "3"])
    assert result.exit_code != 0
    assert "Unexpected error" in result.output
