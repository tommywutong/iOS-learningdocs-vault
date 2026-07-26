---
title: objectID
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/objectid
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/objectid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/objectid.json'
content_hash: 'sha256:efca081680f485e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# objectID

<sub>Instance Property</sub>

The object ID of the managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var objectID: NSManagedObjectID { get }
```

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

> [!important] Important
> If the receiver has not yet been saved, the object ID is a temporary value that will change when the object is saved.

## See Also

### Related Documentation

- [- URIRepresentation](<../nsmanagedobjectid/urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.

### Getting a Managed Object’s Identity

- [entity](entity-swift.property.md) — The entity description of the managed object.
- [+ entity](<entity().md>) — Returns the entity description that is associated with this subclass.
