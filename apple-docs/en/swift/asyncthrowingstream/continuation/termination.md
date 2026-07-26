---
title: AsyncThrowingStream.Continuation.Termination
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/continuation/termination
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/termination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/continuation/termination.json'
content_hash: 'sha256:c87230bb901da3eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingStream](../../asyncthrowingstream.md) · [Continuation](../continuation.md)

# AsyncThrowingStream.Continuation.Termination

<sub>Enumeration</sub>

A type that indicates how the stream terminated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Termination
```

## Overview

The `onTermination` closure receives an instance of this type.

## Relationships

- **Conforms To**: [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Termination States

- [AsyncThrowingStream.Continuation.Termination.finished(_:)](<termination/finished(__).md>) — The stream finished as a result of calling the continuation’s `finish` method.
- [AsyncThrowingStream.Continuation.Termination.cancelled](termination/cancelled.md) — The stream finished as a result of cancellation.

## See Also

### Handling Termination

- [onTermination](ontermination.md) — A callback to invoke when canceling iteration of an asynchronous stream.
