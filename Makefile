setup:
    pip install -r requirements.txt

lint:
    pylint src/main.py

test:
    pytest tests

