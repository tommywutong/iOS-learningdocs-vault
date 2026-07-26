---
title: AsyncSequence
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncsequence
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence.json'
content_hash: 'sha256:9f16a6a0b12ca96f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncSequence

<sub>Protocol</sub>

A type that provides asynchronous, sequential, iterated access to its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AsyncSequence<Element, Failure>
```

## Overview

An `AsyncSequence` resembles the `Sequence` type — offering a list of values you can step through one at a time — and adds asynchronicity. An `AsyncSequence` may have all, some, or none of its values available when you first use it. Instead, you use `await` to receive values as they become available.

As with `Sequence`, you typically iterate through an `AsyncSequence` with a `for await`-`in` loop. However, because the caller must potentially wait for values, you use the `await` keyword. The following example shows how to iterate over `Counter`, a custom `AsyncSequence` that produces `Int` values from `1` up to a `howHigh` value:

```swift
for await number in Counter(howHigh: 10) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 7 8 9 10 "
```

An `AsyncSequence` doesn’t generate or contain the values; it just defines how you access them. Along with defining the type of values as an associated type called `Element`, the `AsyncSequence` defines a `makeAsyncIterator()` method. This returns an instance of type `AsyncIterator`. Like the standard `IteratorProtocol`, the `AsyncIteratorProtocol` defines a single `next()` method to produce elements. The difference is that the `AsyncIterator` defines its `next()` method as `async`, which requires a caller to wait for the next value with the `await` keyword.

`AsyncSequence` also defines methods for processing the elements you receive, modeled on the operations provided by the basic `Sequence` in the standard library. There are two categories of methods: those that return a single value, and those that return another `AsyncSequence`.

Single-value methods eliminate the need for a `for await`-`in` loop, and instead let you make a single `await` call. For example, the `contains(_:)` method returns a Boolean value that indicates if a given value exists in the `AsyncSequence`. Given the `Counter` sequence from the previous example, you can test for the existence of a sequence member with a one-line call:

```swift
let found = await Counter(howHigh: 10).contains(5) // true
```

Methods that return another `AsyncSequence` return a type specific to the method’s semantics. For example, the `.map(_:)` method returns a `AsyncMapSequence` (or a `AsyncThrowingMapSequence`, if the closure you provide to the `map(_:)` method can throw an error). These returned sequences don’t eagerly await the next member of the sequence, which allows the caller to decide when to start work. Typically, you’ll iterate over these sequences with `for await`-`in`, like the base `AsyncSequence` you started with. In the following example, the `map(_:)` method transforms each `Int` received from a `Counter` sequence into a `String`:

```swift
let stream = Counter(howHigh: 10)
    .map { $0 % 2 == 0 ? "Even" : "Odd" }
for await s in stream {
    print(s, terminator: " ")
}
// Prints "Odd Even Odd Even Odd Even Odd Even Odd Even "
```

## Relationships

- **Conforming Types**: [AsyncCompactMapSequence](asynccompactmapsequence.md), [AsyncDropFirstSequence](asyncdropfirstsequence.md), [AsyncDropWhileSequence](asyncdropwhilesequence.md), [AsyncFilterSequence](asyncfiltersequence.md), [AsyncFlatMapSequence](asyncflatmapsequence.md), [AsyncMapSequence](asyncmapsequence.md), [AsyncPrefixSequence](asyncprefixsequence.md), [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md), [AsyncStream](asyncstream.md), [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md), [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md), [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md), [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md), [AsyncThrowingMapSequence](asyncthrowingmapsequence.md), [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md), [AsyncThrowingStream](asyncthrowingstream.md), [Observations](../observation/observations.md), [TaskGroup](taskgroup.md), [ThrowingTaskGroup](throwingtaskgroup.md)

## Topics

### Creating an Iterator

- [makeAsyncIterator()](<asyncsequence/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIterator](asyncsequence/asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIteratorProtocol](asynciteratorprotocol.md) — A type that asynchronously supplies the values of a sequence one at a time.
- [Element](asyncsequence/element.md) — The type of element produced by this asynchronous sequence.

### Finding Elements

- [contains(_:)](<asyncsequence/contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<asyncsequence/contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<asyncsequence/allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [first(where:)](<asyncsequence/first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [min()](<asyncsequence/min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<asyncsequence/min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [max()](<asyncsequence/max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<asyncsequence/max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.

### Selecting Elements

- [prefix(_:)](<asyncsequence/prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [AsyncPrefixSequence](asyncprefixsequence.md) — An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [prefix(while:)](<asyncsequence/prefix(while_)-2xy95.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [prefix(while:)](<asyncsequence/prefix(while_)-6yp5n.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.

### Excluding Elements

- [dropFirst(_:)](<asyncsequence/dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [AsyncDropFirstSequence](asyncdropfirstsequence.md) — An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-9sp3b.md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [AsyncDropWhileSequence](asyncdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-67kgo.md>) — Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<asyncsequence/filter(__)-435af.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [AsyncFilterSequence](asyncfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [filter(_:)](<asyncsequence/filter(__)-2cc0l.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.

### Transforming a Sequence

- [map(_:)](<asyncsequence/map(__)-1q1k3.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [AsyncMapSequence](asyncmapsequence.md) — An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<asyncsequence/map(__)-70wgb.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [AsyncThrowingMapSequence](asyncthrowingmapsequence.md) — An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<asyncsequence/compactmap(__)-gfdq.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [AsyncCompactMapSequence](asynccompactmapsequence.md) — An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<asyncsequence/compactmap(__)-1f8zn.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md) — An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [AsyncFlatMapSequence](asyncflatmapsequence.md) — An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.
- [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md) — An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<asyncsequence/reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<asyncsequence/reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

### Adapting Textual Sequences

- [characters](asyncsequence/characters.md) — A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.
- [AsyncCharacterSequence](../foundation/asynccharactersequence.md) — An asynchronous sequence of characters.
- [unicodeScalars](asyncsequence/unicodescalars.md) — A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
- [AsyncUnicodeScalarSequence](../foundation/asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [lines](asyncsequence/lines.md) — A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [AsyncLineSequence](../foundation/asynclinesequence.md) — An asynchronous sequence of lines of text.

### Associated Types

- [Failure](asyncsequence/failure.md) — The type of errors produced when iteration over the sequence fails.

### Instance Methods

- [flatMap(_:)](<asyncsequence/flatmap(__)-4bl9a.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<asyncsequence/flatmap(__)-54rrt.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<asyncsequence/flatmap(__)-5j8ra.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [flatMap(_:)](<asyncsequence/flatmap(__)-5rn1j.md>) — Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.

## See Also

### Asynchronous Sequences

- [AsyncStream](asyncstream.md) — An asynchronous sequence generated from a closure that calls a continuation to produce new elements.
- [AsyncThrowingStream](asyncthrowingstream.md) — An asynchronous sequence generated from an error-throwing closure that calls a continuation to produce new elements.
