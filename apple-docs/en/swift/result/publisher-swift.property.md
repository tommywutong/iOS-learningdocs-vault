---
title: publisher
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/result/publisher-swift.property
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.property.json'
content_hash: 'sha256:9b708312b80f2733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# publisher

<sub>Instance Property</sub>

A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var publisher: Result<Success, Failure>.Publisher { get }
```

## Discussion

In the following example, `goodResult` provides a successful result with the integer value `1`. A sink subscriber connected to the result’s publisher receives the output `1`, followed by a normal completion ([Subscribers.Completion.finished](../../combine/subscribers/completion/finished.md)).

```swift
 let goodResult: Result<Int, MyError> = .success(1)
 goodResult.publisher
     .sink(receiveCompletion: { print("goodResult done: \($0)")},
           receiveValue: { print("goodResult value: \($0)")} )
 // Prints:
 // goodResult value: 1
 // goodResult done: finished
```

In contrast with the [Just](../../combine/just.md) publisher, which always publishes a single value, this publisher might not send any values and instead terminate with an error, if the result is `/Swift/Result/failure`. In the next example, `badResult` is a failure result that wraps a custom error. A sink subscriber connected to this result’s publisher immediately receives a termination ([Subscribers.Completion.failure(_:)](<../../combine/subscribers/completion/failure(__).md>)).

```swift
 struct MyError: Error, CustomDebugStringConvertible {
     var debugDescription: String = "MyError"
 }
 let badResult: Result<Int, MyError> = .failure(MyError())
 badResult.publisher
     .sink(receiveCompletion: { print("badResult done: \($0)")},
           receiveValue: { print("badResult value: \($0)")} )
 // Prints:
 // badResult done: failure(MyError)
```

## See Also

### Publishing a Result

- [Publisher](publisher-swift.struct.md) — The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.
