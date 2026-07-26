---
title: PHCollectionListSubtype.rootFolder
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phcollectionlistsubtype/rootfolder
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistsubtype/rootfolder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistsubtype/rootfolder.json'
content_hash: 'sha256:a0676f5fb73dce6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListSubtype](../phcollectionlistsubtype.md)

# PHCollectionListSubtype.rootFolder

<sub>Case</sub>

The collection list that contains the top-level user collections, there is always one root folder in the library and does not allow `PHCollectionEditOperationRename` or `PHCollectionEditOperationDelete`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case rootFolder
```

## See Also

### Constants

- [PHCollectionListSubtypeMomentListCluster](momentlistcluster.md) — The collection list is a moment cluster, grouping several related moments. _(deprecated)_
- [PHCollectionListSubtypeMomentListYear](momentlistyear.md) — The collection list is a moment year, grouping all moments from one or more calendar years. _(deprecated)_
- [PHCollectionListSubtypeRegularFolder](regularfolder.md) — The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtypeSmartFolderEvents](smartfolderevents.md) — The collection list is a smart folder containing one or more Events synced from iPhoto.
- [PHCollectionListSubtypeSmartFolderFaces](smartfolderfaces.md) — The collection list is a smart folder containing one or more Faces synced from iPhoto.
- [PHCollectionListSubtypeAny](any.md) — Use this value to fetch collection lists of all possible subtypes.
