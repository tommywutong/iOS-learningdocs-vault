---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectid/entity
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectid/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectid/entity.json'
content_hash: 'sha256:ea06d5e0ee1c0630'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectID](../nsmanagedobjectid.md)

# entity

<sub>Instance Property</sub>

The entity description associated with the object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entity: NSEntityDescription { get }
```

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [entity](../nsmanagedobject/entity-swift.property.md) — The entity description of the managed object.

### Getting Managed Object ID Information

- [temporaryID](istemporaryid.md) — A Boolean value that indicates whether the object ID is temporary.
- [persistentStore](persistentstore.md) — The persistent store that fetched the object for the object ID.
- [- URIRepresentation](<urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.
