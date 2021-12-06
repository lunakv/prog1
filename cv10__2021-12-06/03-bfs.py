# Pseudokód pro hledání vzdálenosti prohledáváním do šířky
def BFS(start, goal):
    queue = [] # fronta vrcholů čekajících na zpracování
    found = set() # množina již objevených vrcholů
    found.add(start)
    queue.append((start, 0)) # ve frontě si ukládáme s vrcholem i jeho vzdálenost

    while len(queue) != 0:
        current, dist = queue.pop(0)
        if current == goal:
            return dist

        # Při zpracování vrcholu přidáme do fronty všechny nové sousedy
        for neighbor in neighbors(vertex):
            if neighbor not in found:
                found.add(neighbor)
                queue.append((neighbor, dist+1))
