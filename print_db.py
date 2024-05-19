from app import app, db
from sqlalchemy import inspect, text

def print_all_tables():
    with app.app_context():
        # Get the database inspector
        inspector = inspect(db.engine)
        
        # Get all table names
        tables = inspector.get_table_names()
        
        if not tables:
            print("No tables found in the database.")
            return
        
        for table_name in tables:
            print(f"Table: {table_name}")
            
            # Get columns for the table
            columns = inspector.get_columns(table_name)
            column_names = [column['name'] for column in columns]
            for column in columns:
                print(f"Column: {column['name']}, Type: {column['type']}")
            
            # Query all data from the table
            records = db.session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
            for record in records:
                record_dict = {column_names[i]: record[i] for i in range(len(column_names))}
                print(record_dict)
            print("\n")
if __name__ == '__main__':
    print_all_tables()
