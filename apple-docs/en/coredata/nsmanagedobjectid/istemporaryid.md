---
title: isTemporaryID
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectid/istemporaryid
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectid/istemporaryid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectid/istemporaryid.json'
content_hash: 'sha256:89258f3a1e6f3367'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectID](../nsmanagedobjectid.md)

# isTemporaryID

<sub>Instance Property</sub>

A Boolean value that indicates whether the object ID is temporary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isTemporaryID: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver is temporary, otherwise [false](../../swift/false.md). Most object IDs return [false](../../swift/false.md). New objects inserted into a managed object context are assigned a temporary ID which is replaced with a permanent one once the object gets saved to a persistent store.

## See Also

### Getting Managed Object ID Information

- [entity](entity.md) — The entity description associated with the object ID.
- [persistentStore](persistentstore.md) — The persistent store that fetched the object for the object ID.
- [- URIRepresentation](<urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.
