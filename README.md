
# Zichun Mini Project 1

This is a Python project template with a functioning `Makefile`, a `.devcontainer`, and basic setup for CI/CD using GitHub Actions. The project also includes unit tests and linting with `pylint`.

## Links

- **Version control Source Code Management Repository**: [github repo](https://github.com/nogibjj/zichun-miniproject-1).
- **Link to successful CI/CD run**: [Link to GitHub Actions](https://github.com/nogibjj/zichun-miniproject-1/actions).


## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zichun-miniproject-1.git
cd zichun-miniproject-1
```

### 2. Install Dependencies

You can install the required Python dependencies by running:

```bash
make setup
```

This will install all the packages listed in `requirements.txt`.

### 3. Running the Linter

To ensure your code follows proper Python style guidelines, run:

```bash
make lint
```

This will run `pylint` on the `src/main.py` file.

### 4. Running Tests

To run the unit tests using `pytest`, use the following command:

```bash
make test
```

The `Makefile` is set up to run the tests in the `tests/` directory.

## Usage Instructions

The project contains a simple `add` function and a main script. You can run the main script as follows:

```bash
python src/main.py
```

The `main.py` file will print "Hello, world!" when executed.

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration (CI). The workflow is defined in the `.github/workflows/ci.yml` file and runs automatically on every push to the main branch. The CI performs the following actions:
- Linting with `pylint`
- Running unit tests with `pytest`

## Development Environment with Devcontainer

A development container is included to ensure consistency in development environments. The `.devcontainer` folder contains a `Dockerfile` and `devcontainer.json` file for setting up the containerized development environment in tools like Visual Studio Code.
