---
title: PHPersistentObjectChangeDetails
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentobjectchangedetails
source_url: 'https://developer.apple.com/documentation/photos/phpersistentobjectchangedetails'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentobjectchangedetails.json'
content_hash: 'sha256:fe52543ad0f51d6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPersistentObjectChangeDetails

<sub>Class</sub>

An object that represents the local identifiers that change between requests using a change token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHPersistentObjectChangeDetails
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Object Type

- [objectType](phpersistentobjectchangedetails/objecttype.md) — The model type the change represents.
- [PHObjectType](phobjecttype.md) — Identifies the type of objects in a change request.

### Getting the Change Details

- [insertedLocalIdentifiers](phpersistentobjectchangedetails/insertedlocalidentifiers.md) — The local identifiers the system inserts since the change token you specify.
- [updatedLocalIdentifiers](phpersistentobjectchangedetails/updatedlocalidentifiers.md) — The local identifiers the system updates since the change token you specify.
- [deletedLocalIdentifiers](phpersistentobjectchangedetails/deletedlocalidentifiers.md) — The local identifiers the system deletes since the change token you specify.

## See Also

### Getting the Change History

- [- changeDetailsForObjectType:error:](<phpersistentchange/changedetails(for_).md>) — Returns the change history that contains the local identifiers for object inserts, updates, and deletes.
