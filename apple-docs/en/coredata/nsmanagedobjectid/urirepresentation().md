---
title: uriRepresentation()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectid/urirepresentation()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectid/urirepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectid/urirepresentation%28%29.json'
content_hash: 'sha256:7e1295b6d9d4b2b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectID](../nsmanagedobjectid.md)

# uriRepresentation()

<sub>Instance Method</sub>

Returns a URI that provides an archiveable reference to the object for the object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uriRepresentation() -> URL
```

## Return Value

An `NSURL` object containing a URI that provides an archiveable reference to the object which the receiver represents.

## Discussion

If the corresponding managed object has not yet been saved, the object ID (and hence URI) is a temporary value that will change when the corresponding managed object is saved.

## See Also

### Related Documentation

- [- managedObjectIDForURIRepresentation:](<../nspersistentstorecoordinator/managedobjectid(forurirepresentation_).md>) — Returns the object identifier for the specified URI representation.
- [- objectWithID:](<../nsmanagedobjectcontext/object(with_).md>) — Returns either an existing object from the context or a fault that represents that object.

### Getting Managed Object ID Information

- [entity](entity.md) — The entity description associated with the object ID.
- [temporaryID](istemporaryid.md) — A Boolean value that indicates whether the object ID is temporary.
- [persistentStore](persistentstore.md) — The persistent store that fetched the object for the object ID.
