---
title: 'moveItem(_:afterItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/moveitem%28_%3Aafteritem%3A%29.json'
content_hash: 'sha256:c369fe5b3f44a4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# moveItem(_:afterItem:)

<sub>Instance Method</sub>

Moves the item from its current position in the snapshot to the position immediately after the specified item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func moveItem(_ identifier: ItemIdentifierType, afterItem toIdentifier: ItemIdentifierType)
```

## Parameters

- `identifier` — The identifier of the item to move in the snapshot.

- `toIdentifier` — The identifier of the item after which to move the specified item.

## See Also

### Reordering items and sections

- [moveItem(_:beforeItem:)](<moveitem(__beforeitem_).md>) — Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [moveSection(_:afterSection:)](<movesection(__aftersection_).md>) — Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [moveSection(_:beforeSection:)](<movesection(__beforesection_).md>) — Moves the section from its current position in the snapshot to the position immediately before the specified section.
