---
title: 'managedObjectID(forURIRepresentation:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/managedobjectid(forurirepresentation:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/managedobjectid(forurirepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/managedobjectid%28forurirepresentation%3A%29.json'
content_hash: 'sha256:207dbc3c46f26f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# managedObjectID(forURIRepresentation:)

<sub>Instance Method</sub>

Returns the object identifier for the specified URI representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func managedObjectID(forURIRepresentation url: URL) -> NSManagedObjectID?
```

## Parameters

- `url` — An URL object containing a URI that specify a managed object.

## Return Value

An object ID for the object specified by `url`.

## Discussion

The URI representation contains a UUID of the store the ID is coming from, and the coordinator can match it against the stores added to it.

## See Also

### Related Documentation

- [- objectWithID:](<../nsmanagedobjectcontext/object(with_).md>) — Returns either an existing object from the context or a fault that represents that object.
- [- URIRepresentation](<../nsmanagedobjectid/urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.
