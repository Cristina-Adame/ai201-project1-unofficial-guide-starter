from query import retrieve

print("\n=== RETRIEVAL TEST ===")
query = "which professor that teaches CS429 or CS429H has the best lectures?"
chunks, metas, dists = retrieve(query)
print(f"Query: {query}\n")
for c, m, d in zip(chunks, metas, dists):
    print(f"Source: {m['source']} | Distance: {d:.3f}")
    print(c)
    print("---")
