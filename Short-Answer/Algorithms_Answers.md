#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  This is (n^3) (n * n * n) Because the number of operations
    will dramatically increase even though n is changed insignificantly
    for example 5*5*5 = 125 vs 10*10*10 = 1000


b)  This is O(n^2).
    For elements in range the program will go through the elements. There's a loop inside the loop.


c)  It's O(1) because the number of operations that the function does
    is always the same no matter how much input it receives

## Exercise II


I would use binary search O(log n).
The floors are like a sorted array. Every time I go down 1 floor, the
quantity of broken eggs decreases.

- I would set the base case where there's no more floors left
- And then start splitting floors by half
- find the middle floor in that range
- throw an egg from that floor
- if an egg gets broken, look up in the left hand part of range ("go downstairs"), recurse
- return the floor if an egg didn't broke otherwise return -1