import sqlite3
import os

# Define the directory and database path
directory_path = '/Users/yanalaraghuvamshireddy/Downloads'
db_path = os.path.join(directory_path, 'rule_engine.db')

# Ensure the directory exists
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Connect to SQLite database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create a table for storing rules, if it isn't already created
c.execute('''
CREATE TABLE IF NOT EXISTS rules (
    id INTEGER PRIMARY KEY,
    rule_string TEXT NOT NULL,
    metadata TEXT
)
''')

# Sample data insertion function with error handling
def insert_sample_rule(id, rule_string, metadata):
    try:
        c.execute('INSERT INTO rules (id, rule_string, metadata) VALUES (?, ?, ?)', (id, rule_string, metadata))
    except sqlite3.IntegrityError:
        print(f'Rule with id {id} already exists. Skipping insertion.')

# Insert sample rules
insert_sample_rule(1, "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)", 'Sample rule 1')
insert_sample_rule(2, "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)", 'Sample rule 2')

# Commit changes and close the connection
conn.commit()
conn.close()