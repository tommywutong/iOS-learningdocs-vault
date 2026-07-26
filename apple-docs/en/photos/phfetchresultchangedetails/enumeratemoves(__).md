---
title: 'enumerateMoves(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phfetchresultchangedetails/enumeratemoves(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phfetchresultchangedetails/enumeratemoves(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresultchangedetails/enumeratemoves%28_%3A%29.json'
content_hash: 'sha256:4b979d7d6b10ecf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResultChangeDetails](../phfetchresultchangedetails.md)

# enumerateMoves(_:)

<sub>Instance Method</sub>

Runs the specified block for each case where an object has moved from one index to another in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enumerateMoves(_ handler: @escaping (Int, Int) -> Void)
```

## Parameters

- `handler` — A block that Photos calls to provide details about which objects in the fetch result have moved to which indexes. The block takes the following parameters: - **fromIndex** — The index of an object in the original fetch result. - **toIndex** — The index to which the object has moved in the new fetch result.

## Discussion

The `toIndex` parameter in the `handler` block is relative to the state of the fetch result after you’ve applied the changes described by the [removedIndexes](removedindexes.md), [insertedIndexes](insertedindexes.md) and [changedIndexes](changedindexes.md) properties. Therefore, if you use this method to update a collection view or similar user interface displaying the contents of the fetch result, update your UI to reflect insertions, removals, and changes before you process moves.

## See Also

### Getting Change Information

- [hasIncrementalChanges](hasincrementalchanges.md) — A Boolean value that indicates whether changes to the fetch result can be described incrementally.
- [removedIndexes](removedindexes.md) — The indexes from which objects have been removed from the fetch result.
- [removedObjects](removedobjects.md) — The items that have been removed from the fetch result.
- [insertedIndexes](insertedindexes.md) — The indexes where new objects have been inserted in the fetch result.
- [insertedObjects](insertedobjects.md) — The new items that have been inserted in the fetch result.
- [changedIndexes](changedindexes.md) — The indexes of objects in the fetch result whose content or metadata have been updated.
- [changedObjects](changedobjects.md) — The objects in the fetch result whose content or metadata have been updated.
- [hasMoves](hasmoves.md) — A Boolean value that indicates whether objects have been rearranged in the fetch result.
