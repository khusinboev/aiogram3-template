from .connects import db

async def create_tables():
    await db.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id BIGSERIAL PRIMARY KEY,
            user_id bigint NOT NULL UNIQUE,
            username character varying(32),
            lang_code character varying(10),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
