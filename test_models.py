import app.models

from app.db.database import Base


print("Registered tables:")

for table in Base.metadata.sorted_tables:
    print(f"- {table.name}")
