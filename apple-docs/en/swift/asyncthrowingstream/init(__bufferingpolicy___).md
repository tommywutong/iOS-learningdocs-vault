---
title: 'init(_:bufferingPolicy:_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/init(_:bufferingpolicy:_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/init(_:bufferingpolicy:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/init%28_%3Abufferingpolicy%3A_%3A%29.json'
content_hash: 'sha256:fa9f80e6b90c5b86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# init(_:bufferingPolicy:_:)

<sub>Initializer</sub>

Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ elementType: Element.Type = Element.self, bufferingPolicy limit: AsyncThrowingStream<Element, Failure>.Continuation.BufferingPolicy = .unbounded, _ build: (AsyncThrowingStream<Element, Failure>.Continuation) -> Void) where Failure == any Error
```

## Parameters

- `elementType` — The type of element the `AsyncThrowingStream` produces.

- `limit` — The maximum number of elements to hold in the buffer. By default, this value is unlimited. Use a `Continuation.BufferingPolicy` to buffer a specified number of oldest or newest elements.

- `build` — A custom closure that yields values to the `AsyncThrowingStream`. This closure receives an `AsyncThrowingStream.Continuation` instance that it uses to provide elements to the stream and terminate the stream when finished.

## Discussion

The `AsyncStream.Continuation` received by the `build` closure is appropriate for use in concurrent contexts. It is thread safe to send and finish; all calls to the continuation are serialized. However, calling this from multiple concurrent contexts could result in out-of-order delivery.

The following example shows an `AsyncStream` created with this initializer that produces 100 random numbers on a one-second interval, calling `yield(_:)` to deliver each element to the awaiting call point. When the `for` loop exits, the stream finishes by calling the continuation’s `finish()` method. If the random number is divisible by 5 with no remainder, the stream throws a `MyRandomNumberError`.

```swift
let stream = AsyncThrowingStream<Int, Error>(Int.self,
                                             bufferingPolicy: .bufferingNewest(5)) { continuation in
    Task.detached {
        for _ in 0..<100 {
            await Task.sleep(1 * 1_000_000_000)
            let random = Int.random(in: 1...10)
            if random % 5 == 0 {
                continuation.finish(throwing: MyRandomNumberError())
                return
            } else {
                continuation.yield(random)
            }
        }
        continuation.finish()
    }
}

// Call point:
do {
    for try await random in stream {
        print(random)
    }
} catch {
    print(error)
}
```

## See Also

### Creating a Continuation-Based Stream

- [BufferingPolicy](continuation/bufferingpolicy.md) — A strategy that handles exhaustion of a buffer’s capacity.
- [Continuation](continuation.md) — A mechanism to interface between synchronous code and an asynchronous stream.
