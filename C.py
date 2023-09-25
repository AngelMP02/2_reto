    # Calculate the minimum number of online subscribers required for all to have read the publication
    min_online_required = n - a

    # Initialize a counter for online subscribers
    online_subscribers = a

    # Iterate through the notifications
    for i in range(q):
        if notifications[i] == '+':
            online_subscribers += 1
        else:
            online_subscribers -= 1
        
        # If at any point, the number of online subscribers exceeds or equals the required minimum,
        # then it's guaranteed that all subscribers have read the publication.
        if online_subscribers >= min_online_required:
            return "YES"
    
    # If we reach this point, it means not all subscribers have read the publication yet.
    # However, it's possible that they might read it later, so we return "MAYBE".
    return "MAYBE"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, a, q = map(int, input().split())
    notifications = input()
    
    # Solve the test case and print the result
    result = solve_test_case(n, a, q, notifications)
    print(result)
