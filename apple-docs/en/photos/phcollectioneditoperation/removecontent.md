---
title: PHCollectionEditOperation.removeContent
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectioneditoperation/removecontent
source_url: 'https://developer.apple.com/documentation/photos/phcollectioneditoperation/removecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectioneditoperation/removecontent.json'
content_hash: 'sha256:7a4391299d8e0d3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionEditOperation](../phcollectioneditoperation.md)

# PHCollectionEditOperation.removeContent

<sub>Case</sub>

The collection supports removing the items it contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case removeContent
```

## Discussion

Removing an item removes it from the collection, but does not permanently delete it from the photo library.

## See Also

### Constants

- [PHCollectionEditOperationDeleteContent](deletecontent.md) — The collection supports deleting the items it contains.
- [PHCollectionEditOperationAddContent](addcontent.md) — The collection supports adding items that already exist elsewhere in the photo library.
- [PHCollectionEditOperationCreateContent](createcontent.md) — The collection supports creating new items.
- [PHCollectionEditOperationRearrangeContent](rearrangecontent.md) — The collection supports reordering the arrangement of items it contains.
- [PHCollectionEditOperationDelete](delete.md) — The collection itself can be deleted.
- [PHCollectionEditOperationRename](rename.md) — The collection itself can be renamed.
