---
title: AsyncThrowingStream
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream.json'
content_hash: 'sha256:a39808b25e16ad94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncThrowingStream

<sub>Structure</sub>

An asynchronous sequence generated from an error-throwing closure that calls a continuation to produce new elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncThrowingStream<Element, Failure> where Failure : Error
```

## Overview

`AsyncThrowingStream` conforms to `AsyncSequence`, providing a convenient way to create an asynchronous sequence without manually implementing an asynchronous iterator. In particular, an asynchronous stream is well-suited to adapt callback- or delegation-based APIs to participate with `async`-`await`.

In contrast to `AsyncStream`, this type can throw an error from the awaited `next()`, which terminates the stream with the thrown error.

You initialize an `AsyncThrowingStream` with a closure that receives an `AsyncThrowingStream.Continuation`. Produce elements in this closure, then provide them to the stream by calling the continuation’s `yield(_:)` method. When there are no further elements to produce, call the continuation’s `finish()` method. This causes the sequence iterator to produce a `nil`, which terminates the sequence. If an error occurs, call the continuation’s `finish(throwing:)` method, which causes the iterator’s `next()` method to throw the error to the awaiting call point. The continuation is `Sendable`, which permits calling it from concurrent contexts external to the iteration of the `AsyncThrowingStream`.

An arbitrary source of elements can produce elements faster than they are consumed by a caller iterating over them. Because of this, `AsyncThrowingStream` defines a buffering behavior, allowing the stream to buffer a specific number of oldest or newest elements. By default, the buffer limit is `Int.max`, which means it’s unbounded.

### Adapting Existing Code to Use Streams

To adapt existing callback code to use `async`-`await`, use the callbacks to provide values to the stream, by using the continuation’s `yield(_:)` method.

Consider a hypothetical `QuakeMonitor` type that provides callers with `Quake` instances every time it detects an earthquake. To receive callbacks, callers set a custom closure as the value of the monitor’s `quakeHandler` property, which the monitor calls back as necessary. Callers can also set an `errorHandler` to receive asynchronous error notifications, such as the monitor service suddenly becoming unavailable.

```swift
class QuakeMonitor {
    var quakeHandler: ((Quake) -> Void)?
    var errorHandler: ((Error) -> Void)?

    func startMonitoring() {…}
    func stopMonitoring() {…}
}
```

To adapt this to use `async`-`await`, extend the `QuakeMonitor` to add a `quakes` property, of type `AsyncThrowingStream<Quake>`. In the getter for this property, return an `AsyncThrowingStream`, whose `build` closure – called at runtime to create the stream – uses the continuation to perform the following steps:

1. Creates a `QuakeMonitor` instance.
2. Sets the monitor’s `quakeHandler` property to a closure that receives each `Quake` instance and forwards it to the stream by calling the continuation’s `yield(_:)` method.
3. Sets the monitor’s `errorHandler` property to a closure that receives any error from the monitor and forwards it to the stream by calling the continuation’s `finish(throwing:)` method. This causes the stream’s iterator to throw the error and terminate the stream.
4. Sets the continuation’s `onTermination` property to a closure that calls `stopMonitoring()` on the monitor.
5. Calls `startMonitoring` on the `QuakeMonitor`.

```swift
extension QuakeMonitor {

    static var throwingQuakes: AsyncThrowingStream<Quake, Error> {
        AsyncThrowingStream { continuation in
            let monitor = QuakeMonitor()
            monitor.quakeHandler = { quake in
                 continuation.yield(quake)
            }
            monitor.errorHandler = { error in
                continuation.finish(throwing: error)
            }
            continuation.onTermination = { @Sendable _ in
                monitor.stopMonitoring()
            }
            monitor.startMonitoring()
        }
    }
}
```

Because the stream is an `AsyncSequence`, the call point uses the `for`-`await`-`in` syntax to process each `Quake` instance as produced by the stream:

```swift
do {
    for try await quake in quakeStream {
        print("Quake: \(quake.date)")
    }
    print("Stream done.")
} catch {
    print("Error: \(error)")
}
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Creating a Continuation-Based Stream

- [init(_:bufferingPolicy:_:)](<asyncthrowingstream/init(__bufferingpolicy___).md>) — Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [BufferingPolicy](asyncthrowingstream/continuation/bufferingpolicy.md) — A strategy that handles exhaustion of a buffer’s capacity.
- [Continuation](asyncthrowingstream/continuation.md) — A mechanism to interface between synchronous code and an asynchronous stream.

### Finding Elements

- [contains(_:)](<asyncthrowingstream/contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<asyncthrowingstream/contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<asyncthrowingstream/allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [first(where:)](<asyncthrowingstream/first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [min()](<asyncthrowingstream/min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<asyncthrowingstream/min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [max()](<asyncthrowingstream/max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<asyncthrowingstream/max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.

### Selecting Elements

- [prefix(_:)](<asyncthrowingstream/prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [prefix(while:)](<asyncthrowingstream/prefix(while_).md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.

### Excluding Elements

- [dropFirst(_:)](<asyncthrowingstream/dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [drop(while:)](<asyncthrowingstream/drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<asyncthrowingstream/filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

### Transforming a Sequence

- [map(_:)](<asyncthrowingstream/map(__)-4a4ke.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<asyncthrowingstream/map(__)-58nrj.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<asyncthrowingstream/compactmap(__)-7mgih.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<asyncthrowingstream/compactmap(__)-944nt.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [flatMap(_:)](<asyncthrowingstream/flatmap(__)-vhin.md>) — Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<asyncthrowingstream/reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<asyncthrowingstream/reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

### Creating an Iterator

- [makeAsyncIterator()](<asyncthrowingstream/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [Iterator](asyncthrowingstream/iterator.md) — The asynchronous iterator for iterating an asynchronous stream.

### Supporting Types

- [AsyncIterator](asyncthrowingstream/asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.

### Initializers

- [init(unfolding:)](<asyncthrowingstream/init(unfolding_).md>) — Constructs an asynchronous throwing stream from a given element-producing closure.

### Type Methods

- [makeStream(of:throwing:bufferingPolicy:)](<asyncthrowingstream/makestream(of_throwing_bufferingpolicy_).md>) — Initializes a new [AsyncThrowingStream](asyncthrowingstream.md) and an [Continuation](asyncthrowingstream/continuation.md).

### Default Implementations

- [AsyncSequence Implementations](asyncthrowingstream/asyncsequence-implementations.md)

## See Also

### Asynchronous Sequences

- [AsyncSequence](asyncsequence.md) — A type that provides asynchronous, sequential, iterated access to its elements.
- [AsyncStream](asyncstream.md) — An asynchronous sequence generated from a closure that calls a continuation to produce new elements.
