# Unit Testing with Python

This project is focused on implementing unit tests for Python modules, specifically testing the `access_nested_map` function from the `utils` module. The tests are written using the `unittest` framework and the `parameterized` library for enhanced test case handling.

## Project Structure

- **test_utils.py**: Contains unit tests for the `access_nested_map` function.
- **utils.py**: The module being tested (assumed to be available in the project).

## Features

1. **Unit Testing**: Ensures each function works as expected with defined inputs and outputs.
2. **Parameterized Tests**: Test cases are parameterized for better readability and maintainability.

## Dependencies

- Python 3.7
- `unittest` (Built-in Python library)
- `parameterized`

To install the required `parameterized` library, run:
```bash
pip install parameterized
```

## Usage

### Running Tests
To execute the tests, ensure the test file is executable and run it as follows:
```bash
chmod +x test_utils.py
./test_utils.py
```

Alternatively, use:
```bash
python3 test_utils.py
```

### Example Test Cases
- Accessing a simple key in a nested map.
- Accessing nested keys within a map.

### Test Cases
| Test Case    | Input Map          | Path       | Expected Output |
|--------------|--------------------|------------|-----------------|
| Test Case 1  | {"a": 1}          | ("a",)     | 1               |
| Test Case 2  | {"a": {"b": 2}} | ("a",)     | {"b": 2}      |
| Test Case 3  | {"a": {"b": 2}} | ("a", "b") | 2               |

## Coding Standards

- All files are executable.
- Follows `pycodestyle` guidelines (version 2.5).
- Comprehensive documentation for modules, classes, and functions.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- All functions and coroutines are type-annotated.

## License

This project is for educational purposes and does not include a specific license.

