import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85):
   
    # Number of pages (nodes)
    N = M.shape[1]
    
    # Ensure matrix columns sum to 1 (normalize)
    M = M / M.sum(axis=0)
    
    # Initialize the rank vector to uniform probability (1/N for each page)
    ranks = np.ones(N) / N
    
    # Iteratively apply the power method to compute the PageRank vector
    for _ in range(num_iterations):
        ranks = (1 - d) / N + d * M @ ranks
    
    return ranks

# Example usage

# Example adjacency matrix (4 pages: A, B, C, D)
# Pages A, B, C, D linking to each other
# M[i][j] = 1 if page j links to page i, 0 otherwise
M = np.array([[0, 0, 1, 0],  # Page A
              [1, 0, 0, 0],  # Page B
              [0, 1, 0, 1],  # Page C
              [1, 1, 1, 0]])  # Page D

ranks = pagerank(M)

# Display the PageRank scores
print("PageRank Scores:")
for i, score in enumerate(ranks):
    print(f"Page {chr(65 + i)}: {score:.4f}")
