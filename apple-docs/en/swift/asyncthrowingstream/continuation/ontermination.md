---
title: onTermination
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/continuation/ontermination
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/ontermination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/ontermination.json'
content_hash: 'sha256:ed5aa18b10584229'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# onTermination

<sub>Instance Property</sub>

A callback to invoke when canceling iteration of an asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var onTermination: (@Sendable (AsyncThrowingStream<Element, Failure>.Continuation.Termination) -> Void)? { get nonmutating set }
```

## Discussion

If an `onTermination` callback is set, using task cancellation to terminate iteration of an `AsyncThrowingStream` results in a call to this callback.

Canceling an active iteration invokes the `onTermination` callback first, and then resumes by yielding `nil` or throwing an error from the iterator. This means that you can perform needed cleanup in the cancellation handler. After reaching a terminal state, the `AsyncThrowingStream` disposes of the callback.

> [!note] Note
> Because the system might call the `onTermination` callback as part of task cancellation, it’s subject to the same considerations for avoiding deadlock as outlined in the documentation for [withTaskCancellationHandler(operation:onCancel:)](<../../withtaskcancellationhandler(operation_oncancel_).md>).

## See Also

### Handling Termination

- [Termination](termination.md) — A type that indicates how the stream terminated.
