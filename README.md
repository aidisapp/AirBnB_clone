# AirBnB Clone Project

## Summary

This project aims to develop a clone of the AirBnB platform, implementing various features and functionalities. Below is a breakdown of the tasks and updates made to the project:

### Task 1: Create a Parent Class

- Created a `BaseModel` class with common attributes/methods for other classes.
- Implemented the `__str__` and `__repr__` methods for string representation.

### Task 2: Create a Simple Storage

- Developed a simple storage engine (`FileStorage`) to serialize/deserialize instances.
- Implemented methods for CRUD operations: `all`, `new`, `save`, `reload`.

### Task 3: Console I/O

- Created a command interpreter (`console.py`) to interact with the project's classes.
- Supported commands: `create`, `show`, `destroy`, `all`, `update`.
- Enabled usage of the interpreter to manage instances of `BaseModel`.

### Task 4: Do you even know JSON?

- Modified the `BaseModel` class to enable conversion to and from JSON format.
- Updated `FileStorage` to handle JSON serialization/deserialization.

### Task 5: All instances

- Extended `console.py` to handle `all` command for all class instances.
- Implemented `all` command for each class type.

### Task 6: More Commands!

- Added commands `show`, `destroy`, and `update` to the command interpreter.
- Allowed manipulation of class instances using these commands.

### Task 7: Yes, I do know about datetime

- Integrated `datetime` module to manage the timestamps of instance creation and update.
- Updated `BaseModel` and `FileStorage` to handle timestamps appropriately.

### Task 8: First User

- Created a `User` class inheriting from `BaseModel`.
- Added public class attributes: `email`, `password`, `first_name`, and `last_name`.
- Updated `FileStorage` to handle serialization and deserialization of `User`.
- Updated the command interpreter (`console.py`) to support CRUD operations for `User`.

### Task 9: More Classes

Implemented classes inheriting from `BaseModel`: `State`, `City`, `Amenity`, `Place`, and `Review`.

### Task 10: Console 1.0

Updated `FileStorage` to manage serialization and deserialization of new classes.
Enhanced the command interpreter to handle actions like show, create, destroy, update, and all for all classes.

## How to Use

1. Clone the GitHub repository: [AirBnB Clone](https://github.com/your_username/AirBnB_clone).
2. Navigate to the project directory.
3. Run `console.py` to start the command interpreter.
4. Use the provided commands to interact with the system.

## Files

- `models/base_model.py`: Contains the BaseModel class.
- `models/engine/file_storage.py`: Implements FileStorage for data persistence.
- `console.py`: Command interpreter with functionalities for managing instances.
- `tests/`: Directory containing unit tests for the project.

## How to Run Tests

1. Navigate to the `tests/` directory.
2. Run the desired test files using a testing framework like `unittest`.

## Contributors

- Idongesit Ekanem
- [aidisapp94@gmail.com]
