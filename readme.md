# Weather Data Analytics Project

## Setup Instructions

### 1. Create and Activate Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```

---

### 2. Install Dependencies

1. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

---

### 3. Set Up Database

1. Open MySQL or a database management tool.
2. Execute the `setup.sql` script to create the database and configure users:
   ```sql
   SOURCE database/setup.sql;
   ```

---

### 4. Fetch Data from API

Run the script to fetch weather data and save it as CSV files:
```bash
python scripts/fetch_data.py
```

---

### 5. Import Data into Database

Run the main database script to create tables and import data:
```bash
python database/main.py
```

---

## Requirements

- **Python** 3.12+
- **MySQL** 8.0+
- Install dependencies from `requirements.txt` and `setup.py`.

---

## License

This project is licensed under the **MIT License**.
