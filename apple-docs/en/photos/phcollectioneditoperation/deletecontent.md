---
title: PHCollectionEditOperation.deleteContent
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectioneditoperation/deletecontent
source_url: 'https://developer.apple.com/documentation/photos/phcollectioneditoperation/deletecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectioneditoperation/deletecontent.json'
content_hash: 'sha256:fcf45b6aafcfdae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionEditOperation](../phcollectioneditoperation.md)

# PHCollectionEditOperation.deleteContent

<sub>Case</sub>

The collection supports deleting the items it contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case deleteContent
```

## Discussion

Deleting an item not only removes it from the collection, but permanently deletes it from the photo library.

## See Also

### Constants

- [PHCollectionEditOperationRemoveContent](removecontent.md) — The collection supports removing the items it contains.
- [PHCollectionEditOperationAddContent](addcontent.md) — The collection supports adding items that already exist elsewhere in the photo library.
- [PHCollectionEditOperationCreateContent](createcontent.md) — The collection supports creating new items.
- [PHCollectionEditOperationRearrangeContent](rearrangecontent.md) — The collection supports reordering the arrangement of items it contains.
- [PHCollectionEditOperationDelete](delete.md) — The collection itself can be deleted.
- [PHCollectionEditOperationRename](rename.md) — The collection itself can be renamed.
