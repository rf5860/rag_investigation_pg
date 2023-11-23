import psycopg2

# Assuming you have set the database credentials and the derived embedding size
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "postgres"
DERIVED_EMB_SIZE = 128  # Example size

# Connect to your postgres DB
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# Using psycopg2 : Creation of Table
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS items (id bigserial PRIMARY KEY, text TEXT, embedding vector(" + str(DERIVED_EMB_SIZE) + "));")
conn.commit()  # Commit to save changes
cur.close()

# Using psycopg2 : Insertion Of Records
# Assuming documents and embeddings are defined
documents = ["doc1", "doc2", "doc3"]  # Example documents
embeddings = [[0.1]*DERIVED_EMB_SIZE, [0.2]*DERIVED_EMB_SIZE, [0.3]*DERIVED_EMB_SIZE]  # Example embeddings

cur = conn.cursor()
for index, item in enumerate(documents):
    my_doc = {"id": index, "text": documents[index], "embedding": embeddings[index]}
    cur.execute("INSERT INTO items(id, text, embedding) VALUES (%(id)s, %(text)s, %(embedding)s)", my_doc)
conn.commit()  # Commit to save changes
cur.close()

# Using psycopg2 : Retrieval
# Assuming user_query_embedding is defined
user_query_embedding = [0.15]*DERIVED_EMB_SIZE  # Example embedding

cur = conn.cursor()
cur.execute("SELECT text, 1 - (embedding <=> %s) AS cosine_similarity FROM items ORDER BY 2 DESC", [user_query_embedding])
for r in cur.fetchall():
    print(r[0], r[1])
cur.close()

# Close the database connection
conn.close()
