---
title: NSKeyValueSharedObservers
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluesharedobservers
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluesharedobservers.json'
content_hash: 'sha256:e9d1be4f756261d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueSharedObservers

<sub>Class</sub>

A collection of key-value observations which may be registered with multiple observable objects

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSKeyValueSharedObservers
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializers

- [- initWithObservableClass:](<nskeyvaluesharedobservers/init(observableclass_).md>) — A new collection of observables for an observable object of the given class

### Instance Methods

- [- addSharedObserver:forKey:options:context:](<nskeyvaluesharedobservers/addsharedobserver(__forkey_options_context_).md>) — Add a new observer to the collection.
- [- snapshot](<nskeyvaluesharedobservers/snapshot().md>) — A momentary snapshot of all observers added to the collection thus far, that can be assigned to an observable using `-[NSObject setSharedObservers:]`

## See Also

### Classes

- [NSKeyValueObservation](nskeyvalueobservation.md)
- [NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md) — A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`
