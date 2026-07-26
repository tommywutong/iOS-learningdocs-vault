---
title: changedObjects
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresultchangedetails/changedobjects
source_url: 'https://developer.apple.com/documentation/photos/phfetchresultchangedetails/changedobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresultchangedetails/changedobjects.json'
content_hash: 'sha256:0c5c070ad8c057d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResultChangeDetails](../phfetchresultchangedetails.md)

# changedObjects

<sub>Instance Property</sub>

The objects in the fetch result whose content or metadata have been updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var changedObjects: [ObjectType] { get }
```

## Discussion

An array of [PHAsset](../phasset.md), [PHAssetCollection](../phassetcollection.md), or [PHCollectionList](../phcollectionlist.md) objects.

If the [hasIncrementalChanges](hasincrementalchanges.md) property’s value is `false`, this property’s value is `nil`.

## See Also

### Getting Change Information

- [hasIncrementalChanges](hasincrementalchanges.md) — A Boolean value that indicates whether changes to the fetch result can be described incrementally.
- [removedIndexes](removedindexes.md) — The indexes from which objects have been removed from the fetch result.
- [removedObjects](removedobjects.md) — The items that have been removed from the fetch result.
- [insertedIndexes](insertedindexes.md) — The indexes where new objects have been inserted in the fetch result.
- [insertedObjects](insertedobjects.md) — The new items that have been inserted in the fetch result.
- [changedIndexes](changedindexes.md) — The indexes of objects in the fetch result whose content or metadata have been updated.
- [hasMoves](hasmoves.md) — A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [- enumerateMovesWithBlock:](<enumeratemoves(__).md>) — Runs the specified block for each case where an object has moved from one index to another in the fetch result.
