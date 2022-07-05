# litera-assessment
Double Book overlapping problem

## Set Up:
- Download the `.py` files
- Run the `litera_test.py` file to assert the edge cases of the tests

## Time and Space Complexity
### Time Complexity:
    It was created with O($n^2$) time complexity since each time interval, after being sorted, is compared with the rest of the intervals
    Ideally, an efficient approach would have taken a O(n logn) time, with start and end times sorted separately, with the help of lambda functions. However, after       scratching different thought processes, I resorted to the brute force solution
    
## About test cases:
  The following edge cases are checked with python unittest module:
  - test for negative values
  - tests for start time being greater than end time
  - tests for overlapping of two events
  - tests if empty list is given with no intervals
  - tests if no overlap is found, or only one interval as input
  - tests a small set of intervals
  - tests a large set of intervals
