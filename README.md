# Knapsack 0/1 problem project

`This project contains three possible solutions to the knapsack 0/1 problem.` <br>
 

## The *greedy* solution 

Our first solution works by __sorting__ every items of our dictionary using the __value / weight__ ratio. Starting from the best ratio each items are added until there is no __space left__ in the knapsack. Finally, if we include the sorting process this solution land a very low time complexity of O(n*log(n)) and a constant space complexity. But keep in mind that this solution will not provide the best knapsack frequently.

## The *best* solution
Our second solution will use the concept of __*dynamic programming*__ to a next level by adding __*recursion*__  and __*memoization*__. Its purpose is to calculate the knapsack value at a current items and capacity remaining by avoiding repetition and over computation since our number of items is fixed. This technique checks if a knapsack has __already been calculated before processing__ the recursive part, if not the process will go on and __store the result__ at the end. This algorithm runs on a time complexity of __O(n*W)__ (number of items * weight) and the space complexity is also  __O(n*W)__ since we're storing calculated value.    

## The *optimal* solution
Our third and final solution can also be called the brainless one. Its main qualification is to calculate and compare every possible knapsack combination to get the best one. Althought, This brute-force technique will guarantee the best possible solution for the Knapsack 0/1 problem its drawback will be its exponential time complexity of O(2^n). Checking each combination takes time and consider using it on a low number of items.

## Sources

1. Greedy solution <br>
[Sorting a dictionnary](https://stackoverflow.com/a/613218)
1. Best solution <br>
[Dynamic programming using memoization](https://youtu.be/xOlhR_2QCXY) <br>
[Dynamic programming explanation](https://youtu.be/nLmhmB6NzcM) <br>
[Wikipedia compiling every possible solution](https://en.wikipedia.org/wiki/Knapsack_problem)
1. Optimal solution <br>
[Brute-force approach explaned very well](https://youtu.be/81vqsCxHWAw) <br>
[great article on brute-force and dynamic approach](https://www.educative.io/blog/0-1-knapsack-problem-dynamic-solution)
1. Bottom-up approach (not chosen) <br>
[bottom-up tabulation](https://youtu.be/cJ21moQpofY)
