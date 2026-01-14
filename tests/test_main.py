from defaultpython.main import main


def test_main_runs() -> None:
    """Basic test to ensure main function exists and runs without error."""
    # Since main() currently just prints, we'll just call it.
    # In a real app, you might mock stdout or check return values.
    main()
