# Discreet-Final-Project

## Goal
Build a simple Python method to find the route with the minimum number of train-line transfers in a public transport network.

## Key ideas
- Model the whole transport network as a universal set of stations.
- Model each train line as a subset containing the stations it serves.
- A transfer happens when a passenger moves from one line to another at an intersection station.
- The algorithm finds the fewest line changes required to go from a start station to a target station.

## How it works
1. Use set theory to describe lines and intersections.
   - Each line is a subset of stations.
   - Line intersections are stations shared by two or more lines.
2. Use a BFS search on the graph of lines.
   - Nodes are train lines.
   - Edges exist when two lines intersect at a station.
3. The BFS guarantees the minimum number of transfers.
   - If both stations are on the same line, the answer is zero.
   - Otherwise, each step in BFS is one transfer.

## Files
- `min_transfers.py` — minimal implementation of the transfer optimizer.

## Usage
Run the script with Python:

```bash
python min_transfers.py
```

The script prints a simple network map and the transfer stations, then asks for a start and end station.
Input is not case-sensitive, so you can type station names in any letter case.

The sample network in `min_transfers.py` demonstrates:
- 0 transfers when start and end are on the same line
- 1 transfer when one line change is needed
- more transfers when the path crosses multiple lines

## Mathematical justification
- Group B (Set Theory): represent the transport network as a family of subsets.
- Group A (Induction): prove that BFS finds the minimum transfer count.

### Induction argument
1. Base case: if the start and end stations lie on the same line, then no transfer is needed and the answer is 0.
2. Induction step: assume BFS has correctly found the minimum transfers for all routes requiring up to `k` transfers.
   - BFS examines lines in layers by transfer count.
   - After processing all routes with `k` or fewer transfers, the next frontier is all routes with `k+1` transfers.
   - If BFS reaches an end line at that stage, it is the first time that route appears, so the transfer count is minimal.

This shows that the algorithm terminates on the shortest path in terms of transfer count.

## Notes
The implementation is intentionally short and easy to read, under 150 lines, and focuses on minimum transfers instead of physical distance.