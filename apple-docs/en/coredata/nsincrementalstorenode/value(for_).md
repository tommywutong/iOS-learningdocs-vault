---
title: 'value(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstorenode/value(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstorenode/value(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstorenode/value%28for%3A%29.json'
content_hash: 'sha256:0a5f92db85f690b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStoreNode](../nsincrementalstorenode.md)

# value(for:)

<sub>Instance Method</sub>

Returns the value for the given property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(for prop: NSPropertyDescription) -> Any?
```

## Parameters

- `prop` — A property description for one of the properties in the receiver.

## Return Value

The value for the property specified by `prop`. May return an instance of `NSNull` for to-one relationships.

## Discussion

If a relationship is `nil`, you should create a new value by invoking `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object.

## See Also

### Managing Node Data

- [objectID](objectid.md) — The object ID that identifies the data stored by the receiver.
- [- updateWithValues:version:](<update(withvalues_version_).md>) — Update the values and version to reflect new data being saved to or loaded from the external store.
- [version](version.md) — The version of data in the receiver.
