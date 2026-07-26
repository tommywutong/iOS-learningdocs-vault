---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/entity-swift.property
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/entity-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/entity-swift.property.json'
content_hash: 'sha256:8f99b167e17f81d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# entity

<sub>Instance Property</sub>

The entity description of the managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entity: NSEntityDescription { get }
```

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting a Managed Object’s Identity

- [objectID](objectid.md) — The object ID of the managed object.
- [+ entity](<entity().md>) — Returns the entity description that is associated with this subclass.
