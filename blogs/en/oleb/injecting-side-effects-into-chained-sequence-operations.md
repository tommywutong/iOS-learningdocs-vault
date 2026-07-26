---
title: Injecting side effects into chained Sequence operations
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/10/chained-foreach/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67aadd57b1bb63b1'
translated: false
---

> 原文：[Injecting side effects into chained Sequence operations](https://oleb.net/blog/2017/10/chained-foreach/)　·　Ole Begemann

# Injecting side effects into chained Sequence operations

A few weeks ago a reader [pointed out an error](https://twitter.com/jasonalexzurita/status/915972380685516800) in [_Advanced Swift_](https://oleb.net/advanced-swift/). We had written this about Swift’s [`forEach`](https://developer.apple.com/documentation/swift/sequence/2906738-foreach) method:

> And it [`forEach`] really shines as part of a sequence of chained operations. For instance, imagine you’ve chained several calls to `map` and `filter` in a single statement, and during debugging you want to log the intermediate values somewhere in the middle of the chain. Inserting a `forEach` step at the desired position is probably the quickest way to do this.

I imagine there was a lot of wishful thinking at play when we wrote this because it sounds like a truly useful feature^[1](#fn:1) (and it’s something you can’t do with a `for`-`in` loop). Alas, it’s completely wrong — you can’t use `forEach` in the middle of a chain like this!

# How I’d like it to work

To illustrate the idea with a code sample, let’s say we have chained a number of operations on a sequence:

```
let numbers = 1...10
let sumOfSquaredEvenNumbers = numbers
    .filter { $0 % 2 == 0}
    .map { $0 * $0 }
    .reduce(0, +)
// → 220
```

Now suppose we wanted to check that each of the operations in the chain does what we expect. It’d be really neat if we could insert a call like `.forEach { print($0) }` somewhere in the middle of that chain to inspect the elements that come out of the `filter` and/or `map` operations.

Why doesn’t `forEach` support this? To appear in the middle of the chain, it would have to return some kind of [`Sequence`](https://developer.apple.com/documentation/swift/sequence) such that the next operation in the chain has something to operate. Because the return type of `forEach` is `()`, it can only appear at the end of the chain.

# A `forEach` variant that returns `Self`

Fortunately, it’s not difficult to add this functionality. All we need is a method on `Sequence` that calls the passed-in function once for each element (like `forEach`) and then returns itself so that the chain can continue as if nothing happened. In other words, the method’s return type should be `Self`. I chose to call it `forEachPerform` to avoid ambiguities between it and the original `forEach` during type checking:

```
extension Sequence {
    /// Perform a side effect for each element in `self`.
    @discardableResult
    func forEachPerform(_ body: (Element) throws -> ())
        rethrows -> Self
    {
        try forEach(body)
        return self
    }
}
```

Unlike `forEach`, we can insert this method into the chain like so:

```
let sumOfSquaredEvenNumbers = numbers
    .filter { $0 % 2 == 0}
    .forEachPerform { print($0) }
    .map { $0 * $0 }
    .reduce(0, +)
/* Prints:
2
4
6
8
10
*/
```

I also found it useful to add a second method, which calls its function argument only once for the entire sequence and not once per element:

```
extension Sequence {
    /// Perform a side effect.
    @discardableResult
    func perform(_ body: (Self) throws -> ())
        rethrows -> Self
    {
        try body(self)
        return self
    }
}
```

This is perfect for logging each intermediate result:

```
let sumOfSquaredEvenNumbers = numbers
    .filter { $0 % 2 == 0}
    .perform { print("After filter: \($0)") }
    .map { $0 * $0 }
    .perform { print("After map: \($0)") }
    .reduce(0, +)
/* Prints:
After filter: [2, 4, 6, 8, 10]
After map: [4, 16, 36, 64, 100]
*/
```

# Self-consuming sequences

The new methods return `self` unchanged, so inserting them into a chain should be totally transparent. But note that the `Sequence` protocol makes no guarantees that implementations produce the same sequence of elements when iterated repeatedly.

Most conforming types obviously do guarantee this (like [`Array`](https://developer.apple.com/documentation/swift/array)), but suppose you have a `Sequence` that represents an incoming byte stream from a network socket: calling `forEachPerform` or `perform` on it will consume the sequence, leaving no bytes to process for subsequent operations.

If that’s a problem for you, you could either have the methods return an `Array<Element>` (thereby implicitly turning destructive sequences into repeatable ones) or to add the new methods on [`Collection`](https://developer.apple.com/documentation/swift/collection) (which does guarantee non-destructive iteration).

# Making it lazy

Another not-quite-transparent side effect of `forEachPerform` is that it doesn’t work well with _lazy sequences_.

The idea of a lazy sequence is that it should defer all work to produce the next element until the last possible moment, i.e. when an operation further down the chain actually requests that element. By looping over each element in the implementation of `forEachPerform`, we destroy any laziness the incoming sequence may have had.

To preserve the laziness, we can define our own lazy iterator and sequence types, named `LazyForEachIterator` and `LazyForEachSequence`. These work exactly like similar types in the standard library: instead of executing the side effect function immediately, they _store_ the function and the incoming sequence, and then they _wait_ until someone requests the next element. Only then will they in turn ask the base sequence for _its_ next element and process it.

The code looks like this:

```
struct LazyForEachIterator<Base: IteratorProtocol>
    : IteratorProtocol
{
    mutating func next() -> Base.Element? {
        guard let nextElement = base.next() else {
            return nil
        }
        perform(nextElement)
        return nextElement
    }
    var base: Base
    let perform: (Base.Element) -> ()
}

struct LazyForEachSequence<Base: Sequence>
    : LazySequenceProtocol
{
    func makeIterator()
        -> LazyForEachIterator<Base.Iterator>
    {
        return LazyForEachIterator(
            base: base.makeIterator(),
            perform: perform)
    }
    let base: Base
    let perform: (Base.Element) -> ()
}
```

Notice that our sequence type conforms to [`LazySequenceProtocol`](https://developer.apple.com/documentation/swift/lazysequenceprotocol). This protocol inherits from `Sequence`. Its purpose is to provide lazy implementations of normally-eager operations.

When you call a method like `map` on a value that conforms to `LazySequenceProtocol`, the compiler will favor the lazy variant of `map` over the non-lazy version because one of Swift’s type inference rules is to pick the most specific overload that works under the given constraints.

To achieve the same effect for our method, we can extend `LazySequenceProtocol` with a variant of `forEachPerform` that returns a lazy sequence:

```
extension LazySequenceProtocol {
    func forEachPerform(_ body: @escaping (Element) -> ())
        -> LazyForEachSequence<Self>
    {
        return LazyForEachSequence(base: self,
            perform: body)
    }
}
```

This method differs in several aspects from the non-lazy version:

- The function parameter must be `@escaping` because we’re storing it.
- It doesn’t support throwing functions because that wouldn’t work with lazy evaluation.
- The return value is not marked as discardable because a lazy operation that no one ever executes later doesn’t make any sense.

But the most important charateristic is what we discussed above: the method doesn’t perform any work except storing the base sequence and the function for later.

With this in place, `forEachPerform` will preserve the laziness of a sequence (notice the `.lazy` call):

```
let largeNumbersSquared = numbers
    .lazy
    .filter { $0 >= 5 }
    .forEachPerform { print("After filter: \($0)") }
    .map { $0 * $0 }
// Prints nothing
```

_Note: Actually, this exact code produces a compile error in Swift 4.0: “ambiguous use of ‘forEachPerform’”. It only works as shown here if I change the return type of `Sequence.forEachPerform` from `Self` to `[Element]`. I’m not quite sure why that is. As a workaround, you could give `LazySequenceProtocol.forEachPerform` a unique name._

Only when we access elements from the lazy sequence will the side effects for those elements be printed:

```
// Access the first two elements
Array(largeNumbersSquared.prefix(2))
/* Prints:
After filter: 5
After filter: 6
*/
// → [25, 36]
```

# Conclusion

I really like being able to inject side effects into method chains, even if I almost never use this for anything other than debugging. And although `print`-based debugging is arguably anachronistic, I still use it all the time.

Perhaps you find this useful too.

PS: Chris and I wrote the last words for the Swift 4 edition of Advanced Swift a few days ago. There’s still some final production work to do, but the book will be out real soon now™.

1. [RxSwift](https://github.com/ReactiveX/RxSwift) has a similar operator called [`debug`](https://github.com/ReactiveX/RxSwift/blob/master/RxSwift/Observables/Debug.swift). [↩︎](#fnref:1)
