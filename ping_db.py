import os
from supabase import create_client, Client

# 1. Grab the hidden secrets from the environment
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 2. Initialize the Supabase client
supabase: Client = create_client(url, key)

try:
    # 3. Perform a basic read operation to register activity
    # Replace 'students' with the actual name of any table in your database
    response = supabase.table("students").select("*").limit(1).execute()
    print("Success: Database pinged and kept alive!")
except Exception as e:
    print(f"Error: Could not ping database. Details: {e}")
