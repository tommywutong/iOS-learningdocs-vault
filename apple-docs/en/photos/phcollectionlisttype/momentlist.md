---
title: PHCollectionListType.momentList
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phcollectionlisttype/momentlist
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlisttype/momentlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlisttype/momentlist.json'
content_hash: 'sha256:d4275f1b90f7a01c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListType](../phcollectionlisttype.md)

# PHCollectionListType.momentList

<sub>Case</sub>

A group of asset collections of type [PHAssetCollectionTypeMoment](../phassetcollectiontype/moment.md).

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case momentList
```

## Discussion

Moment lists include both moment clusters and moment years. Moment clusters appear as “Collections” in the Photos app, grouping individual moments. Years group all moments containing assets created in the same calendar year.

## See Also

### Constants

- [PHCollectionListTypeFolder](folder.md) — A folder containing asset collections of type [PHAssetCollectionTypeAlbum](../phassetcollectiontype/album.md) or [PHAssetCollectionTypeSmartAlbum](../phassetcollectiontype/smartalbum.md).
- [PHCollectionListTypeSmartFolder](smartfolder.md) — A smart folder synced to the device from .
