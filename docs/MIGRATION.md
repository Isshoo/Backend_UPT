COMMON ALEMBIC COMMANDS

"""

# Initialize Alembic dalam project

alembic init alembic
atau
alembic init app/database/migrations

# Generate migration otomatis dari model changes

alembic revision --autogenerate -m "Add user table"

# Create empty migration

alembic revision -m "Custom migration"

# Apply migrations

alembic upgrade head # Upgrade ke versi terbaru
alembic upgrade +1 # Upgrade 1 step
alembic upgrade ae1027a6acf # Upgrade ke revision tertentu

# Downgrade migrations

alembic downgrade -1 # Downgrade 1 step
alembic downgrade base # Downgrade ke awal
alembic downgrade ae1027a6ac # Downgrade ke revision tertentu

# Show migration history

alembic history # Show all migrations
alembic current # Show current migration
alembic show ae1027a6ac # Show specific migration

# Generate SQL without executing

alembic upgrade head --sql # Generate SQL untuk upgrade
alembic downgrade -1 --sql # Generate SQL untuk downgrade

# Merge multiple heads

alembic merge heads -m "Merge migrations"

# Stamp database (mark as migrated without running)

alembic stamp head # Mark as current
alembic stamp ae1027a6ac # Mark specific revision
"""
