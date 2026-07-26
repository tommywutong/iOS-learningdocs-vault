---
title: 'Square Root: Numerical fun with NSDecimalNumber | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/square-root-numerical-fun-with.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:a8b9905fb9e4f5fe'
translated: false
---

> 原文：[Square Root: Numerical fun with NSDecimalNumber | Cocoa with Love](https://www.cocoawithlove.com/2008/05/square-root-numerical-fun-with.html)　·　Cocoa with Love (Matt Gallagher)

NSDecimalNumber is a powerful Foundation class that holds high precision base 10 numbers. The default class only provides basic arithmetic operators, leaving you to write any advanced operations that you need. This is an example that implements a square root using NSDecimalNumber.

## Casus belli: I want to expand my territory

Do you ever find yourself wishing for greater than the 15 decimal place precision of a 64-bit IEEE 754 floating point number? Of course you do. Your lab equipment is accurate to supernatural levels and your finances regularly deal with tens of trillions of dollars/euros accurately to the cent.

Or perhaps you're more like me — your lab equipment gives answers in "warmer/colder" and your finances are mostly organised around the barter system — but you really like long numbers.

Cocoa proudly offers the Foundation class NSDecimalNumber to satisfy this desire. NSDecimalNumber is a class which will give slightly better than twice the precision of a double (as much as 38 digits) and should never give the weird binary to decimal conversion quirks that binary doubles give (like 0.1 becoming 0.10000000000000000555 without warning).

Sadly, NSDecimalNumber does not appear to be written for the mathematically or scientifically inclined. Its operators are mostly limited to basic arithmetic: add, subtract, multiply and divide. It does provide the ability to raise to a power but only to whole number exponents.

So if we want anything more, we must write it ourselves. No problem?

## How do other people implement a square root?

You can't get very far in scientific or statistical calculations without a square root, so it's a good "higher level" function to implement first. So, how is it done?

The short answer is normally "an optimised Newton's method iteration". [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) goes like this:

- Take a first guess at the square root (it will be somewhere between the operand and 1)
- Use the slope of the line at the guess point (d/dx of sqrt(x) is 0.5x) to choose a next guess
- Repeat until you're close enough

Within this fairly simple set of steps is a huge range of possible implementation approaches. Most center on choosing a best first guess, avoiding accumulated error, avoiding floating point division and handling convergence quirks around x=1. Professor W. Kahan (who helped invent the IEEE 754 standard) and K.C. Ng wrote a [1986 paper on a range of these different approaches](http://www.netlib.org/fdlibm/e_sqrt.c).

Beyond these, there are some very strange alternate implementations of square root, including the ["Quake III" square root](http://www.codemaestro.com/reviews/9) which contains the utterly baffling line:

```objc
i  = 0x5f3759df - ( i >> 1 );
```

which exploits the specific binary representation of a 32-bit float to choose an exceptionally good first guess.

## How will I implement a square root?

I'm going to implement a square root in NSDecimalNumber, without peeking illegally at the internals of the number format (I'm guessing it's just a binary coded decimal). I'm not going to try anything fancy so this implementation will be:

- a little slow (maybe a hundred microseconds per calculation)
- may suffer from convergence and rounding errors near x=1 (last 1-3 digits of transcendental results will occasionally be wrong)

At least the code will be simple.

## Basic solution

Taking the easiest first guess (an average of the operand and 1) applying Newton's method to solve for the square root looks like this:

```objc
- (NSDecimalNumber *)sqrt
{
    NSDecimalNumber *half =
        [NSDecimalNumber decimalNumberWithMantissa:5 exponent:-1 isNegative:NO];
    NSDecimalNumber *guess =
        [[self decimalNumberByAdding:[NSDecimalNumber one]]
            decimalNumberByMultiplyingBy:half];
    
    NSCompareResult compare;
    do
    {
        NSDecimalNumber *previousGuess = [[guess copy] autorelease];
        guess = [self decimalNumberByDividingBy:previousGuess];
        guess = [guess decimalNumberByAdding:previousGuess];
        guess = [guess decimalNumberByDividingBy:two];
        
        compare = [guess compare:previousGuess];
    }
    while (guess != NSOrderedSame);
    
    return guess;
}
```

Make this a category method of NSDecimalNumber and you'll immediately be able to calculate the square root of 2.

But you'll get weird failures and infinite loops if you try to calculate the square root of 1.01, 0 or anything negative.

## A few special cases

Since we're not going to handle imaginary numbers, all attempts to take the square root of a negative number should return [NSDecimalNumber notANumber].

Then we have the quirks associated with taking the square root of zero. Two problems are occurring: if "previousGuess" is zero, then we are creating a divide by zero exception. Secondly, we are deliberately trying to converge on zero as the solution which means that we are deliberately creating an "underflow" (which is another kind of exception in NSDecimalNumber).

To address these problems, we'll simply put a blanket "try/catch" block around the do/while loop. When an exception occurs, we'll simply return the current guess which we can safely assume to be correct in both these cases.

Then we are left with one final problem: the listed method iterates until it converges on a solution (the guess has the same value for two iterations in a row). Unfortunately, there are many cases where this will never occur — especially for values close to 1. Instead, we'll replace the do/while with a fixed number of iterations. Experimentally, 4 iterations seems to handle most situations, 5 is sometimes needed. I've gone with 6 to be safe.

## Unanswered question

This solution will give square root answers with a worst case accuracy of 34 decimal places for values near 1 (according to my few experiments). I was expecting a worst case of at least 36 decimal places so I'm a little confused.

This error does not appear to be due to accumulated error or convergence problems. It appears to be because NSDecimalNumber is rounding numbers like (1 + 1e-35) to the nearest integer — even when I use an NSDecimalNumberBehaviors object that returns NSDecimalNoScale. This would appear to be unnecessary, given the 38 digit length of the mantissa. I'm not quite certain why it would do this but it appears to be reducing accuracy by approximately 2 decimal places.

If you know why this may be happening, please leave a comment and let me know.

## Final solution

```objc
- (NSDecimalNumber *)sqrt
{
    if ([self compare:[NSDecimalNumber zero]] == NSOrderedAscending)
    {
        return [NSDecimalNumber notANumber];
    }
    
    NSDecimalNumber *half =
        [NSDecimalNumber decimalNumberWithMantissa:5 exponent:-1 isNegative:NO];
    NSDecimalNumber *guess =
        [[self decimalNumberByAdding:[NSDecimalNumber one]]
            decimalNumberByMultiplyingBy:half];
    
    @try
    {
        const int NUM_ITERATIONS_TO_CONVERGENCE = 6;
        for (int i = 0; i < NUM_ITERATIONS_TO_CONVERGENCE; i++)
        {
            guess =
                [[[self decimalNumberByDividingBy:guess]
                    decimalNumberByAdding:guess]
                        decimalNumberByMultiplyingBy:half];
        }
    }
    @catch (NSException *exception)
    {
        // deliberately ignore exception and assume the last guess is good enough
    }
    
    return guess;
}
```
