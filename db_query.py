import aiosqlite
import json

async def get_db():
    users = {} 
    async with aiosqlite.connect('db/users.db') as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users") as cur:
            async for row in cur:
                users[row['username']] = {'id': row['id'], 'is_admin': True if row['is_admin'] > 0 else False}
    return {'users': users}


            
    
async def insert_db(userid, username, isadmin):
    async with aiosqlite.connect('db/users.db') as db:
        await db.execute("INSERT INTO users (id, username, is_admin) VALUES (?, ?, ?)", (userid, username, isadmin))
        await db.commit()
        
        
async def delete_record(username):
    async with aiosqlite.connect('db/users.db') as db:
        await db.execute("DELETE FROM users WHERE username=?", (username,))
        await db.commit()
