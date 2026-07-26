---
title: AsyncIteratorProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asynciteratorprotocol
source_url: 'https://developer.apple.com/documentation/swift/asynciteratorprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynciteratorprotocol.json'
content_hash: 'sha256:94d63342db8e538f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncIteratorProtocol

<sub>Protocol</sub>

A type that asynchronously supplies the values of a sequence one at a time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AsyncIteratorProtocol<Element, Failure>
```

## Overview

The `AsyncIteratorProtocol` defines the type returned by the `makeAsyncIterator()` method of the `AsyncSequence` protocol. In short, the iterator is what produces the asynchronous sequence’s values. The protocol defines a single asynchronous method, `next()`, which either produces the next element of the sequence, or returns `nil` to signal the end of the sequence.

To implement your own `AsyncSequence`, implement a wrapped type that conforms to `AsyncIteratorProtocol`. The following example shows a `Counter` type that uses an inner iterator to monotonically generate `Int` values until reaching a `howHigh` value. While this example isn’t itself asynchronous, it shows the shape of a custom sequence and iterator, and how to use it as if it were asynchronous:

```swift
struct Counter: AsyncSequence {
    typealias Element = Int
    let howHigh: Int

    struct AsyncIterator: AsyncIteratorProtocol {
        let howHigh: Int
        var current = 1

        mutating func next() async -> Int? {
            // A genuinely asynchronous implementation uses the `Task`
            // API to check for cancellation here and return early.
            guard current <= howHigh else {
                return nil
            }

            let result = current
            current += 1
            return result
        }
    }

    func makeAsyncIterator() -> AsyncIterator {
        return AsyncIterator(howHigh: howHigh)
    }
}
```

At the call site, this looks like:

```swift
for await number in Counter(howHigh: 10) {
  print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 7 8 9 10 "
```

### End of Iteration

The iterator returns `nil` to indicate the end of the sequence. After returning `nil` (or throwing an error) from `next()`, the iterator enters a terminal state, and all future calls to `next()` must return `nil`.

### Cancellation

Types conforming to `AsyncIteratorProtocol` should use the cancellation primitives provided by Swift’s `Task` API. The iterator can choose how to handle and respond to cancellation, including:

- Checking the `isCancelled` value of the current `Task` inside `next()` and returning `nil` to terminate the sequence.
- Calling `checkCancellation()` on the `Task`, which throws a `CancellationError`.
- Implementing `next()` with a `withTaskCancellationHandler(handler:operation:)` invocation to immediately react to cancellation.

If the iterator needs to clean up on cancellation, it can do so after checking for cancellation as described above, or in `deinit` if it’s a reference type.

## Relationships

- **Conforming Types**: [Iterator](asynccompactmapsequence/iterator.md), [Iterator](asyncdropfirstsequence/iterator.md), [Iterator](asyncdropwhilesequence/iterator.md), [Iterator](asyncfiltersequence/iterator.md), [Iterator](asyncflatmapsequence/iterator.md), [Iterator](asyncmapsequence/iterator.md), [Iterator](asyncprefixsequence/iterator.md), [Iterator](asyncprefixwhilesequence/iterator.md), [Iterator](asyncstream/iterator.md), [Iterator](asyncthrowingcompactmapsequence/iterator.md), [Iterator](asyncthrowingdropwhilesequence/iterator.md), [Iterator](asyncthrowingfiltersequence/iterator.md), [Iterator](asyncthrowingflatmapsequence/iterator.md), [Iterator](asyncthrowingmapsequence/iterator.md), [Iterator](asyncthrowingprefixwhilesequence/iterator.md), [Iterator](asyncthrowingstream/iterator.md), [Iterator](../observation/observations/iterator.md), [Iterator](taskgroup/iterator.md), [Iterator](throwingtaskgroup/iterator.md)

## Topics

### Declaring Iterator Topography

- [Element](asynciteratorprotocol/element.md)

### Producing Iterator Values

- [next()](<asynciteratorprotocol/next().md>) — Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

### Associated Types

- [Failure](asynciteratorprotocol/failure.md) — The type of failure produced by iteration.

### Instance Methods

- [next(isolation:)](<asynciteratorprotocol/next(isolation_).md>) — Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

## See Also

### Creating an Iterator

- [makeAsyncIterator()](<asyncsequence/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIterator](asyncsequence/asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Element](asyncsequence/element.md) — The type of element produced by this asynchronous sequence.
