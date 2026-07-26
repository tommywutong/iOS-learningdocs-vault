---
title: 'update(withValues:version:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstorenode/update(withvalues:version:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstorenode/update(withvalues:version:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstorenode/update%28withvalues%3Aversion%3A%29.json'
content_hash: 'sha256:ee3347eae3f6d2b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStoreNode](../nsincrementalstorenode.md)

# update(withValues:version:)

<sub>Instance Method</sub>

Update the values and version to reflect new data being saved to or loaded from the external store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update(withValues values: [String : Any], version: UInt64)
```

## Parameters

- `values` — A dictionary containing updated values, in the same format as that described in [- initWithObjectID:withValues:version:](<init(objectid_withvalues_version_).md>).

- `version` — The version number for the transaction.

## Discussion

Update the values and version to reflect new data being saved to or loaded from the external store.  // The values dictionary is in the same format as the initializer

## See Also

### Managing Node Data

- [objectID](objectid.md) — The object ID that identifies the data stored by the receiver.
- [- valueForPropertyDescription:](<value(for_).md>) — Returns the value for the given property.
- [version](version.md) — The version of data in the receiver.
