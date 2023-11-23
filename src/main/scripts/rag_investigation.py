# Using psycopg2 : Creation of Table
cur = conn.cursor()
cur.execute(
    "CREATE TABLE items (id bigserial PRIMARY KEY, text TEXT, embedding vector(" + str(DERIVED_EMB_SIZE) + "));")
cur.close()

# Using psycopg2 : Insertion Of Records
# documents is list of sentences
# embeddings is embeddings for corresponding sentences
cur = conn.cursor()
for index, item in enumerate(documents):
    my_doc = {"id": index, "text": documents[index], "embedding": embeddings[index].tolist()}
    cur.execute("""INSERT INTO items(id,text,embedding) VALUES (%(id)s, %(text)s, %(embedding)s)""", my_doc)
cur.close()

# Using psycopg2 : Retrieval
# user_query_embedding is vector embedding of user query which will be used to search Knowledge Base
# We are finding Cosine Similarity between existing docs and user query
cur = conn.cursor()
cur.execute("""SELECT text, 1 - (embedding <=> '""" + str(
    user_query_embedding) + """') AS cosine_similarity FROM items order by 2 desc""")
for r in cur.fetchall():
    print(r[0], r[1])
cur.close()
