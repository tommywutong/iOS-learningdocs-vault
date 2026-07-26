---
title: 'Random number generators in Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/05/19/random-numbers.html'
original_language: en
published: 2016-05-19
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:547b83eba962c860'
translated: false
---

> 原文：[Random number generators in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/05/19/random-numbers.html)　·　Cocoa with Love (Matt Gallagher)

What’s the best general purpose random number generating algorithm available?

In this article I’ll present 8 different implementations of the Swift `RandomNumberGenerator` protocol. Implementations will include wrappers around Mac/iOS built-in algorithms, my own implementations in Swift of some popular algorithms and some corresponding C implementations for comparison. The implementations can all seed themselves from /dev/urandom, can generate data of arbitrary size (although I’ll focus on 64-bit integer generation) and offer conversion to `Double` (preserving up to 52-bits of randomness in the significand).

As an aside, my Swift implementation of the Mersenne Twister ended up 20% faster than the official [mt19937-64.c](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/VERSIONS/C-LANG/mt19937-64.c) implementation. Curious to understand what I had done, I ended up “fixing” the C version to be just as fast as the Swift version. Yes, it’s true: with a little tuning, C can be just as fast as Swift.

Welcome to C with love.

## Use case

My primary use for random numbers is in fuzz testing; deliberately sending mixed, garbled or simply “random” inputs to my functions (to look for data handling errors) or running large numbers of threads with different timing offsets and data sizes (to look for timing or thread-safety bugs).

It’s difficult to know exactly what performance or quality I require from random numbers in this scenario – most “good quality” options would probably suffice – but what I do require is:

- no shared global data (since I run multiple tests in parallel)
- the ability to set the initial seed (since I want to reproduce bugs when I find them)

Historically, I’ve used a C implementation of the Mersenne Twister. I don’t have any particular problems with it but the algorithm is nearing its 20th birthday so I was curious to see what else was around.

## Built-in sources of randomness on Mac and iOS

The C standard library on the Mac and iOS contains a few different functions for random number generation:

1. `rand()`
2. `random()`
3. `[d|e|j|l|m]rand48()` et al
4. `arc4random()`
5. /dev/[u]random

In iOS 10, macOS 10.12 and later, the first 3 are all “unavailable” in Swift, leaving us with just `arc4random()` and /dev/urandom as default sources of random numbers in Swift.

### /dev/urandom

If you need cryptographically secure random numbers, the _only_ option you should consider is /dev/[u]random.

On Mac and iOS, both /dev/random and /dev/urandom are identical and use the [Yarrow algorithm](https://en.wikipedia.org/wiki/Yarrow_algorithm) in conjunction with bits accumulated from hardware entropy sources. The existence of two different names is largely for cross-compatibility with Linux where the different devices have historically had a complicated range of distinct security considerations with general advice leaning towards /dev/urandom. I’ve used /dev/urandom to minimize portability problems.

The problem is that reading from /dev/urandom is slow. In my testing, it is between 100 and 1000 times slower than other generators and uses additional system resources on top of the userspace resources of typical random number generators.

The end result is that /dev/urandom, while useful for initializing initial seed values, is a poor choice for a general-use random number generator.

### The “allegedly” RC4 generator

The only “general purpose” random number generator available by default in Swift is `arc4random`. It is generally high quality but it is slow due to the use of large amounts of state, locks on the global data and periodic mixing of additional entropy from /dev/urandom.

Like /dev/urandom, `arc4random` can’t be seeded, so you can’t regenerate previous sequences. This means that, while useful for _random_ generation, it is harder to test and less useful for dynamically generated content, distributions or modelling.

The “arc4” in the name was originally because the algorithm was [“allegedly” compatible with the RC4 algorithm](https://en.wikipedia.org/wiki/RC4) developed by RSA Labs. However, since macOS 10.12 Sierra, the implementation uses the unrelated NIST-approved AES cipher and the man page suggest you consider the acronym to represent “a replacement call for random”.

`arc4random` provides good quality but is about 5 times slower than pseudorandom algorithms of equivalent statistical quality (if you don’t truly need security). Problematic for testing purposes is that `arc4random` uses global state and can’t be directly seeded for debugging purposes or other situations requiring repeatability.

## Other general-purpose random number generators

I’m going to look at some high quality, simple, fast random number generators, implement them in Swift and see how they compare.

### Linear feedback shift register

Most pseudo-random algorithms are collections of shift and XOR operations. Some of the oldest are the linear-feedback shift register (LFSR) algorithms. [Wikipedia has a very clear animated GIF](https://en.wikipedia.org/wiki/Linear-feedback_shift_register) of the operation generating a random sequence from a 4-bit number.

By carefully selecting the feedback points, the shift amounts and combining multiple registers, you can get very long cycles, good distribution and low predicatability. Researcher Pierre L’Ecuyer gives some tables of values for “Tausworthe” style linear-feedback shift register generators in his paper [Tables of Maximally-Equidistributed Combined LFSR Generators](http://www.iro.umontreal.ca/~lecuyer/myftp/papers/tausme2.ps).

In the code I present as part of this article, I give two variants, `Lfsr176` and `Lfsr258` – with periods approximately equal to 2176 and 2258 respectively.

### Mersenne Twister

The [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) was a huge advancement when it was introduced by M Matsumoto and T Nishimura in 1997 and it remains the random generator that newer non-cryptographic generators are compared against (the algorithm isn’t cryptographic because you can observe just 624 values and from that point, predict the sequence).

So the Mersenne Twister fails the “unpredictable” test but it is well tested, has a good distribution, very long period and is fairly fast. But there are some caveats.

In a tight loop, the Mersenne Twister is within a factor of 2 of the fastest algorithms tested. However, the standard Mersenne Twister uses 2496 bytes of internal storage. That might not seem like a lot of space on a modern computer but it is big enough to put additional burden on your L1 cache.

On the quality front: the Mersenne Twister has some known problems with entering “zero” states (situations where its internal state contains a large number of zeros and the generator gets “stuck”).

### Xoshiro256**

A number of algorithms have been proposed and tested in the last few years: PCG, LCG 64, XorShift 64, RanQ and others. The last couple generations have relied on automated statistical quality tests to experiment with different variations on themes to find heavily refined versions of their respective approaches.

The latest release from Sebastiano Vigna (in collaboration with David Blackman) is [Xoshiro256**](http://xoshiro.di.unimi.it/xoshiro256starstar.c) – a specialized linear-feedback shift register. Xoshiro claims to be the fastest algorithm to fare well on the [TestU01](http://www.iro.umontreal.ca/~simardr/testu01/tu01.html) set of quality tests for random number generators and [claims to provide a better statistical distribution](http://xoshiro.di.unimi.it) on the [PracRand](http://pracrand.sourceforge.net) tests than previous xorshift and xoroshiro algorithms.

While the period of the generator is fairly low (2256), it’s easily high enough for any common purpose.

## Implementations

Swift’s `RandomNumberGenerator` protocol requires at least a `mutating func next() -> UInt64`

> NOTE: in an earlier version of this code I implemented my own `Double` generation. Since Swift 4.2, this is offered by default as `Double.random(in:, using:)` so I’ve removed these functions from my own code.

The implementations are:

- `Arc4Random` – 64 bit integers generated with `arc4random_buf`
- `DevRandom` – data read from /dev/urandom
- `Lfsr176` – a 3 register linear-feedback shift register with period

  2176
- `Lfsr258` – a 5 register linear-feedback shift register with period

  2258
- `MersenneTwister` – a Swift implementation of MT19937_64
- `MT19937_64` – the Mersenne Twister as generated by [mt19937-64.c](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/VERSIONS/C-LANG/mt19937-64.c) by Takuji Nishimura and Makoto Matsumoto.
- `Xoshiro` – 64-bit integers generated by this custom xor/shift generator
- `Xoshiro256**` – the [original C implementation of `Xoshiro256**`](http://xoshiro.di.unimi.it/xoshiro256starstar.c) by David Blackman and Sebastiano Vigna

and

- `ConstantNonRandom` – baseline that returns a constant 64-bit number

## Performance

All algorithms were used to generate 100 million 64-bit `UInt64` values. These are the timing results:

|  | Seconds (Swift 3, MacPro4,1) | Seconds (Swift 4.2, MacBookPro15,1) |
|---|---|---|
| `DevRandom` | 113.250 | 102.0 |
| `Arc4Random` | 4.359 | 16.76 |
| `Lfsr258` | 0.717 | 0.359 |
| `MT19937_64` | 0.640 | 0.368 |
| `MersenneTwister` | 0.533 | 0.303 |
| `Lfsr176` | 0.498 | 0.256 |
| `xoshiro256**` | (0.352) | 0.246 |
| `Xoshiro` | (0.347) | 0.244 |
| `ConstantNonRandom` | 0.211 | 0.104 |

<sub>Time taken to generate 100 million 64-bit values</sub>

> **Update note**: the tests in parentheses were using an older xoroshiro128 algorithm and are not directly comparable with the newer xoshiro256 algorithm.

I carefully set the target’s build settings to “incremental” (not whole module optimization) so I could carefully ensure that all algorithms had to go through exactly one interface boundary. The `ConstantNonRandom` test is intended to measure this overhead.

These numbers show the Swift version of `Xoshiro` faster than `xoshiro256** ` but from run to run, they trade places. Any difference between them is within the margin of error of this test setup.

## MersenneTwister in C versus Swift

So the Swift implementation of MersenneTwister ended up 20% faster than the [mt19937-64.c](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/VERSIONS/C-LANG/mt19937-64.c) C implementation. Hooray, Swift is the fastest!

### Why?

The Mersenne Twister is made up of two parts:

1. The “xor-shift-mask” steps performed on every iteration
2. The “twist” steps performed every 312 iterations

The “xor-shift-mask” has very little wiggle room. Here’s the C implementation:

````c
x = ctx->state[ctx->index++];
x ^= (x >> 29) & 0x5555555555555555ULL;
x ^= (x << 17) & 0x71D67FFFEDA60000ULL;
x ^= (x << 37) & 0xFFF7EEE000000000ULL;
x ^= (x >> 43);
return x;
```cw

There is a minor performance issue with this code but there's no *significant* room for refactoring here. The real difference between my Swift code and the C is in the "twist" steps.

A simple Swift implementation of "twist" would look like this:
    
```swift
for i in 0..<stateCount {
   let x = (state[i] & upperMask) | (state[(i + 1) % stateCount] & lowerMask)
   int xA = (x & 1 == 0) ? (x >> 1) : ((x >> 1) ^ 0xB5026F5AA96619E9)
   state[i] = state[(i + (stateCount / 2)) % stateCount] ^ xA
}
````

This code would work but unfortunately, `%` is not a fast operation and at 100 million per second speeds, the ternary conditional operator `?:` is also too slow (don’t worry about the `stateCount / 2` part, that’s a constant and is optimized away). Avoiding these requires restructuring the loop so that they’re not required.

The mt19937-64.c implementation breaks the loop apart into two halves and follows up with an epilogue to handle the final position:

```c
for (i = 0; i < (stateCount / 2); i++) {
   x = (ctx->state[i] & upperMask) | (ctx->state[i + 1] & lowerMask);
   ctx->state[i] = ctx->state[i + (stateCount / 2)] ^ (x >> 1) ^ mag01[x & 1];
}
for (; i < stateCount - 1; i++) {
   x = (ctx->state[i] & upperMask) | (ctx->state[i + 1] & lowerMask);
   ctx->state[i] = ctx->state[i - (stateCount / 2)] ^ (x >> 1) ^ mag01[x & 1];
}
x = (ctx->state[stateCount - 1] & upperMask) | (ctx->state[0] & lowerMask);
ctx->state[stateCount - 1] = ctx->state[(stateCount / 2) - 1] ^ (x >> 1) ^ mag01[x & 1];
```

_(I’ve renamed the variables and reformatted this to look more like my Swift code, to aid comparison.)_

This code contains no division or modulo (remember: the `stateCount / 2` is a constant and optimized away) and no conditionals or ternary operators (except the loops themselves). But there’s a weird `mag01` array (which is `0` at index 0 and `0xB5026F5AA96619E9` at index 1) and worse: the `ctx->state` is fully iterated multiple times since the `ctx->state[i + (stateCount / 2)]` and `ctx->state[i - (stateCount / 2)]` accesses each walk the values from the _other_ loop.

I took a different approach to optimize the “twist” code for my implementation. My code walks both halves of the loop simultaneously, using two different indexes, offset by `stateCount / 2`:

```swift
let (a, mid, stateMid) = (0xB5026F5AA96619E9, stateCount / 2, state[stateCount / 2])
var (i, j) = (0, mid)
repeat {
   let x1 = (state[i] & upperMask) | (state[i &+ 1] & lowerMask)
   state[i] = state[i &+ mid] ^ (x1 >> 1) ^ ((state[i &+ 1] & 1) &* a)
   let x2 = (state[j] & upperMask) | (state[j &+ 1] & lowerMask)
   state[j] = state[j &- mid] ^ (x2 >> 1) ^ ((state[j &+ 1] & 1) &* a)
   (i, j) = (i &+ 1, j &+ 1)
} while i != mid &- 1

let x3 = (state[mid &- 1] & upperMask) | (stateMid & lowerMask)
state[mid &- 1] = state[stateCount &- 1] ^ (x3 >> 1) ^ ((stateMid & 1) &* a)
let x4 = (state[stateCount &- 1] & upperMask) | (state[0] & lowerMask)
state[stateCount &- 1] = state[mid &- 1] ^ (x4 >> 1) ^ ((state[0] & 1) &* a)
```

The epilogue needs to handle _two_ indexes but the `state` array is only traversed once, we’re hitting _half_ as many loop conditions and a simple multiply by `0` or `1` (optimized to bitwise arithmetic) is used to eliminate the ternary operator conditional.

If there were no other elements at play, this alone would improve performance 7% versus the mt19937-64.c implementation.

But there’s another advantage: with these two iterations (using the `i` index and the `j` index) side-by-side in the same loop, _the compiler can automatically optimize to SIMD instructions_ to give us an extra 10% boost.

There’s another 3% performance difference but to understand that, we’ll need to make the C and Swift code more similar.

### What happens if the C code does the same thing?

Swift is faster but it’s not an apples-to-apples comparison. Is it possible to make a true comparison? Where both C and Swift follow the same logic?

Let’s try changing the C code to:

```c
for (i = 0, j = mid; i != mid - 1; i++, j++) {
   x = (ctx->state[i] & upperMask) | (ctx->state[i + 1] & lowerMask);
   ctx->state[i] = ctx->state[i + mid] ^ (x >> 1) ^ ((ctx->state[i + 1] & 1) * a);
   y = (ctx->state[j] & upperMask) | (ctx->state[j + 1] & lowerMask);
   ctx->state[j] = ctx->state[j - mid] ^ (y >> 1) ^ ((ctx->state[j + 1] & 1) * a);
}
x = (ctx->state[mid - 1] & upperMask) | (stateMid & lowerMask);
ctx->state[mid - 1] = ctx->state[stateCount - 1] ^ (x >> 1) ^ ((stateMid & 1) * a);
y = (ctx->state[stateCount - 1] & upperMask) | (ctx->state[0] & lowerMask);
ctx->state[stateCount - 1] = ctx->state[mid - 1] ^ (y >> 1) ^ ((ctx->state[0] & 1) * a);
```

As expected, this brings the C to within 3% of Swift.

So what’s the cause of the remaining difference?

At this point, the only differences are a few `int` types in C that are `Int` in Swift. We need to move the C code to a more consistent 64-bit everywhere with `unsigned long long` instead of `int`.

The remaining difference? The use of the postincrement operator I showed in the first line of the C “xor-shift-mask” code. We need to change:

```c
x = ctx->state[ctx->index++];
```

to

```c
x = ctx->state[ctx->index];
ctx->index = ctx->index + 1;
```

It might seem like this shouldn’t make any difference but it does affect the generated assembly and appears to result in a 1-2% difference.

Both the C and Swift are now the same. I don’t just mean “they take the same time”, I mean **they are compiled to literally the same instructions**. You can open the generated assembly in each case and they are _identical_.

Hooray, C is also the fastest!

## Usage

> The project containing these `RandomNumberGenerator` implementations is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

The [CwlRandom.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlRandom.swift?ts=3) file is fully self-contained so you can just copy the file, if that’s all you need.

Otherwise, the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) contains detailed information on cloning the whole repository and adding the framework it produces to your own projects.

The [mt19937-64.c in the repository](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/ReferenceRandomGenerators/mt19937-64.c) file contains my changes to the Takuji Nishimura and Makoto Matsumoto mt19937-64.c file, with a `#if/#else/#endif` to switch between my implementation and the original. You’re welcome to use this in your own C projects, if desired.

> **License note**: the [mt19937-64.c file](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/ReferenceRandomGenerators/mt19937-64.c) is “Copyright (C) 2004, Makoto Matsumoto and Takuji Nishimura” and contains its own BSD 3-clause license however, this file is _not_ built into the CwlUtils.framework, it is used only by the testing bundle for validation and performance testing.

## Conclusion

If you’re after high performance, Xoshiro is probably the best general purpose algorithm currently available. Low memory (just 256 bits of storage), high performance (1.45 nanoseconds per 64-bit number, after subtracting test overheads) and well distributed (beating other algorithms on a range of automated tests).

However, the difference doesn’t mean much unless you need a _lot_ of random numbers. For most applications, 2, or even 10 times slower random numbers is not a big problem. Mersenne Twister might still be a better choice for highly conservative projects unwilling to switch to newer algorithms, but the current generation of statistically tested algorithms brings a baseline of assurance from the outset that previous generations lacked.

Of course, if you only need a few random numbers in your program and you don’t really care about multithreading or repeatability then these alternative algorithms are unnecessary – there’s no problem with the built-in `arc4random` or even reading from /dev/urandom (you could generate hundreds of numbers from /dev/urandom per second without overheads reaching 1%).

Getting C-level performance in Swift for numerical algorithms is quirky but not particularly difficult. If you limit yourself to value types (no classes or existentials), use unsafe pointers and tuples instead of arrays, use overflow discarding operators `&+`/`&-`/`&*` instead of normal `+`/`-`/`*`, use `while` or `repeat/while` for your loops, then Swift and clang C will generally compile to identical instructions.

It’s not as though C is maximally performant without a little contortion. Using `int` types for indexes on 64-bit systems should be avoided and so should common idioms like inline use of the `++` postincrement operator.
