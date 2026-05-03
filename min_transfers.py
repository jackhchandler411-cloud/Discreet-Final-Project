from collections import deque
from itertools import combinations


def build_station_lines(lines):
    """Map each station to the lines that pass through it."""
    station_lines = {}
    for line, stations in lines.items():
        for station in stations:
            station_lines.setdefault(station, []).append(line)
    return station_lines


def build_line_graph(station_lines):
    """Create a graph where each line is a node and edges exist when two lines share a station."""
    graph = {}
    for lines in station_lines.values():
        for a, b in combinations(lines, 2):
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
    for line in set(line for lines in station_lines.values() for line in lines):
        graph.setdefault(line, set())
    return graph


def min_transfers(lines, start, end):
    """Return the minimum number of transfers between start and end stations."""
    station_lines = build_station_lines(lines)
    if start not in station_lines or end not in station_lines:
        return None

    start_lines = set(station_lines[start])
    end_lines = set(station_lines[end])
    if start_lines & end_lines:
        return 0

    line_graph = build_line_graph(station_lines)
    queue = deque((line, 0) for line in start_lines)
    visited = set(start_lines)

    while queue:
        line, transfers = queue.popleft()
        if line in end_lines:
            return transfers
        for neighbor in line_graph[line]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, transfers + 1))
    return None


def explain_route(lines, start, end):
    station_lines = build_station_lines(lines)
    normalized = {station.lower(): station for station in station_lines}
    start_key = normalized.get(start.lower())
    end_key = normalized.get(end.lower())
    if not start_key or not end_key:
        return f"No route found. Check that both stations exist."
    start_lines = set(station_lines[start_key])
    end_lines = set(station_lines[end_key])
    if start_lines & end_lines:
        return f"The route requires 0 transfers: ride on the same line."
    transfers = min_transfers(lines, start_key, end_key)
    if transfers is None:
        return "No connection exists between these stations."
    return f"Minimum transfers from {start_key} to {end_key}: {transfers}."


def print_network(lines):
    print("Network map:")
    for line, stations in lines.items():
        print(f"  {line}: {' - '.join(stations)}")

    station_lines = build_station_lines(lines)
    intersections = {
        station: sorted(lines)
        for station, lines in station_lines.items()
        if len(lines) > 1
    }
    if intersections:
        print("\nTransfer stations:")
        for station, lines in sorted(intersections.items()):
            print(f"  {station}: connects {' and '.join(lines)}")
    print()


if __name__ == "__main__":
    lines = {
        "L1": ["A", "B", "C", "D"],
        "L2": ["C", "E", "F", "G"],
        "L3": ["D", "H", "I", "J"],
        "L4": ["G", "K", "L", "M"],
    }

    print_network(lines)
    stations = sorted({station for stations in lines.values() for station in stations})
    print("Available stations:", ", ".join(stations))
    start = input("Enter start station: ").strip()
    end = input("Enter end station: ").strip()
    print(explain_route(lines, start, end))
