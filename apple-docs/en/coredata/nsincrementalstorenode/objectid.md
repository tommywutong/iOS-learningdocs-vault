---
title: objectID
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsincrementalstorenode/objectid
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstorenode/objectid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstorenode/objectid.json'
content_hash: 'sha256:21c84767789edbb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStoreNode](../nsincrementalstorenode.md)

# objectID

<sub>Instance Property</sub>

The object ID that identifies the data stored by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var objectID: NSManagedObjectID { get }
```

## See Also

### Managing Node Data

- [- updateWithValues:version:](<update(withvalues_version_).md>) — Update the values and version to reflect new data being saved to or loaded from the external store.
- [- valueForPropertyDescription:](<value(for_).md>) — Returns the value for the given property.
- [version](version.md) — The version of data in the receiver.
