---
title: insertedObjects
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nssavechangesrequest/insertedobjects
source_url: 'https://developer.apple.com/documentation/coredata/nssavechangesrequest/insertedobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssavechangesrequest/insertedobjects.json'
content_hash: 'sha256:dfb246a041a0cbc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSSaveChangesRequest](../nssavechangesrequest.md)

# insertedObjects

<sub>Instance Property</sub>

The objects that were inserted into the calling context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var insertedObjects: Set<NSManagedObject>? { get }
```

## See Also

### Getting Information about a Request

- [updatedObjects](updatedobjects.md) — The objects that were modified in the calling context.
- [deletedObjects](deletedobjects.md) — The objects that were deleted in the calling context.
- [lockedObjects](lockedobjects.md) — The objects that were flagged for optimistic locking on the calling context.
