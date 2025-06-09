import builtins
from calculator import main

def test_run_calculator_add(monkeypatch, capsys):
    inputs = iter(["add", "2", "3", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    main.run_calculator()
    output = capsys.readouterr().out
    assert "Result: 5.0" in output
    assert "Welcome to the CLI Calculator!" in output
    assert "Goodbye!" in output

def test_get_number_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "42")
    assert main.get_number("Enter: ") == 42.0

def test_get_number_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["abc", "3.14"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = main.get_number("Enter: ")
    output = capsys.readouterr().out
    assert result == 3.14
    assert "Invalid number" in output

def test_invalid_operation(monkeypatch, capsys):
    inputs = iter(["modulus", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.run_calculator()
    output = capsys.readouterr().out
    assert "Invalid operation." in output

def test_value_error_handling(monkeypatch, capsys):
    def bad_divide(x, y):
        raise ValueError("fake value error for testing")

    original_divide = main.operations.divide
    main.operations.divide = bad_divide

    inputs = iter(["divide", "10", "2", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.run_calculator()
    output = capsys.readouterr().out

    assert "Please enter valid numbers." in output

    main.operations.divide = original_divide

def test_operation_exception(monkeypatch, capsys):
    original_add = main.operations.add
    del main.operations.add  # simulate missing function to raise AttributeError

    inputs = iter(["add", "2", "3", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main.run_calculator()
    output = capsys.readouterr().out

    assert "Error:" in output

    main.operations.add = original_add  # restore original function
