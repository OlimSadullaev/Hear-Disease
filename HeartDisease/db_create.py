import sqlite3
from database.db_utils import create_table, insert_data, get_all_data

conn = sqlite3.connect('./database/patients.db')  # Replace with your desired filename

create_table(conn, 'patients', ["age",	"gender",	"cp",	"trestbps",
                                "chol",	"fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"])

conn.close()
