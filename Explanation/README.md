# Explanation of All Problems

This post might help those who don't understand the algorithm thoroughly. 

## 0001 Two Sum

*See also*: 0015 (3 sum), 0018 (4 sum).

Use the "index" and "value" to save the summation relation information so that we only need to scan the whole list once. Time complexity *O(n)*.

Instead, the naive thought costs *n(n-1)/2* times comparision (worst), therefore it will be much slower.

## 0002 Add Two Numbers

Key points:
1. Even when `l1` and `l2` are scanned to the tail, we still need to continue if `num` is not zero after divided it by 10 (`num //= 10`). Because that means we should carry it to a new digit, e.g.: (9) + (1) = (0->1).
2. Since the linked list is singled, so we put the value in `current.next` instead of `current` to avoid deleting a possible tail dummy node. We just return a linked list from `lsum.next` instead of `lsum`, which is kind of tricky.


## 0003 Longest Substring Without Repeating Characters

Key points:
1. Such a substring can only be triggered when a duplicate letter is found --- except there is no duplicate letter in the whole string (that's the reason of returning `max(L, len(s) - head)`).
2. When a duplicate letter `ch` is found, say `s[j2]` and `s[j1]`, move the head of the candidate substring to `s[j1+1]` and continue scanning.

## 0004 Longest Palindromic Substring

A basic truth: The center of a palindromic substring can be either a letter or a "gap": "aba" (leter "b") and "abba" (gap between two "b").

- Manacher's Algorithm.   
It insert "#" (or other symbol which won't appear in any input string) on both sides of every char of the original string (e.g. convert "abc" to "#a#b#c#"). 
1. It means you don't need to consider the gap-or-letter problem. Now all gaps have become letters. This is really clever because it can surely shorten your code.
2. The algorithm uses `center` and `redge` to represent the center of the palindromic substring who has a *rightmost right-edge* among all known substrings. When we check a new center `i` (where `center < i < redge` and we have already known `p[j]`) and its radius `p[i]`, we can tell that `p[i]` is surely greater than or equal to `min(p[j], redge - i)`. This thought avoid many unnecessary comnparisions.

A simple figure:

                 p[i] >= min(p[j], redge - i)
                             ___________________
                            |   2 * (redge - i) |
                            |                   |
    ---------ledge-------j---center---i-------redge----------  
           |                              |
           |______________________________|               
                       2 * p[j]             

## 0006 ZigZag Conversion

Scan the word in the original sequence, record them to different string categoried by row indices.

In common sense, we might choose to scan the word in the same order as how we print the converted one. Then we need to consider many patterns and turn this problem into a maths one. BUT DON'T DO THAT.

## 0007 Reverse Integer

32-bit signed integer should locate between -2^31~2^31-1.

In Python, lists are implemented from dynamic arrays. So `[::-1]` process (slicing) can be fast.

## 0008 String to Integer (atoi)

Nothing special. Unexpected chars (include spaces and decimal dot), positive/negative sign, integer overflow... Consider all above and you can simply get the answer.

## 0009 Palindrome Number

THIS PROBLEM REQUIRES O(1) SPACE! I believe some submissions on LeetCode ignore this constraint.

Key points:
1. Negative number cannot be palindromic.
2. A non-negative less-than-10 integer is guaranteed to be palindromic.
3. Check from both sides of the number to the center. Scale is divided by 100 so you don't need to consider the odd-or-even cases (e.g. 121 and 1221 can be determined by same code).

## 0011 Container With Most Water

Scan from both sides, `v = (j - i) * h` where `h = min(height[i], height[j])`. 

A trick is that we can skip some vertical lines in the middle of our scanning path, if their height is not larger than `h`.

## 0012 Integer to Roman

Because each digit can only have 10 cases, the straightforward thought is quite high efficient. The algorithm starts from the highest digit to the lowest.

## 0013 Roman to Integer

When a digit number is larger than or equal to the number on its right digit, it should be added to the sum; otherwise it should be subtracted from the sum.

The last digit will always be added.

## 0014 Longest Common Prefix

The `zip` function can help you to transpose a "matrix" (a list whose entries are all also lists). This trick works well in this problem, since it makes it feasible to use `set` function to examine equality along each "column".

Another thought is to use `reduce` function, because comparison between each pair of strings affects how we compare next pair (namely, it helps update the upper bound of longest common prefix length). This is also the basic idea of `reduce` function.

## 0015 3 Sum

*See also*: 0001(two sum), 0018(4 sum).

It's currently accepted that the algorithm should be *O(n^2)*. First sort the list, then enumerate the first number from lowest to highest (outer loop), and scan the other 2 numbers from both sides of the sequence between the first number and the tail number (inner loop). 

## 0017 Letter Combinations of a Phone Number

A good backtracking example. Note that when we talk about `reduce` function:
```
reduce(func, lst, initial=I)
``` 
equals to the last entry of sequence: `a_0 = func(I, lst[0]), a_1 = func(a_0, lst[1]), a_i = func(a_[i-1], lst[i])`.


## 0018 4 Sum

*See also*: 0001(two sum), 0015(3 sum).

Hey, we have done many "k-sum" problems! The basic idea is to reduce k to 2, then solve it. So we use recursion here, and it does work well.

## 0019 Remove Nth Node from End of List

Two pointers, just similiar with 0002 (Add two numbers).

## 0020 Valid Parenthesis

A simple stack question. Main idea:
1. If the current char is a left parenthesis, push it into the stack.
2. If the current char is a right parenthesis:
    - If it doesn't match the top of stack (or the stack is empty), return False.
    - Otherwise, pop the top char of the stack.
3. At the end of the loop, return True if the stack is empty.


## 0021 Merge Two Sorted List

Very straightforward. You can also use recursion method to solve it.
