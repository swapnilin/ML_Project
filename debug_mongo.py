
import sys
import os
import pymongo
import certifi
import pandas as pd

# Add src to path
sys.path.append(os.getcwd())

from src.constants import DB_NAME, DB_CONNECTION_URL
from src.configuration.mongo_db_connection import MongoDBClient

def debug_mongo():
    print("Debugging MongoDB Connection...")
    print(f"DB_NAME constant: {DB_NAME}")
    print(f"DB_CONNECTION_URL env key: {DB_CONNECTION_URL}")
    
    mongo_url = os.getenv(DB_CONNECTION_URL)
    if not mongo_url:
        print(f"ERROR: Environment variable {DB_CONNECTION_URL} is not set.")
        return

    print(f"MongoDB URL found (masked): {mongo_url[:10]}...")

    try:
        # 1. Test raw connection first
        print("\n--- Testing Raw Connection ---")
        client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())
        print("Connected to MongoDB.")
        
        dbs = client.list_database_names()
        print(f"Available Databases: {dbs}")
        
        if DB_NAME not in dbs:
            print(f"WARNING: Database '{DB_NAME}' not found in available databases.")
        else:
            print(f"Database '{DB_NAME}' found.")
            db = client[DB_NAME]
            collections = db.list_collection_names()
            print(f"Collections in '{DB_NAME}': {collections}")
            
            # Check for 'mlops' collection specifically (hardcoded assumption based on constants or use case)
            target_collection = "mlops" # inferred from user description or constants
            # In src/constants/__init__.py: COLLECTION_NAME = "mlops"
            from src.constants import COLLECTION_NAME
            target_collection = COLLECTION_NAME
            print(f"Target Collection Name from constants: {target_collection}")
            
            if target_collection in collections:
                count = db[target_collection].count_documents({})
                print(f"Document count in '{DB_NAME}.{target_collection}': {count}")
                if count > 0:
                    print("First document sample:")
                    print(db[target_collection].find_one())
            else:
                print(f"WARNING: Collection '{target_collection}' not found in '{DB_NAME}'.")

        # 2. Test ProjectData class
        print("\n--- Testing ProjectData Class ---")
        from src.data_access.project_data import ProjectData
        
        project_data = ProjectData()
        df = project_data.export_collection_as_dataframe(collection_name=COLLECTION_NAME)
        print(f"DataFrame Shape: {df.shape}")
        print("DataFrame Head:")
        print(df.head())

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_mongo()
