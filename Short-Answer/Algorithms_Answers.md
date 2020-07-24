#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


O(n) - Linear time
If you were to make this functional in python youd see that
the number of operations is equal to the number of the input
if you graph the size of the input and the # of operations you will see
that the line resembles 0(n) the most.


b)
O(log n) - Logarithmic

at first I thought this was quadratic because of the nesting.
but if you look closely you will see that j is limiting the number
of outputs on n through the while loop. Logarithmic algorthims are defined by
a function thats time complexity decreased over time. that is exactly
what is happening when j is being multiplied by 2.

c)
O(n) - Linear time
Linear time again! if you count the number of operations you will see that
the number of operations are equal to the input.

## Exercise II
O(n) - linear
if you want to minimize eggs lost you would need to start throwing eggs from the
very bottom floor. if your egg does not break on the first floor go up a floor.
keep going up a floor when your egg does not break. the first floor an egg
breaks on and higher will be the floors that all eggs will break on if thrown.
the reason why this is the best case for minimum breakage is because
you could have way more floors than eggs. if you start at the top of
the building you could run out of guesses before you reach a floor
the egg breaks on.

