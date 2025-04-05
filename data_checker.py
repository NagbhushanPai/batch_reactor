with open('data.csv', 'r') as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i > 10: break
