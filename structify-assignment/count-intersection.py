class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update_range(self, node, start, end, l, r, val):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        # if current segment is completely outside range 
        if start > end or start > r or end < l:
            return

        # if current segment is completely within range
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                self.lazy[node * 2] += val
                self.lazy[node * 2 + 1] += val
            return
        
        # if current segment is partially within range
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, l, r, val)
        self.update_range(node * 2 + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query_range(self, node, start, end, l, r):
        # if current segment is completely outside range 
        if start > end or start > r or end < l:
            return 0

        # check for any pending updates
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        # if current segment is completely overlaps with range
        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        p1 = self.query_range(node * 2, start, mid, l, r)
        p2 = self.query_range(node * 2 + 1, mid + 1, end, l, r)
        return p1 + p2


def count_intersections(radians, identifiers) -> int:
    """
    This function counts the number of intersections 
    between chords in a circle. Each chord is represented by its 
    starting and ending radians along with its identifer
    
    params:
    radians: List[int]
    identifiers: List[str]

    rtype:
    intersections: int
    """
    chords = sorted(zip(radians, identifiers), key=lambda x: x[0])
    id_map = {}
    endpoints = []
    
    for radian, identifier in chords:
        # Extract digits to handle both formats
        base_id = ''.join(filter(str.isdigit, identifier))
        is_start = identifier.startswith("s")
        if is_start:
            id_map[base_id] = len(id_map) + 1
        chord_id = id_map[base_id]
        endpoints.append((radian, chord_id, is_start))
    
    intersections = 0
    segment_tree = SegmentTree(len(id_map))
    
    for _, chord_id, is_start in sorted(endpoints):
        if is_start:
            segment_tree.update_range(1, 1, len(id_map), chord_id, chord_id, 1)
        else:
            segment_tree.update_range(1, 1, len(id_map), chord_id, chord_id, -1)
            intersections += segment_tree.query_range(1, 1, len(id_map), chord_id + 1, len(id_map))
    
    return intersections