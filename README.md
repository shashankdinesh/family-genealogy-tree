DESCRIPTION
-----------

In Flinstones family genealogy tree has interesting structure. Every family member has exactly 2 children. Every male member has first male child and then female. Every female member has first female child and then male. We want to know what is the X-th child in the Nth generation. The generation starts with a male member.

Family structure:

                    M-------- 1st generation

              /         \
            M             F ------- 2nd child of 2nd generation
         /    \         /   \
        M     F       F     M
                      |
                   3rd child of 3rd generation

INPUT
-----

First line specifies T - the number of test cases.
Next T lines have 2 numbers, N and X
Read from standard input.

OUTPUT
------

For each test case write to standard output one line: “M” for male “F” for female (without quotes).

Constraints:

* 1<=T<=600
* 1<=N<=11000
* 1<=X<=min(10^15 , 2^(n-1))


EXAMPLE
-------

Input:
4
1 1
2 1
2 2
4 5

Output:
M
M
F
F


LIMITS:
-------

Time limit:     2s
Source limit:   4KB
Memory limit: 128MB
Deadline:     1:30h
