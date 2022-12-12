trees = open('inputs/08.txt').read().splitlines()
rows = [[int(t) for t in row] for row in trees]
cols = [[t for t in row] for row in zip(*[row for row in rows])]

# H = height, L = left, R = right, U = up, D = down

def treepaths(X, Y, row, col):
    L, R = row[:Y], row[1+Y:]
    U, D = col[:X], col[1+X:]
    return dict(L=L, R=R, U=U, D=D)

def is_hidden(H, L, R, U, D):
    return H <= min(max(L), max(R), max(U), max(D))

def how_scenic(H, L, R, U, D):
    directions = [L[::-1], R, U[::-1], D]
    score = 1
    for dir in directions:
        for j, height in enumerate(dir):
            if height >= H or j == len(dir) - 1:
                score *= (j+1)
                break
    return score

def count_and_score_visible_trees(tree_count=0,
                                  best_score=0):
    for i, row in enumerate(rows):
        if i == 0 or i == len(row) - 1:
            tree_count += len(row)
            continue

        for j, height in enumerate(row):
            if j == 0 or j == len(row) - 1:
                tree_count += 1
                continue

            mapper = treepaths(i, j, rows[i], cols[j])
            hidden = is_hidden(height, **mapper)
            score = how_scenic(height, **mapper)

            tree_count += int(not hidden)
            best_score = max(best_score, score)
    return tree_count, best_score

count, score = count_and_score_visible_trees()
print(f'DAY 8 | PART 1: {count}')
print(f'DAY 8 | PART 2: {score}')
