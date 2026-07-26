---
title: NSKeyValueObservation
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservation
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservation.json'
content_hash: 'sha256:d728df6c933c28a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueObservation

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@objc(_NSKeyValueObservation) class NSKeyValueObservation
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Methods

- [invalidate()](<nskeyvalueobservation/invalidate().md>) — invalidate() will be called automatically when an NSKeyValueObservation is deinited

## See Also

### Classes

- [NSKeyValueSharedObservers](nskeyvaluesharedobservers.md) — A collection of key-value observations which may be registered with multiple observable objects
- [NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md) — A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`
