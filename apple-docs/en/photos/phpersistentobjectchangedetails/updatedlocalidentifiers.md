---
title: updatedLocalIdentifiers
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentobjectchangedetails/updatedlocalidentifiers
source_url: 'https://developer.apple.com/documentation/photos/phpersistentobjectchangedetails/updatedlocalidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentobjectchangedetails/updatedlocalidentifiers.json'
content_hash: 'sha256:81d44eeda0be822f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPersistentObjectChangeDetails](../phpersistentobjectchangedetails.md)

# updatedLocalIdentifiers

<sub>Instance Property</sub>

The local identifiers the system updates since the change token you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var updatedLocalIdentifiers: Set<String> { get }
```

## Discussion

This value includes assets the user moves to the trash or hides, so they may later be available if the user removes an asset from the trash or unhides it.

## See Also

### Getting the Change Details

- [insertedLocalIdentifiers](insertedlocalidentifiers.md) — The local identifiers the system inserts since the change token you specify.
- [deletedLocalIdentifiers](deletedlocalidentifiers.md) — The local identifiers the system deletes since the change token you specify.
