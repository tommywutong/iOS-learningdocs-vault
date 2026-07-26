---
title: InstantProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/instantprotocol
source_url: 'https://developer.apple.com/documentation/swift/instantprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/instantprotocol.json'
content_hash: 'sha256:e89a592f4f1314db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# InstantProtocol

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol InstantProtocol<Duration> : Comparable, Hashable, Sendable
```

## Relationships

- **Inherits From**: [Comparable](comparable.md), [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

- **Conforming Types**: [Instant](continuousclock/instant.md), [Instant](suspendingclock/instant.md)

## Topics

### Associated Types

- [Duration](instantprotocol/duration.md)

### Instance Methods

- [advanced(by:)](<instantprotocol/advanced(by_).md>)
- [duration(to:)](<instantprotocol/duration(to_).md>)
