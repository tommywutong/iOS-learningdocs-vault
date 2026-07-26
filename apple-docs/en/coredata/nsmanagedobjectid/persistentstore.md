---
title: persistentStore
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectid/persistentstore
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectid/persistentstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectid/persistentstore.json'
content_hash: 'sha256:efa2ed8b67b9158a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectID](../nsmanagedobjectid.md)

# persistentStore

<sub>Instance Property</sub>

The persistent store that fetched the object for the object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var persistentStore: NSPersistentStore? { get }
```

## Discussion

`nil` if the ID is for a newly-inserted object that has not yet been saved to a persistent store.

## See Also

### Getting Managed Object ID Information

- [entity](entity.md) — The entity description associated with the object ID.
- [temporaryID](istemporaryid.md) — A Boolean value that indicates whether the object ID is temporary.
- [- URIRepresentation](<urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.
