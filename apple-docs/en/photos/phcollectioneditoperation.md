---
title: PHCollectionEditOperation
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectioneditoperation
source_url: 'https://developer.apple.com/documentation/photos/phcollectioneditoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectioneditoperation.json'
content_hash: 'sha256:d1ef6b78bb312dc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCollectionEditOperation

<sub>Enumeration</sub>

Values identifying possible actions that a collection can support, used by the [- canPerformEditOperation:](<phcollection/canperform(__).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHCollectionEditOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHCollectionEditOperationDeleteContent](phcollectioneditoperation/deletecontent.md) — The collection supports deleting the items it contains.
- [PHCollectionEditOperationRemoveContent](phcollectioneditoperation/removecontent.md) — The collection supports removing the items it contains.
- [PHCollectionEditOperationAddContent](phcollectioneditoperation/addcontent.md) — The collection supports adding items that already exist elsewhere in the photo library.
- [PHCollectionEditOperationCreateContent](phcollectioneditoperation/createcontent.md) — The collection supports creating new items.
- [PHCollectionEditOperationRearrangeContent](phcollectioneditoperation/rearrangecontent.md) — The collection supports reordering the arrangement of items it contains.
- [PHCollectionEditOperationDelete](phcollectioneditoperation/delete.md) — The collection itself can be deleted.
- [PHCollectionEditOperationRename](phcollectioneditoperation/rename.md) — The collection itself can be renamed.

### Initializers

- [init(rawValue:)](<phcollectioneditoperation/init(rawvalue_).md>)

## See Also

### Determining Collection Capabilities

- [canContainAssets](phcollection/cancontainassets.md) — A Boolean value indicating whether the collection can contain assets.
- [canContainCollections](phcollection/cancontaincollections.md) — A Boolean value indicating whether the collection can contain other collections.
- [- canPerformEditOperation:](<phcollection/canperform(__).md>) — Returns whether the collection supports the specified editing operation.
