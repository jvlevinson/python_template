# Python Project Template

This repository serves as a template for Python projects, providing a clean and organized folder structure along with best practices for logging, configuration, and modularization. The project follows a well-structured layout to facilitate easy development, debugging, and maintenance.

## Folder Structure

```
project_name/
│
├── bin/                        # Main application code folder
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── main.py                 # Main script to run the program
│   ├── module1.py              # Code for specific feature/task
│   ├── module2.py              # Code for another feature/task
│   ├── utils.py                # Utility functions that are shared across modules
│   ├── logger.py               # Central logger configuration
│
├── logs/                       # Folder for log files
│   ├── app.log                 # Main application log
│
├── config/                     # Folder for configuration files
│   ├── settings.json           # JSON config file
│   ├── config.yaml             # YAML config file
│
├── data/                       # Folder for storing data files
│   ├── db.sqlite3              # SQLite database file (if using SQLite)
│   ├── dictionaries/           # Subfolder for custom dictionaries or lookup tables
│       ├── custom_dict.json
│
├── resources/                  # Folder for static files or other resources
│   ├── images/                 # Static images used in the app
│   ├── templates/              # Templates for reports, emails, etc.
│
├── scripts/                    # Additional helper or setup scripts
│   ├── setup_env.sh            # Script for setting up the environment
│   ├── backup.py               # Script for backing up the database or other data
│
├── tests/                      # Folder for all unit tests
│   ├── __init__.py
│   ├── test_module1.py         # Unit tests for module1
│   ├── test_module2.py         # Unit tests for module2
│
├── requirements.txt            # Lists all dependencies (like libraries)
├── README.md                   # Description of the project, how to set it up, etc.
├── setup.py                    # Script for packaging the project
├── .gitignore                  # Files and folders to ignore in version control
└── LICENSE                     # License for the project
```

## Explanation of Key Folders and Files

### `bin/` Folder
This folder contains the main code for the project. The code is organized into different modules based on functionality:
- **`main.py`**: The main script to run the application.
- **`module1.py`, `module2.py`**: Modules containing specific features or functionalities.
- **`utils.py`**: Common utility functions shared across multiple modules.
- **`logger.py`**: Central logging configuration to ensure consistent logging throughout the project.

### `logs/` Folder
Contains log files for the application. Logs help in debugging, monitoring errors, and tracking performance:
- **`app.log`**: The main log file for the application. Logs all relevant messages.

### `config/` Folder
Stores configuration files that contain settings and parameters for the application:
- **`settings.json`, `config.yaml`**: Files used for managing application settings, such as database connection strings or API keys, which can easily be modified without altering the core code.

### `data/` Folder
For storing data files, such as:
- **`db.sqlite3`**: The SQLite database file, used if the project requires lightweight database storage.
- **`dictionaries/`**: Subfolder to store lookup tables or custom dictionaries used in the application.

### `resources/` Folder
Contains static resources that the application might need:
- **`images/`**: Icons or other image resources used in the app.
- **`templates/`**: Templates for reports, emails, or other generated content.

### `scripts/` Folder
Contains helper or setup scripts:
- **`setup_env.sh`**: Script to help set up the development environment by installing dependencies.
- **`backup.py`**: Script to back up the database or other important data.

### `tests/` Folder
Contains unit tests for the application. Unit tests ensure that each module functions as expected:
- **`test_module1.py`, `test_module2.py`**: Unit tests for different modules to verify their correctness.

### Other Key Files
- **`requirements.txt`**: Contains a list of dependencies. Helps in setting up the environment with the necessary packages.
- **`setup.py`**: Used for packaging the project if you plan to distribute it.
- **`.gitignore`**: Specifies which files and directories should be ignored by version control (e.g., environment files, compiled Python files).
- **`README.md`**: Describes the project, setup instructions, and other relevant information.
- **`LICENSE`**: The license under which the project is distributed.

## Logging Best Practices
- **Centralized Logging**: A central logging setup (`logger.py`) is used throughout the project. Each module imports the logger to ensure all log messages are written consistently to the same log file.
- **Module-Specific Loggers**: The `get_logger(module_name)` function in `logger.py` can be used to create module-specific loggers. This helps in filtering logs by module, making debugging easier.
- **Logging Configuration**: The logging format includes timestamps, log levels, and module names for easy identification.

Example `logger.py` file:
```python
import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'app.log'),
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)

# Create a logger object for modules to import
logger = logging.getLogger('project_name')
```

## Getting Started

### Prerequisites
- Python 3.8+
- `pip` for installing dependencies

### Setup Instructions
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/username/project_name.git
   cd project_name
   ```

2. **Create a Virtual Environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```sh
   python bin/main.py
   ```

### Running Tests
To run unit tests:
```sh
pytest tests/
```

## Contribution Guidelines
- Follow PEP8 standards for Python code.
- Use the existing logging setup (`logger.py`) for consistent logging.
- Write unit tests for any new features or bug fixes.
- Update `README.md` and other documentation as necessary.

## Future Considerations
- **Database Management**: If the project scales, consider moving from SQLite to a more robust database solution like PostgreSQL or MySQL.
- **Continuous Integration**: Add CI tools (e.g., GitHub Actions) to automatically run tests when changes are pushed.
- **Deployment**: The `setup.py` file can be expanded for easier packaging and distribution.

## Questions?
Feel free to reach out if you have any questions about setting up or contributing to the project!

