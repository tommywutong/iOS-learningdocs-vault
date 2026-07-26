---
title: UICollectionViewDropProposal.Intent.insertIntoDestinationIndexPath
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropproposal/intent-swift.enum/insertintodestinationindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum/insertintodestinationindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum/insertintodestinationindexpath.json'
content_hash: 'sha256:d74646799e99f989'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionViewDropProposal](../../uicollectionviewdropproposal.md) · [Intent](../intent-swift.enum.md)

# UICollectionViewDropProposal.Intent.insertIntoDestinationIndexPath

<sub>Case</sub>

Incorporate the dropped items into the item at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case insertIntoDestinationIndexPath
```

## Discussion

Use this option when the drop target has nested content. Dropping items with this proposal causes them to be added to the drop target’s children. For example, if the drop target is a folder, use this option to add the items to the contents of that folder.
