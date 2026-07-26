---
title: PHPersistentChange
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentchange
source_url: 'https://developer.apple.com/documentation/photos/phpersistentchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentchange.json'
content_hash: 'sha256:93dd34dafccab8f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPersistentChange

<sub>Class</sub>

An object that represents a change in the Photos library, and allows for requesting local identifiers that identify the changes for a library object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHPersistentChange
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Change Token

- [changeToken](phpersistentchange/changetoken.md) — An opaque object that represents the state of Photos library.
- [PHPersistentChangeToken](phpersistentchangetoken.md) — An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.

### Getting the Change History

- [- changeDetailsForObjectType:error:](<phpersistentchange/changedetails(for_).md>) — Returns the change history that contains the local identifiers for object inserts, updates, and deletes.
- [PHPersistentObjectChangeDetails](phpersistentobjectchangedetails.md) — An object that represents the local identifiers that change between requests using a change token.
