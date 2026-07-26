---
title: PHCollectionListSubtype.regularFolder
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlistsubtype/regularfolder
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistsubtype/regularfolder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistsubtype/regularfolder.json'
content_hash: 'sha256:d16592cccc1957bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListSubtype](../phcollectionlistsubtype.md)

# PHCollectionListSubtype.regularFolder

<sub>Case</sub>

The collection list is a folder containing albums or other folders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case regularFolder
```

## Discussion

This subtype applies only to collection lists whose type is [PHCollectionListTypeFolder](../phcollectionlisttype/folder.md).

## See Also

### Constants

- [PHCollectionListSubtypeMomentListCluster](momentlistcluster.md) — The collection list is a moment cluster, grouping several related moments. _(deprecated)_
- [PHCollectionListSubtypeMomentListYear](momentlistyear.md) — The collection list is a moment year, grouping all moments from one or more calendar years. _(deprecated)_
- [PHCollectionListSubtypeRootFolder](rootfolder.md) — The collection list that contains the top-level user collections, there is always one root folder in the library and does not allow `PHCollectionEditOperationRename` or `PHCollectionEditOperationDelete` _(beta)_
- [PHCollectionListSubtypeSmartFolderEvents](smartfolderevents.md) — The collection list is a smart folder containing one or more Events synced from iPhoto.
- [PHCollectionListSubtypeSmartFolderFaces](smartfolderfaces.md) — The collection list is a smart folder containing one or more Faces synced from iPhoto.
- [PHCollectionListSubtypeAny](any.md) — Use this value to fetch collection lists of all possible subtypes.
