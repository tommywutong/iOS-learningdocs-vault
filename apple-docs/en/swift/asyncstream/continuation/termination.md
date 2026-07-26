---
title: AsyncStream.Continuation.Termination
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/termination
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/termination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/termination.json'
content_hash: 'sha256:99e17c3c4a40e6af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncStream](../../asyncstream.md) · [Continuation](../continuation.md)

# AsyncStream.Continuation.Termination

<sub>Enumeration</sub>

A type that indicates how the stream terminated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Termination
```

## Overview

The `onTermination` closure receives an instance of this type.

## Relationships

- **Conforms To**: [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Termination States

- [AsyncStream.Continuation.Termination.finished](termination/finished.md) — The stream finished as a result of calling the continuation’s `finish` method.
- [AsyncStream.Continuation.Termination.cancelled](termination/cancelled.md) — The stream finished as a result of cancellation.

### Hashing

- [hashValue](termination/hashvalue.md) — The hash value.
- [hash(into:)](<termination/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Comparing Termination Values

- [==(_:_:)](<termination/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<termination/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.

### Default Implementations

- [Equatable Implementations](termination/equatable-implementations.md)

## See Also

### Handling Termination

- [onTermination](ontermination.md) — A callback to invoke when canceling iteration of an asynchronous stream.
