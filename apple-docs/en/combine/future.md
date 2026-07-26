---
title: Future
framework: Combine
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/future
source_url: 'https://developer.apple.com/documentation/combine/future'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/future.json'
content_hash: 'sha256:4e399b52cdbc7d75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Future

<sub>Class</sub>

A publisher that eventually produces a single value and then finishes or fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Future<Output, Failure> where Failure : Error
```

## Overview

Use a future to perform some work and then asynchronously publish a single element. You initialize the future with a closure that takes a [Promise](future/promise.md); the closure calls the promise with a [Result](../swift/result.md) that indicates either success or failure. In the success case, the future’s downstream subscriber receives the element prior to the publishing stream finishing normally. If the result is an error, publishing terminates with that error.

The following example shows a method that uses a future to asynchronously publish a random number after a brief delay:

```swift
func generateAsyncRandomNumberFromFuture() -> Future <Int, Never> {
    return Future() { promise in
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            let number = Int.random(in: 1...10)
            promise(Result.success(number))
        }
    }
}
```

To receive the published value, you use any Combine subscriber, such as a [Sink](subscribers/sink.md), like this:

```swift
cancellable = generateAsyncRandomNumberFromFuture()
    .sink { number in print("Got random number \(number).") }
```

### Integrating with Swift Concurrency

To integrate with the `async`-`await` syntax in Swift 5.5, `Future` can provide its value to an awaiting caller. This is particularly useful because unlike other types that conform to [Publisher](publisher.md) and potentially publish many elements, a `Future` only publishes one element (or fails). By using the [value](future/value-9iwjz.md) property, the above call point looks like this:

```swift
let number = await generateAsyncRandomNumberFromFuture().value
print("Got random number \(number).")
```

### Alternatives to Futures

The `async`-`await` syntax in Swift can also replace the use of a future entirely, for the case where you want to perform some operation after an asynchronous task completes.

You do this with the function [withCheckedContinuation(isolation:function:_:)](<../swift/withcheckedcontinuation(isolation_function___).md>) and its throwing equivalent, [withCheckedThrowingContinuation(isolation:function:_:)](<../swift/withcheckedthrowingcontinuation(isolation_function___).md>). The following example performs the same asynchronous random number generation as the `Future` example above, but as an `async` method:

```swift
func generateAsyncRandomNumberFromContinuation() async -> Int {
    return await withCheckedContinuation { continuation in
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            let number = Int.random(in: 1...10)
            continuation.resume(returning: number)
        }
    }
}
```

The call point for this method doesn’t use a closure like the future’s sink subscriber does; it simply awaits and assigns the result:

```swift
let asyncRandom = await generateAsyncRandomNumberFromContinuation()
```

For more information on continuations, see the [Concurrency](../swift/concurrency.md) topic in the Swift standard library.

## Relationships

- **Conforms To**: [Publisher](publisher.md)

## Topics

### Creating a future

- [init(_:)](<future/init(__).md>) — Creates a publisher that invokes a promise closure when the publisher emits an element.
- [Promise](future/promise.md) — A type that represents a closure to invoke in the future, when an element or error is available.

### Accessing the value asynchronously

- [value](future/value-9iwjz.md) — The published value of the future, delivered asynchronously.
- [value](future/value-5iprp.md) — The published value of the future or an error, delivered asynchronously.

## See Also

### Convenience Publishers

- [Just](just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Deferred](deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Empty](empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Fail](fail.md) — A publisher that immediately terminates with the specified error.
- [Record](record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.
