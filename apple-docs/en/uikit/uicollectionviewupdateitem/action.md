---
title: UICollectionViewUpdateItem.Action
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewupdateitem/action
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewupdateitem/action.json'
content_hash: 'sha256:d7fc3a0ad4199f22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewUpdateItem](../uicollectionviewupdateitem.md)

# UICollectionViewUpdateItem.Action

<sub>Enumeration</sub>

Constants indicating the type of action being performed on an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Action
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UICollectionUpdateActionNone](action/none.md)
- [UICollectionUpdateActionInsert](action/insert.md)
- [UICollectionUpdateActionDelete](action/delete.md)
- [UICollectionUpdateActionReload](action/reload.md)
- [UICollectionUpdateActionMove](action/move.md)

### Initializers

- [init(rawValue:)](<action/init(rawvalue_).md>)

## See Also

### Accessing the item changes

- [indexPathBeforeUpdate](indexpathbeforeupdate.md) — The index path of the item before the update.
- [indexPathAfterUpdate](indexpathafterupdate.md) — The index path of the item after the update.
- [updateAction](updateaction.md) — The action being performed on the item.
