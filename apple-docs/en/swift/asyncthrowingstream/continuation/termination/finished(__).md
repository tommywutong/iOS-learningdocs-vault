---
title: 'AsyncThrowingStream.Continuation.Termination.finished(_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingstream/continuation/termination/finished(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/termination/finished(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/termination/finished%28_%3A%29.json'
content_hash: 'sha256:b8a01da933608aa5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncThrowingStream](../../../asyncthrowingstream.md) · [Continuation](../../continuation.md) · [Termination](../termination.md)

# AsyncThrowingStream.Continuation.Termination.finished(_:)

<sub>Case</sub>

The stream finished as a result of calling the continuation’s `finish` method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case finished(Failure?)
```

## Discussion

The associated `Failure` value provides the error that terminated the stream. If no error occurred, this value is `nil`.

## See Also

### Termination States

- [AsyncThrowingStream.Continuation.Termination.cancelled](cancelled.md) — The stream finished as a result of cancellation.
