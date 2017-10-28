# Leetcode

![png](https://img.shields.io/badge/language-Python%203-brightgreen.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[**All solutions are explained in Explanation/README.md**](Explanation/README.md).

This is my personal repo while learning algorithms. There is NO GUARANTEE for opitimal solutions, so sometimes you might find a better one that what I post here (If so, I appreciate it that if you can post an issue). 

# What's Leetcode？

> **LeetCode OJ** is a platform for preparing technical coding interviews. Pick from an expanding library of hundreds of questions, code and submit your solution to see if you have solved it correctly.

You can visit [Leetcode Online Judge](https://leetcode.com/) for more information.

# Solution Table

Each file in this repo goes with a number of simple tests, which use the example test testcase on LeetCode(or some cases made by myself). 

You may utilize my test code (`import _mytest`) to test the difference between your code and mine. 
- Time testing is supported by [line_profiler](https://pypi.python.org/pypi/line_profiler/) package.
- Unit testing is supported by [unittest](https://docs.python.org/3/library/unittest.html) built-in library.

You may find that some problems are skipped, because I've planed to only cover easy and medium problems at first run. But don't worry, this is a long-term project. Just give me some time.

Because the number of Python 3 submission is always too few, I test all my Python 3 code under "Python" instead of "Python 3". Therefore, the rank and time is only for fun.

| # | Title (with file link) | Cxty | Level | Category | Time | Rank | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Two Sum](0001.py) | *O(n)* | Easy | HashTable | 32ms | 97.3\% | |
| 2 | [Add Two Numbers](0002.py) | *O(n)* | Medium | LinkedList | 149ms | 22.4\% | |
| 3 | [Longest Substring Without Repeating Characters](0003.py) | *O(n)* | Medium | HashTable | 82ms | 88.5\% | |
| 5 | [Longest Palindromic Substring](0004.py) | *O(n)* | Medium | String | 838ms | 76.9\% | Manacher's Algo |
|  | | *O(n^2)* | | | 86ms | 95.3\% | Odd & Even |
| 6 | [Zigzag Conversion](0006.py) | *O(n)* | Medium | String | 92ms | 82.5\% | |
| 7 | [Reverse Integer](0007.py) | *O(1)* | Easy | Math | 42ms | 94.4\% | |
|  | | *O(1)* | | | 48ms | 72.0\% | No num2str |
| 8 | [String to Integer (atoi)](0008.py) | *O(1)* | Medium | String | 58ms | 77.8\% | |
| 9 | [Palindrome Number](0009.py) | *O(1)*| Easy | Math | 346ms | 11.6\% | O(1) Space |
| | | *O(n)* | | | 182ms | 98.1\% | O(n) Space | |
| 11 | [Container With Most Water](0011.py) | *O(n)* | Medium | Optmz | 56ms | 95.2\% | |
| 12 | [Integer to Roman](0012.py) | *O(n)* | Medium | Math | 95ms | 94.5\% | | 
| 13 | [Roman to Integer](0013.py) | *O(n)* | Easy | Math | 125ms | 82.8\% | |
| 14 | [Longest Common Prefix](0014.py) | *O(nm)* | Easy | String | 32ms | 96.4\% | Pythonic |
| | | *O(nm)* | | | 39ms | 66.7\% | `reduce` function |
| 15 | [3 Sum](0015.py) | *O(n^2)* | Medium | N/A | 959ms | 83.4\% | Scan from both sides |
| 17 | [Letter Combination of a Phone Number](0017.py) | *O(n\*4^n)* | Medium | Backtrack | 32ms | 84.5\% |  |
| 18 | [4 Sum](0018.py) | *O(n^3)* | Medium | N/A | 99ms | 93.7\% | N-Sum solution |

