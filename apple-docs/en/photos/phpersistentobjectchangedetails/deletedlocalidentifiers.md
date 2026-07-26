---
title: deletedLocalIdentifiers
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentobjectchangedetails/deletedlocalidentifiers
source_url: 'https://developer.apple.com/documentation/photos/phpersistentobjectchangedetails/deletedlocalidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentobjectchangedetails/deletedlocalidentifiers.json'
content_hash: 'sha256:870fa746792012cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPersistentObjectChangeDetails](../phpersistentobjectchangedetails.md)

# deletedLocalIdentifiers

<sub>Instance Property</sub>

The local identifiers the system deletes since the change token you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var deletedLocalIdentifiers: Set<String> { get }
```

## See Also

### Getting the Change Details

- [insertedLocalIdentifiers](insertedlocalidentifiers.md) — The local identifiers the system inserts since the change token you specify.
- [updatedLocalIdentifiers](updatedlocalidentifiers.md) — The local identifiers the system updates since the change token you specify.
