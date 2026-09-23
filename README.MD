LSA Model from scratch used to query UF Labs

The following project is an attempt at querying UF Labs to specific fields using LSA.

Strategy:

1. Copy all the text from UF Website on all the labs

2. Tokenize the documents. (used stopwords from sci-kit learn)

3. Run LSA on the documents

4. When user runs a search query just project the query on the processed documents.