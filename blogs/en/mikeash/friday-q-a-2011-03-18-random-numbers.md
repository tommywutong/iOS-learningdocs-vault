---
title: 'Friday Q&A 2011-03-18: Random Numbers'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-03-18-random-numbers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:21406647247a6c9c'
translated: false
---

> 原文：[Friday Q&A 2011-03-18: Random Numbers](https://www.mikeash.com/pyblog/friday-qa-2011-03-18-random-numbers.html)　·　mikeash.com Friday Q&A

Posted at 2011-03-18 16:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-04-01: Signal Handling](https://www.mikeash.com/pyblog/friday-qa-2011-04-01-signal-handling.html)  
Previous article: [See Me Speak at Voices That Matter in Seattle](https://www.mikeash.com/pyblog/see-me-speak-at-voices-that-matter-in-seattle.html)  
Tags: [cryptography](https://www.mikeash.com/pyblog/?tag=cryptography) [friday](https://www.mikeash.com/pyblog/?tag=friday) [qna](https://www.mikeash.com/pyblog/?tag=qna) [random](https://www.mikeash.com/pyblog/?tag=random)

Friday Q&A 2011-03-18: Random Numbers

by [Mike Ash](https://www.mikeash.com/)

**Introduction**  
 When talking about random numbers in computer programs, what we usually mean is _pseudorandom_ numbers. Computers have a hard time being truly random. Give the same program the same input and you'll get the same output. A pseudorandom number is one which is difficult to predict if you don't know the initial input, but which is still intrinsically deterministic.

Not all computer random numbers are pseudorandom. There are sources of truly random numbers available to computers. Sometimes it's specialized hardware, like reading thermal noise in an electrical circuit. Sometimes it's unpredictable external events, like hard disk head movement or keystroke timing. In this article, I will cover both types.

When generating random numbers, there are a few different aspects to consider. An obvious one is speed. Some methods for generating random numbers are much faster than others. Somewhat less obvious is simplicity. A solution which requires a huge amount of code isn't going to see much use.

Often highly important, but somewhat harder to evaluate, is the _quality_ of random numbers. Some generators have highly predictable output. Some have highly unpredictable output, and some are somewhere in between.

**Quality**  
 There is a classic joke where a random number generator is implemented like so:

```
    int RandomNumber(void)
    {
        return 3;
    }
```

While silly, it's also interesting to consider. Theoretically, is this function truly wrong? After all, if you were to roll a die, it's

, although increasingly unlikely, to roll a 3 every time. In practice, of course, such a thing is entirely useless.

However, it's a good starting point to consider the notion of random number quality. On one end, you have constants, like the above 3. On the other end, you generate a sequence of numbers which even an extremely clever adversary with enormous resources at his disposal could not predict.

There's a huge range in between. Sometimes your adversary isn't some sinister organization, but just a guy playing cards. Sometimes you need random numbers only good enough to fool a casual observer. Sometimes you need random numbers which are reasonably unpredictable but which wouldn't be impossible to reverse engineer.

These needs can be broken down into a few categories:

1. A need for the basic appearance of unpredictability but doesn't need to stand up to scrutiny. An example might be a simulation of a flickering light, or a randomly bouncing ball.
2. Difficult for a human observer to predict even if he's paying attention and making the attempt. An example for this might be a casual card game.
3. Cryptographic quality randomness, where the sequence cannot be predicted even by a motivated adversary with enormous resources. This is what you want when practicing cryptography.

There are a wealth of random number APIs available on OS X. I will present a few commonly useful ones here.

**`rand()`**  
 Perhaps the oldest of these APIs is the standard library call `rand()`. At this point it's mostly a historical curiosity and there's little reason to use it, but I'll discuss it for tradition's sake if nothing else.

The quality of the random numbers produced by `rand()` is poor. The sequences are highly predictable and not very useful. This function can be useful for situations which need only the lowest quality of random numbers, but even then you might as well use something a bit better.

The numbers returned by `rand()` are based on a seed value which is stored as a global. To ensure that you don't get an identical sequence every time you run your program, it's necessary to initialize that seed value with something less predictable. This is a common theme with any pseudorandom number generator. Some initial source of true randomness must be provided in order to have any unpredictability.

The traditional way to seed `rand()` is to initialize the seed using the current time:

```
    srand(time(0));
```

This ensures that different invocations of the program have different seeds... provided that they are started at least one second apart!

Another way to initialize the seed is with `sranddev()`. This pulls from the OS's pool of true randomness to initialize the seed, which I'll discuss in a bit.

Relying on global state is generally considered to be bad. There's a companion function, `rand_r()`, which allows you to provide your own state storage.

However, as I mentioned above, there's little reason to use any of these.

**`random()`**  
 This is an improved version of `rand()`. It's considerably less predictable, and would generally be suitable for casual card games and other situations where you want your randomness to stand up to some scrutiny by the user. As with `rand()`, it needs to be initialized to produce an unpredictable sequence, and the best way to do that here is using `srandomdev()`.

Unfortunately, there is no variant of this function which doesn't use global state, which makes it somewhat dangerous to use. Another downside is that it's slightly slower than `rand()`, although this is unlikely to matter in most applications.

**`jrand48()`**  
 This is a decent random number generator which also uses user-supplied state. Its state is an array of 3 `unsigned short`s. To initialize its state, dump random data into that array. Like `random()`, it's good enough to stand up under casual scrutiny, but no more.

**`/dev/random`**  
 We finally arrive at the big gun of randomness. This is not a function, but rather a device file provided by the OS. You can open and read from it like any other file. The data read from it is good, cryptographic-quality randomness. Because it's implemented as a file and any read from it will have to go into the kernel, this is considerably slower to use than random number generation functions. Whether that matters or not will, of course, depend on the individual situation.

It is implemented by taking advantage of external (and possibly internal) sources of random data, such as keyboard input timings. This random data is then mixed together using the [Yarrow algorithm](http://en.wikipedia.org/wiki/Yarrow_algorithm) which then produces the actual output data. Due to this, it is extremely difficult for an adversary to predict the output.

Since it's just a file, there are numerous ways to obtain data from it. A convenient way to obtain a fixed-size chunk of data is to use `NSFileHandle`:

```
    NSData *randomChunk = [[NSFileHandle fileHandleForReadingAtPath: @"/dev/random"] readDataOfLength: 20];
```

This is handy for quickly generating unique identifiers or encryption keys. If you need a lot of random data then it would be a good idea to open the file once and then read data on demand, but for simple one-offs, the above can be nice.

Note that opening that file is not guaranteed to succeed, so if you use that approach, be prepared for the data to end up `nil`. Depending on how important the quality of randomness is, you might fall back to a weaker random number generator, or you might simply abort the operation.

For those coming from Linux, a word of caution. On Linux, there are two random devices: `/dev/random` and `/dev/urandom`. `/dev/random` is a blocking interface that only returns as much random data as the system possesses at any particular time. Once the system runs out of randomness, no more can be fetched until more is generated (by listening to the user bang on the keyboard, or however the OS gathers true randomness). `/dev/urandom` is a non-blocking interface that always returns the requested amount of data, by using a pseudorandom generator even when true randomness is exhausted.

OS X has both of these as well, however they both act like `/dev/urandom` does on Linux. If you need a source of nothing but true randomness, I'm afraid you're out of luck. The good news is that the `/dev/random` pseudorandom generator should be good enough for pretty much any purpose.

**Range Limiting**  
 These functions return numbers in different ranges. `random()` returns numbers in the range of [0, 231-1]. `/dev/random` returns an arbitrary number of bytes, which means it can be used to fill the full range of any data type.

Frequently, you want random numbers in a smaller range. For example, you may want to choose a random element in an array, and for this you would need a random number in the range [0, `[array count]` - 1]. To do this, you need a way to cut down the range that comes out of the random number generator.

The simplest and perhaps oldest way to accomplish this is to use the mod operator, like so:

```
    int randomIndex = random() % [array count];
```

This works and is often good enough. However, it's flawed, because in most cases it doesn't provide a completely uniform distribution of random indices, even if

itself is completely uniformly distributed. The problem comes when the size of the range of random numbers is not evenly divisible by

. In this case, there are 2

possible random numbers, which means that if

is not a power of two, the result will not be uniformly distributed.

To illustrate, let's take a somewhat absurd case and imagine that `[array count]` is `1431655765`. (This value is 2/3 of 231, which is why I chose it specifically.) The random number generator then works out to:

```
    random() % 1431655765
```

There are now two cases to consider.

If `random()` returns a number in the range [0, 1431655764], that same number is used as the random index. If `random()` returns a number in the range [1431655765, 231 - 1], then the random index is equal to the number returned minus 1431655765. The result will lie in the range [0, 715827883], which is roughly the first half of the array.

This is a major problem! Our "random" index is twice as likely to fall within the first half of the array as the second half. As the desired range shrinks, this problem likewise shrinks, but it still exists for any desired range which can't evenly divide the original range.

The solution to this is to use as much as possible of the original range, and discard the number and try a new one if it falls outside what's usable.

The largest possible range is [0, M - 1], where M is the largest number less than 231 which is divisible by the target maximum. This number can be found with a bit of simple integer arithmetic. Once M is known, an uniform distribution of random numbers can be generated:

```
    int count = [array count];
    
    unsigned two31 = 1U << 31;
    unsigned maxUsable = (two31 / count) * count;
    
    int randomIndex = -1;
    while(randomIndex == -1)
    {
        unsigned num = random();
        if(num < maxUsable)
            randomIndex = num % count;
    }
```

Of course, better would be to write a function that handles the grunt work for us:

```
    int RandomUnder(int topPlusOne)
    {
        unsigned two31 = 1U << 31;
        unsigned maxUsable = (two31 / topPlusOne) * topPlusOne;
        
        while(1)
        {
            unsigned num = random();
            if(num < maxUsable)
                return num % topPlusOne;
        }
    }
```

This can then be used to easily generate our random index, or anything else:

```
    int randomIndex = RandomUnder([array count]);
```

The use of a loop which only terminates when a random number meets a certain condition might make you nervous. However, don't fret. In the worst case, slightly over 50% of the random numbers will terminate the loop. The chances of the loop going over 10 iterations is therefore less than 0.1%, and the chances of the loop going over 20 iterations is less than one in a million. In more common cases, the number of cases which cause the loop to repeat will be a small fraction of the overall range, and so even single repeats will be rare.

This returns a number in the range [0, X - 1] for some arbitrary X. This is usually good, but sometimes you want a range which starts at a different value. This is easy to accomplish. First, generate a zero-based random number with the appropriate maximum, then just shift it up:

```
    int RandomInRange(int bottom, int top)
    {
        int rangeSize = top - bottom;
        int zeroBased = RandomUnder(rangeSize);
        return zeroBased + bottom;
    }
```

Sometimes you need a random floating-point number rather than a random integer. To create a floating-point number with an uniform distribution, it's a simple bit of arithmetic from an uniform distribution of integers. For example, to generate a random number in the range [0.0, 1.0], just divide by the maximum integer value, being sure to carry out the calculation in floating point:

```
    double random01 = random() / (double)0x7fffffff;
```

Many other useful distributions of random floating-point numbers exist, but they are beyond the scope of this article. Uniform distributions are, in my experience, the most commonly useful to most programmers.

**Conclusion**  
 That wraps things up for today. I hope that you now know a little more about generating random numbers than you did before. For many common cases, the `random()` function is good enough. The `/dev/random` file is great for cases where you need something really robust.

Come back in two weeks for another frabulous Friday Q&A. As always, Friday Q&A is driven by reader suggestions, so in the meantime please keep [sending me](mailto:mike@mikeash.com) your suggestions for topics to cover.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
