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
doc_path: /documentation/swift/asyncstream/continuation/ontermination
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/ontermination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/ontermination.json'
content_hash: 'sha256:30c4f1ae04d32429'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# onTermination

<sub>Instance Property</sub>

A callback to invoke when canceling iteration of an asynchronous stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var onTermination: (@Sendable (AsyncStream<Element>.Continuation.Termination) -> Void)? { get nonmutating set }
```

## Discussion

If an `onTermination` callback is set, using task cancellation to terminate iteration of an `AsyncStream` results in a call to this callback.

Canceling an active iteration invokes the `onTermination` callback first, then resumes by yielding `nil`. This means that you can perform needed cleanup in the cancellation handler. After reaching a terminal state as a result of cancellation, the `AsyncStream` sets the callback to `nil`.

> [!note] Note
> Because the system might call the `onTermination` callback as part of task cancellation, it’s subject to the same considerations for avoiding deadlock as outlined in the documentation for [withTaskCancellationHandler(operation:onCancel:)](<../../withtaskcancellationhandler(operation_oncancel_).md>).

## See Also

### Handling Termination

- [Termination](termination.md) — A type that indicates how the stream terminated.
