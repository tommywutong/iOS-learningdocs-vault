---
title: Generic Range Algorithms
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/10/generic-range-algorithms/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:063bd1af5a1435bb'
translated: false
---

> 原文：[Generic Range Algorithms](https://oleb.net/blog/2016/10/generic-range-algorithms/)　·　Ole Begemann

# Generic Range Algorithms

I mentioned in [an earlier post](https://oleb.net/blog/2016/09/swift-3-ranges/#converting-between-half-open-and-closed-ranges) that the two basic range types in Swift, [`Range`](https://developer.apple.com/reference/swift/range) and [`ClosedRange`](https://developer.apple.com/reference/swift/closedrange), are not convertible to each other. This makes it difficult to write a function that should work with both types.

Yesterday, someone on the swift-users mailing list [had the exact problem](https://forums.swift.org/t/how-to-be-dry-on-ranges-and-closed-ranges/4251): suppose you’ve written a function named `random` that takes an integer range and returns a random value that lies in the range:

```
import Darwin // or Glibc on Linux

func random(from range: Range<Int>) -> Int {
    let distance = range.upperBound - range.lowerBound
    let rnd = arc4random_uniform(UInt32(distance))
    return range.lowerBound + Int(rnd)
}
```

You can call this function with a half-open range:

```
let random1 = random(from: 1..<10)
```

But you can’t pass a closed range:

```
let random2 = random(from: 1...9) // error
```

That sucks. What’s the best way to solve this?

# Overloading

One option is to overload the `random` function, adding a variant that takes a `ClosedRange`. The implementation can simply forward to the existing overload:

```
func random(from range: ClosedRange<Int>) -> Int {
    return random(from: range.lowerBound ..< range.upperBound+1)
}
```

This would fail for input ranges whose upper bound is `Int.max` because such a range can’t be expressed as a half-open range. However, this is not a relevant problem in our example because the `arc4random_uniform` function can only deal with 32-bit integers anyway, so the program would crash on the conversion to `UInt32` long before hitting this new limitation.

# Countable ranges are convertible

Since this particular example deals with integer ranges, we have another option. Integer-based ranges are _countable_, and countable ranges are convertible between their half-open and closed variants, [`CountableRange`](https://developer.apple.com/reference/swift/countablerange) and [`CountableClosedRange`](https://developer.apple.com/reference/swift/countableclosedrange). So we can switch the parameter type to `CountableRange` like this:

```
func random(from range: CountableRange<Int>) -> Int {
    // Same implementation
    ...
}
```

And now we can call the function with a closed range, but _only_ if we explicitly convert it to `CountableRange` first, which is not very nice (and unintuitive):

```
// Works as before
let random3 = random(from: 1..<10)
// Requires explicit conversion
let random4 = random(from: CountableRange(1...9))
```

Now you might think, no problem, let’s overload the closed-range operator `...` to return a half-open range, like this (I copied this declaration from the existing version in the standard library and only changed the return type from `CountableClosedRange` to `CountableRange`):

```
func ...<Bound>(minimum: Bound, maximum: Bound) -> CountableRange<Bound>
    where Bound: _Strideable & Comparable, Bound.Stride: SignedInteger {
    return CountableRange(uncheckedBounds: (lower: minimum, upper: maximum.advanced(by: 1)))
}
```

This would solve our problem, but unfortunately it creates new ones, because now an expression like `1...9` is ambiguous without explicit type information — the compiler can’t decide between which overload to choose. So this is not a good option.

# Writing generic code by identifying the essential interface

The reason I’m writing this post is to point out [a very good suggestion](https://forums.swift.org/t/how-to-be-dry-on-ranges-and-closed-ranges/4251/4) Hooman Mehr made on the mailing list: what if ranges are not the best abstraction for this algorithm anyway? What if we consider a higher abstraction level?

Let’s try to identify the _essential interface_ our `random` function needs, i.e. the minimal set of features required to implement the functionality:

- It needs an efficient way to compute the distance between the lower and upper bounds of the input sequence.
- It needs an efficient way to retrieve the _n_-th element of the input sequence in order to return it, where _n_ is the random distance from the lower bound it computed.

Hooman notes that both countable range types share a common protocol conformance in the form of [`RandomAccessCollection`](https://developer.apple.com/reference/swift/randomaccesscollection). And indeed, `RandomAccessCollection` provides exactly the essential interface we want: random-access collections guarantee that they can measure distances between indices and access elements at arbitrary indices in constant time.

So let’s turn the `random` function into a method on `RandomAccessCollection` (the [`numericCast`s](https://developer.apple.com/reference/swift/1641291-numericcast) are required because different collections have different [`IndexDistance`](https://developer.apple.com/reference/swift/collection/indexdistance) types):

```
extension RandomAccessCollection {
    func random() -> Iterator.Element? {
        guard !isEmpty else { return nil }
        let offset = arc4random_uniform(numericCast(count))
        let i = index(startIndex, offsetBy: numericCast(offset))
        return self[i]
    }
}
```

Now it works with both range types:

```
(1..<10).random()
(1...9).random()
```

And even better, we can now get a random element from _every_ random-access collection:

```
let people = ["Susan", "David", "Janet", "Jordan", "Kelly"]
let winner = people.random()
```

# Conclusion

We already knew that the distinction between half-open ranges and closed ranges in the type system is unintuitive. If you’re stuck with ranges, the best way to deal with the problem is usually to suck it up and provide two overloads, even if that means you have to repeat some code.

But it can pay off to make your code more generic. Even if you don’t need your algorithm to work with other data types right now, implementing it generically at the correct level of abstraction forces you to think about the _essential interface_ your algorithm requires, which in turn makes it easier for readers of the code to keep the capabilities of the involved types in their head — a `RandomAccessCollection` has by definition fewer methods and properties than a concrete type that conforms to the protocol (such as `CountableRange`).

Don’t overdo it, though. Generic code with lots of constraints on the generic parameters can also be harder to read, and especially if you write application code that doesn’t provide public APIs to third parties, spending too much time building the perfect abstraction without getting any real work done is an easy trap to fall into.
