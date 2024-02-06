# Chord Intersections Counter

count-intersections code provides a solution for counting the number of intersections between chords in a circular arrangement. Each chord is defined by its starting and ending radians, along with a unique identifier.

## Segment Tree Implementation

The code includes a SegmentTree class, a data structure used for efficient range queries and updates. The segment tree is employed to keep track of active chords in the circular arrangement.

## `SegmentTree` Methods:

`__init__(self, n)`:
* Constructor initializes the segment tree with size `n`.
* The `tree` array is initialized with size `4 * n` as a safe upper bound. 
* The `lazy` array is initialized for lazy propogation to optimize range updates.

`update_range(self, node, start, end, l, r, val)`:

* Updates the segment tree within the specified range `[l, r]` with the given value `val`.
* `node`, `start`, and `end` define the current node's scope in the tree and also the segment of the array it represents.
* The method checks for any deferred updates and also checks for the location current segment with respect to the update range and updates the segment tree accordingly. 

`query_range(self, node, start, end, l, r)`:

* Queries the segment tree to get the **sum** within the range `[l, r]`.


## Chord Intersection Counter Function

The main function, `count_intersections(radians, identifiers)`, takes two lists as input

### Parameters
* `radians`: List of integers representing the starting radians of chords.
* `identifiers`: List of strings representing unique identifiers for chords.

### Return Type
* `intersections`: Integer representing the total count of intersections between chords in the circular arrangement.


## Algorithmic Logic:
The algorithm involves the following key steps:

1. Process Input Lists `chords`: Pairing each start and end point of chords based on the input lists.

2. Map Identifiers `chord_id`: Assigning a unique integer (1 to n) to each chord for easy management in the segment tree. 
Two points will have the same integer if and only if they are endpoints of the same chord.
`base_id` will contain 2n integer labels, each label appearing twice.

3. Sort Endpoints `sorted(endpoints)`: Sorting all endpoints (start and end points of chords) based on their radian measures.

### The idea behind the algorithm is to go through `sorted(endpoints)` once. When a label i is seen for the first time, an interval is opened for it. When i is seen again, we close its interval and find out how many intervals have been opened and **not closed** since i was first seen. Each of these represents an intersection between chord i and some other chord. 

4. Segment Tree: Implementing a segment tree data structure to manage active intervals (open chords). The segment tree supports insertion, deletion, and querying the number of active intervals within a range.

5. Count Intersections: Traverse through the sorted endpoints, using the segment tree to count intersections by querying the number of active intervals whenever an endpoint is encountered.


## Time complexity of the algorithm:

1. Sorting Endpoints:
The algorithm initiates by sorting all the endpoints (both start and end points of chords), which is O(2nlog(2n)) since there are 2n endpoints in total for n chords. This simplifies to `O(nlogn)` since constants and scalar multiples are ignored in big O notation.

2. Mapping Identifiers:
Creating a mapping for chord identifiers is linear with respect to the number of endpoints, O(2n), which simplifies to `O(n)`.

3. Segment Tree Operations:
For each of the 2n endpoints, the algorithm performs an update or query operation on the segment tree.

* Update Operation: The segment tree update operation (insertion or deletion of an interval) has a time complexity of O(logn) since it may need to traverse the height of the segment tree, which is proportional to the logarithm of the number of intervals (or chords).

* Query Operation: Similarly, querying the segment tree to count the number of active intervals also has a time complexity of O(logn) for the same reason as the update operation.

Since each of the 2n endpoints involves an operation on the segment tree with O(logn) complexity, the total time complexity for handling all endpoints with segment tree operations is O(2nlogn), which simplifies to `O(nlogn)`.

4. Overall Algorithmic runtime:
The summing up of time complexities for different parts of the algorithm gives O(nlogn) + O(n) + O(nlogn), which is `O(nlogn)` overall.

## How to Use:

* Provide lists of radians and identifiers to the count_intersections function.
* The function will return the count of intersections between the chords.

