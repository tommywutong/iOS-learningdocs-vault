---
title: AVAsyncProperty.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasyncproperty/status
source_url: 'https://developer.apple.com/documentation/avfoundation/avasyncproperty/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasyncproperty/status.json'
content_hash: 'sha256:569f1e21a9e58b28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsyncProperty](../avasyncproperty.md)

# AVAsyncProperty.Status

<sub>Enumeration</sub>

Loaded status values for asynchronous properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Status
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVAsyncProperty.Status.notYetLoaded](status/notyetloaded.md) — The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](status/loading.md) — The system is loading the property.
- [AVAsyncProperty.Status.loaded(_:)](<status/loaded(__).md>) — A property value is ready to use.
- [AVAsyncProperty.Status.failed(_:)](<status/failed(__).md>) — A property value fails to load.
