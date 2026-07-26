---
title: 'Friday Q&A 2011-01-04: Practical Floating Point'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-01-04-practical-floating-point.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dd4864738492897c'
translated: false
---

> 原文：[Friday Q&A 2011-01-04: Practical Floating Point](https://www.mikeash.com/pyblog/friday-qa-2011-01-04-practical-floating-point.html)　·　mikeash.com Friday Q&A

Posted at 2011-01-14 16:33 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Complete Friday Q&A Now Available](https://www.mikeash.com/pyblog/complete-friday-qa-now-available.html)  
Previous article: [Rogue Amoeba Is Hiring Again](https://www.mikeash.com/pyblog/rogue-amoeba-is-hiring-again.html)  
Tags: [float](https://www.mikeash.com/pyblog/?tag=float) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2011-01-04: Practical Floating Point

by [Mike Ash](https://www.mikeash.com/)

First, I want to discuss what I will cover. I do _not_ intend a deep theoretical discussion of floating point calculations, nor even the sorts of things you'd need to know when doing heavy numeric or scientific calculations with them. The classic [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://web.archive.org/web/20080527204528/http://docs.sun.com/source/806-3568/ncg_goldberg.html) covers that ground well.

What I intend to cover is how to approach floating-point arithmetic in a practical, pragmatic sense when writing your everyday Mac or iOS applications. Where to use floating point, where not to use it, what it's good for, and useful tricks.

**Myths**  
 Before getting into the meat, I want to discuss two myths which are fairly pervasive in the programming community:

1. Floating point calculations are slow
2. Floating point calculations are inaccurate

Floating point was slow in the dark ages before a floating-point unit was a standard part of any CPU you'd be programming on. These days, it's pretty fast. On heftier processors (like on the Mac), using floating point can actually make your code go _faster_, due to freeing up integer units for other tasks. Even on iOS devices, the floating point support is entirely reasonable and there's no need to shy away without extensive profiling.

Floating point accuracy is harder to characterize than simply saying it's inaccurate. Many floating point calculations produce exact results. Most others produce results which are as close to the exact answer as is possible to represent. Accuracy must be properly understood to use floating point properly, but it's not always bad and not always a problem.

**Floating Point Representation**  
 While I don't want to get into the exact binary representation of floating point numbers, it is useful to understand the basics of how they are represented. Those interested in the lowest-level details can read about the [IEEE-754 spec](http://en.wikipedia.org/wiki/IEEE-754).

Note that there is nothing in C which _requires_ the floating point types to use IEEE-754 semantics. However, that is what is used on all Apple platforms, and what you're likely to find anywhere else, so everything I discuss here assumes IEEE-754.

You are probably familiar with scientific notation. To put a number in scientific notation, you normalize the number by multiplying or dividing by 10 until the number is in the range `[1, 10)`, and then you multiply it by a power of 10 to get it back where you want it:

- 42 = 4.2 × 10^1
- 998.75 = 9.9875 × 10^2
- 0.125 = 1.25 × 10^-1

By using binary and powers of 2, this concept can be changed to something that's more friendly to computers:

- 42 = 101010~2 = 1.01010~2 × 2^5
- 998.75 = 1111100110.11~2 = 1.11110011011~2 × 2^9
- 0.125 = 0.001~2 = 1.0 × 2^-3

The 2 never changes, which means that these numbers can be represented as simple pairs:

- (1.01010, 5)
- (1.11110011011, 9)
- (1.0, -3)

The first component of these pairs is called the _mantissa_, and the second component is the _exponent_.

You'll notice that the leading digit on all three is 1. In fact, the leading digit will _always_ be 1, except for representing zero, which is a special case. Since the leading digit is always 1, it's not necessary to store it. The pairs can then be reduced to:

- (01010, 5)
- (11110011011, 9)
- (0, -3)

This is how floating point numbers are represented. The mantissa is given a section of storage. The exponent is given another section. One more bit is used to indicate the sign.

There are some special cases. Zero is one of those, as is infinity, and various others. But the basics are these simple pairs.

**Observations**  
 Knowing the representation of these numbers, there are some useful observations that can be made about their properties.

Any integer whose binary representation fits within the mantissa can be precisely represented with no error. For a `double`, this means that any integer up to 2^53, or about 18 quadrillion, can be represented exactly. In a `float`, integers up to 2^24, or a bit under 16.8 million can be represented exactly.

Numbers much larger than this can be represented as well, but with less precision. Only even numbers can be represented when immediately past the above limits. As the numbers grow further, only multiples of 4 can be represented, then multiples of 8, then 16, etc.

Fractions can be represented _if and only if_ they can be expressed as a sum of powers of two. For example, ^3/~4 = ^1/~2 + ^1/~4 = 1.1 × 2^-1 = (1, -1). However, a seemingly simple number such as ^1/~10 cannot be precisely represented in floating point. The best you can do is a close approximation: (10011001100110011..., -4).

To put it differently: every floating point number can be precisely written out as a finite decimal. However, many finite decimals cannot be exactly represented as a floating point number. This is why [you should never use floating point to represent currency](http://c2.com/cgi/wiki?FloatingPointCurrency).

**Literals**  
 When writing floating point constants in code, it's important to be mindful of the semantic difference between integer constants and floating point constants. For example, the following trap is common:

```
    double halfpi = 1/2 * M_PI;
```

The value of `halfpi` is not the expected approximation, but rather zero. This is because both `1` and `2` are integers. The integer division `1/2` produces `0`, and `0 * M_PI` also produces zero.

To fix this, it is necessary to simply place a decimal point on the literals to make them into floats. In a case like this, only one of the numbers needs it, because the other number will be converted to floating point automatically, but it's more clear to just do it with both:

```
    double halfpi = 1.0/2.0 * M_PI;
```

It's best to get into the habit of using `.0` at the end of any integer constant used in a floating point expression to avoid unhappy mistakes like this.

**Accuracy**  
 There are various accuracy requirements placed on arithmetic operations on floating point numbers. In particular, the four basic operations of addition, subtraction, multiplication, and division, are required to produce exactly the correct result if the correct result is representable. If the correct result is not representable, then they must produce the closest possible floating point number to the correct result.

Combine this with the fact that a large range of integers are exactly representable. This means that, as long as the operands and result are within that range, addition, subtraction, and multiplication of integers in floating-point numbers _will be exact_. Division with an integral result will also be exact. In general, you can place integers in floating point numbers and, as long as you know the range of the numbers to be within what's required, you can count on full accuracy and no unpredictability.

This is how Cocoa can use `CGFloat` for graphics coordinates. At first glance it might seem like a bad idea. Pixels are discrete units, floating point is continuous and inaccurate. However, any operation that works on whole pixels will produce exact results and no inaccuracy. Using floating point gives Cocoa additional flexibility to produce good approximate results when not working on whole pixels.

**Comparison**  
 It's commonly said that a C programmer should never use `==` to compare floating point numbers. There's even a gcc warning specifically to catch this: `-Wfloat-equal`. The reason given for this is that floating point inaccuracy means two numbers which _should_ be exactly equal may in fact differ slightly due to rounding errors or other such computational inexactness.

While this is often true and a good rule of thumb to follow, as you can see it is not always the case. It _is_ perfectly reasonable to use `==` on floating point values _as long as you know that the values are completely accurate_. For example, if you're working purely on well-behaved integers, `==` presents no problem:

```
    double x = 1.0 + 2.0 * 3.0;
    double y = (29.0 - 1.0) / 7.0 + 3.0;
    if(x == y)
        // guaranteed to be true
```

However, operations on numbers which cannot be exactly represented will not fare so well:

```
    double one1 = 0.1 * 10.0;
    double one2 = 1.0 / 3.0 * 3.0;
    double one3 = 4.0 * atan(1.0) / M_PI;
    if(one1 == 1.0 || one2 == 1.0 || one3 == 1.0)
        // no guarantee any of these will be true
```

For cases where the calculation is expected to be inexact, it's best to compare for "equality" by checking to see if the two numbers are close together. A simple way to do this is to see if the difference is less than some delta. Deciding on the value for that delta can be tricky, and is often guesswork. Here's a function to perform this comparison:

```
    BOOL FloatAlmostEqual(double x, double y, double delta)
    {
        return fabs(x - y) <= delta;
    }
```

This can be used on less precise values:

```
    double one = 0.1 * 10.0;
    if(FloatAlmostEqual(one, 1.0, 0.0000001))
        // this will be true
```

There are also [more advanced ways](http://www.cygnus-software.com/papers/comparingfloats/comparingfloats.htm) to compare floating point values, although in practice they are generally not necessary.

**Special Numbers**  
 There are a few kinds of special floating point numbers that are useful to understand.

The first is zero. IEEE-754 actually has two zeroes: positive and negative. While they are largely the same, and even compare as equal using `==`, they do behave slightly differently. For example, `1.0 * 0.0` produces positive zero, but `1.0 * -0.0` produces negative zero. The concept of negative zero makes sense when considering floating point values as _approximations_ to some theoretical exact number. Positive zero represents not only the precise quantity of zero, but a small range of extremely small positive numbers that are very close to zero. Likewise, negative zero represents zero and a small range of negative numbers very close to zero.

For the most part, negative zero has few practical consequences and can be ignored. For cases where it needs to be detected, it can be checked using `signbit`:

```
    BOOL IsNegativeZero(double x)
    {
        return x == 0.0 && signbit(x);
    }
```

Next is infinity. Like zero, there are two kinds of infinity: positive and negative. These are produced when a calculation overflows the largest representable number. They are also produced when dividing a non-zero number by zero. Although mathematically such an operation is undefined, not infinite, it again makes sense when thinking of a floating point zero as an approximate, not exact, zero.

Infinity can be written in code by writing the `INFINITY` macro. It can be detected with `isinf(x)`. For the most part, floating point infinities behave the way you would expect them to. Adding or subtracting a finite number produces infinity. Multiplying or dividing by a positive number produces infinity, and a negative number switches the sign. Dividing a finite number by infinity produces zero.

Finally, there is Not a Number, or NaN. This represents the mathematical concept of "undefined", or at least a result which can't be represented as a real number. NaN is produced by operations such as taking the square root of -1, calculating `0.0/0.0`, or `INFINITY - INFINITY`.

NaNs have several unusual behaviors. Perhaps the most surprising is that NaN is not equal to anything, _not even itself_. The expression `x == x` will be false if x is a NaN. NaNs also propagate through calculations. Any floating point operation where one operand is a NaN will produce NaN as the result. This means that code can do a single check for NaN at the end of a long calculation, rather than having to check after each operation that could potentially produce one.

NaN can be written in code with the `NAN` macro, and can be detected using `isnan`. They can also be detected using `x != x`, but this is not recommended as some compilers get a little too clever while optimizing and will make that expression always be false.

**Math Functions**  
 There are a ton of useful math functions in the `math.h` header. Each function comes in two variants. The plain function, for example `sin`, takes a `double` and returns a `double` with the result. Functions which end in `f`, for example `sinf`, do the same except they operate on `float`. This makes them a bit faster when your values are all `float`. There are a few categories of functions worth mentioning:

- **Trigonometric functions:**`sin`, `cos`, `tan`, and others are all provided. These are, of course, useful for all kinds of geometric calculations.
- **Exponential functions:**`exp` calculates powers of the mathematical constant `e`, and `log` calculates natural logarithms. Other functions are available to calculate powers of two and logarithms in other bases.
- **Powers:** the `pow` function will calculate arbitrary exponents. The `sqrt` function is specifically optimized to take square roots.
- **Integer conversion:** various functions to get a nearby integer from a floating point number, such as `ceil`, `floor`, `trunc`, `round`, and `rint`.
- **Specialized floating point functions:** many functions which provide better performance or accuracy, or additional capabilities by taking advantage of the nature of floating point, such as `fma` (performs a multiply and an add), `log1p` (calculates the function `log(1 + x)`), and `hypot`.

There are also a bunch of useful constants defined in this header, such as `M_E` (the mathematical constant `e`) and `M_PI` (π).

**Further Reading**  
 Mac OS X ships with some good documentation on floating point numbers. `man float` discusses their general representation and behavior. `man math` discusses the various functions in `math.h`. Most of those functions also have their own man page which goes into more detail.

Finally, the classic [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://web.archive.org/web/20080527204528/http://docs.sun.com/source/806-3568/ncg_goldberg.html) is a somewhat difficult but extremely useful read to anyone who really wants to understand just how all of this stuff works and what consequences it has.

**Conclusion**  
 Floating point arithmetic can be strange, but if you understand the basics of how it works, it's nothing to be afraid of and can be extremely useful. Floating point can be great for physics, graphics, and even just internal bookkeeping. It's important to always be mindful of accuracy and other limits, but within those limits there's much that it's good for.

That's it for this time. Come back again in two weeks for another exciting edition. If you get bored while waiting, why not [send me a topic suggestion](mailto:mike@mikeash.com)?

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-01-04-practical-floating-point.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
