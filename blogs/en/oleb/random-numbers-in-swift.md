---
title: Random numbers in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/06/random-numbers-in-swift/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:3b973aa819ac8196'
translated: false
---

> 原文：[Random numbers in Swift](https://oleb.net/blog/2018/06/random-numbers-in-swift/)　·　Ole Begemann

# Random numbers in Swift

Working with random numbers in Swift used to be a bit of pain because there was no native random number API. Developers had to fall back on C APIs provided by the operating system, which are often easy to misuse. Moreover, the preferred random number API differs between platforms (e.g. [`arc4random`](https://man.openbsd.org/arc4random.3) vs. [`rand`](http://en.cppreference.com/w/c/numeric/random/rand) vs. [`random`](http://man7.org/linux/man-pages/man3/random.3.html)), making it difficult to write cross-platform code.

Swift 4.2 makes this much easier by including a native and fairly full-featured random number API in the standard library. You can read about the full API and its design rationale in [Swift Evolution proposal SE-0202](https://github.com/apple/swift-evolution/blob/master/proposals/0202-random-unification.md)).

# Generating random numbers

Let’s look at some usage examples. All number types have a static [`random(in:)`](https://developer.apple.com/documentation/swift/fixedwidthinteger/2995514-random) method that takes a [`Range`](https://developer.apple.com/documentation/swift/range) (or [`ClosedRange`](https://developer.apple.com/documentation/swift/closedrange)) and returns a random number in the given range (with a uniform distribution):

```
Int.random(in: 1...1000) // → 691
Double.random(in: 0..<1) // → 0.8741555749903935
UInt32.random(in: 0xD800...0xDFFF) // → 55666
```

## Modulo bias

Note that there’s no `random()` method that doesn’t take a range argument. This was a deliberate decision so as to protect users from a common error called [modulo bias](https://www.quora.com/What-is-modulo-bias). If there were such an API, you might be tempted to use modulo division to generate a random number in a given range. For example:

```
// Wrong! ❌
let between0And5 = UInt8.random() % 6
```

This would indeed produce a number between 0 and 5 (inclusive), but the random results are no longer uniformly distributed! The Swift API nicely leads you to the correct solution:

```
// Correct ✅
let between0And5 = UInt8.random(in: 0..<6) // → 5
```

If you need a random number over the full range of a type, pass `.min ... .max` as the range argument:

```
let between0And255 = UInt8.random(in: .min ... .max) // → 163
```

# Random booleans

[`Bool.random()`](https://developer.apple.com/documentation/swift/bool/2994861-random) is also a thing. Here’s a small function that performs a number of coin tosses and returns the number of heads and tails:

```
func coinToss(count tossCount: Int) -> (heads: Int, tails: Int) {
    var tally = (heads: 0, tails: 0)
    for _ in 0..<tossCount {
        let isHeads = Bool.random()
        if isHeads {
            tally.heads += 1
        } else {
            tally.tails += 1
        }
    }
    return tally
}

let (heads, tails) = coinToss(count: 100)
// → (heads 54, tails 46)
```

# Random collection elements

[Collections](https://developer.apple.com/documentation/swift/collection) have a [`randomElement()`](https://developer.apple.com/documentation/swift/collection/2995109-randomelement) method that returns a random element from the collection. The return type is an [`Optional`](https://developer.apple.com/documentation/swift/optional) because the collection could be empty (just like [`min`](https://developer.apple.com/documentation/swift/sequence/1641174-min) and [`max`](https://developer.apple.com/documentation/swift/sequence/1641492-max)):

```
let emptyRange = 10..<10
emptyRange.isEmpty // → true
emptyRange.randomElement() // → nil
```

Here’s an example that picks a random character from a string:

```
let emotions = "😀😂😊😍🤪😎😩😭😡"
let randomEmotion = emotions.randomElement()! // → "🤪"
```

# Shuffling

Use the [`shuffled()`](https://developer.apple.com/documentation/swift/sequence/2996816-shuffled) method to shuffle a [sequence](https://developer.apple.com/documentation/swift/sequence) or collection:

```
(1...10).shuffled() // → [10, 3, 8, 1, 4, 6, 2, 7, 9, 5]
```

There’s also a mutating variant named [`shuffle()`](https://developer.apple.com/documentation/swift/mutablecollection/2996411-shuffle) for shuffling a collection in place. It’s defined for types that conform to both [`MutableCollection`](https://developer.apple.com/documentation/swift/mutablecollection) and [`RandomAccessCollection`](https://developer.apple.com/documentation/swift/randomaccesscollection):

```
var numbers = Array(1...10)
numbers.shuffle()
// → numbers is now [3, 10, 7, 4, 6, 9, 2, 5, 8, 1]
```

# Random number generators

## The default RNG

All examples above implicitly use the default random number generator (RNG) that ships with the standard library, which is named [`SystemRandomNumberGenerator`](https://developer.apple.com/documentation/swift/systemrandomnumbergenerator).

[SE-0202](https://github.com/apple/swift-evolution/blob/master/proposals/0202-random-unification.md) doesn’t prescribe a particular RNG, but it [lists some desired characteristics](https://github.com/apple/swift-evolution/blob/master/proposals/0202-random-unification.md#random-number-generator) of a good default RNG:

> The aspiration is that this RNG should be cryptographically secure, provide reasonable performance, and should be thread safe. If a vendor is unable to provide these goals, they should document it clearly. … if an RNG on a platform has the possibility of failing, then it must fail [i.e. trap] when it is unable to complete its operation.

Trapping in the (extremely rare, if at all possible) event of failure was preferred over an API where every single function that generated a random value would have to be throwing or return an `Optional`. Such an API would either be extremely inconvenient to use or just lead to users littering their code with force-unwraps for no gain.

The concrete algorithm the default RNG uses can differ between platforms and Swift releases. [The documentation](https://developer.apple.com/documentation/swift/systemrandomnumbergenerator) makes the following guarantees about `SystemRandomNumberGenerator`:

> `SystemRandomNumberGenerator` is automatically seeded, is safe to use in multiple threads, and uses a cryptographically secure algorithm whenever possible.

## Custom RNGs

The intention is that the default RNG should be the correct choice for most simple use cases. But if your code has special requirements for a random number generator, such as a specific algorithm or the ability to initialize the RNG with a repeatable seed, you can implement your own RNG by adopting the the [`RandomNumberGenerator`](https://developer.apple.com/documentation/swift/randomnumbergenerator) protocol. The protocol has a single requirement: a `next()` method that produces 8 fresh bytes of randomness:

```
public protocol RandomNumberGenerator {
    /// Returns a value from a uniform, independent
    /// distribution of binary data.
    public mutating func next() -> UInt64
}
```

Notice that the protocol requires a uniform distribution. The idea is that users who need random values with non-uniform distributions can apply the desired distribution to the sequence of uniformly distributed randomness in a second step.

## Using a custom RNG

All standard library APIs for producing random values provide an overload that allows users to pass in a custom random number generator. For example, the `Int` type has these two methods:

```
extension Int {
    static func random(in range: Range<Int>) -> Int { ... }
    static func random<T>(in range: Range<Int>,
        using generator: inout T) -> Int
        where T: RandomNumberGenerator { ... }
    // The overloads that take a ClosedRange are not shown
}
```

The `generator` parameter is always passed [`inout`](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID545) because it’s common for RNGs to mutate their state when generating new randomness.

Here’s how you would use a custom RNG. You need to create a mutable variable to satisfy the `inout` requirement:

```
var mersenneTwister = MersenneTwisterRNG(...) // assume this exists
Int.random(in: 10..<20, using: &mersenneTwister)
```

# Producing random values in your own types

If it makes sense for your own data types to produce random values, you should try to follow the standard library pattern:

- method that always uses the default RNG. This can take additional parameters if it makes sense to constrain the random values to a certain range.
- , that takes a generic random number generator.

Example: an enum representing playing card suits. We’re taking advantage of the compiler-synthesized [`allCases`](https://developer.apple.com/documentation/swift/caseiterable) property ([new in Swift 4.2](https://github.com/apple/swift-evolution/blob/master/proposals/0194-derived-collection-of-enum-cases.md)) for the implementation:

```
enum Suit: String, CaseIterable {
    case diamonds = "♦"
    case clubs = "♣"
    case hearts = "♥"
    case spades = "♠"

    static func random() -> Suit {
        var rng = SystemRandomNumberGenerator()
        return Suit.random(using: &rng)
    }

    static func random<T: RandomNumberGenerator>
        (using generator: inout T) -> Suit
    {
        // Force-unwrap can't fail as long as the
        // enum has at least one case.
        return allCases.randomElement(using: &generator)!
    }
}

let randomSuit = Suit.random() // → clubs
randomSuit.rawValue // → "♣"
```
