---
title: UITableViewDropProposal.Intent
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropproposal/intent-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropproposal/intent-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropproposal/intent-swift.enum.json'
content_hash: 'sha256:4e2d9e1d533dc2fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropProposal](../uitableviewdropproposal.md)

# UITableViewDropProposal.Intent

<sub>Enumeration</sub>

Constants indicating how you intend to handle a drop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Intent
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewDropIntentUnspecified](intent-swift.enum/unspecified.md) — No drop proposal was specified.
- [UITableViewDropIntentInsertAtDestinationIndexPath](intent-swift.enum/insertatdestinationindexpath.md) — Insert the dropped content at the specified index path.
- [UITableViewDropIntentInsertIntoDestinationIndexPath](intent-swift.enum/insertintodestinationindexpath.md) — Incorporate the dropped content into the row at the specified index path.
- [UITableViewDropIntentAutomatic](intent-swift.enum/automatic.md) — Incorporate the content in an appropriate way based on the drop location.

### Initializers

- [init(rawValue:)](<intent-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the proposed drop location

- [intent](intent-swift.property.md) — The option to use when incorporating dropped items into your content.
- [UIDropOperation](../uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
