---
title: PHCollectionListSubtype.momentListYear
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phcollectionlistsubtype/momentlistyear
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistsubtype/momentlistyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistsubtype/momentlistyear.json'
content_hash: 'sha256:2fad4eea3deeee46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListSubtype](../phcollectionlistsubtype.md)

# PHCollectionListSubtype.momentListYear

<sub>Case</sub>

The collection list is a moment year, grouping all moments from one or more calendar years.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case momentListYear
```

## Discussion

This subtype applies only to collection lists whose type is [PHCollectionListTypeMomentList](../phcollectionlisttype/momentlist.md).

## See Also

### Constants

- [PHCollectionListSubtypeMomentListCluster](momentlistcluster.md) — The collection list is a moment cluster, grouping several related moments. _(deprecated)_
- [PHCollectionListSubtypeRegularFolder](regularfolder.md) — The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtypeRootFolder](rootfolder.md) — The collection list that contains the top-level user collections, there is always one root folder in the library and does not allow `PHCollectionEditOperationRename` or `PHCollectionEditOperationDelete` _(beta)_
- [PHCollectionListSubtypeSmartFolderEvents](smartfolderevents.md) — The collection list is a smart folder containing one or more Events synced from iPhoto.
- [PHCollectionListSubtypeSmartFolderFaces](smartfolderfaces.md) — The collection list is a smart folder containing one or more Faces synced from iPhoto.
- [PHCollectionListSubtypeAny](any.md) — Use this value to fetch collection lists of all possible subtypes.
