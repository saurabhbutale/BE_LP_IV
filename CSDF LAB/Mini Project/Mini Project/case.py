import sys

def solution(I, J, K, X, Y, Z):
    # Total votes and minimum votes required to win
    total_votes = I + J + K
    min_votes_required = (total_votes // 2) + 1
    
    leader_votes = X + Y + Z
    
    # Case 1: Hacking wing A (double votes in A but not exceeding I)
    hack_A_votes = min(2 * X, I) + Y + Z
    if hack_A_votes >= min_votes_required:
        return "YES"

    # Case 2: Hacking wing B (one-third of B votes go to the opposition)
    hack_B_votes = X + (Y + (J // 3)) + Z
    if hack_B_votes >= min_votes_required:
        return "YES"

    # Case 3: Hacking wing C (flip all votes in C to the leader)
    hack_C_votes = X + Y + K
    if hack_C_votes >= min_votes_required:
        return "YES"

    return "NO"

def main():
    # Get input
    input_from_question = input().split()
    
    # Extracting values from input
    I, J, K = map(int, input_from_question[:3])
    X, Y, Z = map(int, input_from_question[3:])
    
    # Call the solution function and print the result
    result = solution(I, J, K, X, Y, Z)
    print(result)

# Running the main function
if __name__ == "__main__":
    main()
