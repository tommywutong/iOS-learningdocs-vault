---
title: PHCollectionListSubtype.smartFolderFaces
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlistsubtype/smartfolderfaces
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistsubtype/smartfolderfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistsubtype/smartfolderfaces.json'
content_hash: 'sha256:0c518d7b3f4837c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListSubtype](../phcollectionlistsubtype.md)

# PHCollectionListSubtype.smartFolderFaces

<sub>Case</sub>

The collection list is a smart folder containing one or more Faces synced from iPhoto.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case smartFolderFaces
```

## Discussion

This subtype applies only to collection lists whose type is [PHCollectionListTypeSmartFolder](../phcollectionlisttype/smartfolder.md).

## See Also

### Constants

- [PHCollectionListSubtypeMomentListCluster](momentlistcluster.md) — The collection list is a moment cluster, grouping several related moments. _(deprecated)_
- [PHCollectionListSubtypeMomentListYear](momentlistyear.md) — The collection list is a moment year, grouping all moments from one or more calendar years. _(deprecated)_
- [PHCollectionListSubtypeRegularFolder](regularfolder.md) — The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtypeRootFolder](rootfolder.md) — The collection list that contains the top-level user collections, there is always one root folder in the library and does not allow `PHCollectionEditOperationRename` or `PHCollectionEditOperationDelete` _(beta)_
- [PHCollectionListSubtypeSmartFolderEvents](smartfolderevents.md) — The collection list is a smart folder containing one or more Events synced from iPhoto.
- [PHCollectionListSubtypeAny](any.md) — Use this value to fetch collection lists of all possible subtypes.
