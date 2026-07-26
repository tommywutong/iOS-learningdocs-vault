---
title: UICollectionViewDropProposal.Intent
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropproposal/intent-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum.json'
content_hash: 'sha256:629d98f004d16637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropProposal](../uicollectionviewdropproposal.md)

# UICollectionViewDropProposal.Intent

<sub>Enumeration</sub>

Constants indicating how you intend to handle a drop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Intent
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UICollectionViewDropIntentInsertAtDestinationIndexPath](intent-swift.enum/insertatdestinationindexpath.md) — Insert the dropped items at the specified index path.
- [UICollectionViewDropIntentInsertIntoDestinationIndexPath](intent-swift.enum/insertintodestinationindexpath.md) — Incorporate the dropped items into the item at the specified index path.
- [UICollectionViewDropIntentUnspecified](intent-swift.enum/unspecified.md) — No drop proposal was specified.

### Initializers

- [init(rawValue:)](<intent-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the Proposed Drop Location

- [intent](intent-swift.property.md) — The option to use when incorporating the dropped items into your content.
- [UIDropOperation](../uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
